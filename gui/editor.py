import aqt
import aqt.qt
import logging
import re
from anki.notes import Note
from anki.collection import Collection
from aqt import mw
from aqt.browser import Browser
from aqt.editor import Editor
from aqt.operations import CollectionOp, QueryOp
from aqt.operations.note import OpChangesWithCount
from aqt.qt import (
    QDialog,
    QFileDialog,
    QComboBox,
    QRadioButton,
    QListWidgetItem,
    QSize,
    QAbstractItemView,
)
from aqt.utils import tooltip
from bs4 import BeautifulSoup
from typing import Union

from ..dictionary import Dictionary
from . import editor_form as form
from .regex_edit import RegexEditWidget, AddRegexDialog


class EditorDialog(QDialog):
    def __init__(
        self,
        context: Union[Editor, Browser],
        nids: list[int] = None,
    ) -> None:
        if nids is None:
            self.editor = context
            self.browser = None
            self.parent_window = self.editor.parentWindow
            self.note = self.editor.note
        else:
            self.editor = None
            self.browser = context
            self.parent_window = self.browser
            self.nids = nids

        QDialog.__init__(self, self.parent_window)
        self.form = form.Ui_Dialog()
        self.form.setupUi(self)
        self.show()
        self.config = mw.addonManager.getConfig(__name__)
        self.dictionary = None

        note_types = [note_type.name for note_type in mw.col.models.all_names_and_ids()]
        self.form.note_type.addItems(note_types)
        self.form.text_format.addItems(["HTML-Full", "HTML-Brief", "Plain-Text"])

        self.update_dict_path(self.config["dictionary_path"])
        self.update_definition_view("")
        self.update_combo(self.form.text_format, self.config["text_format"])
        self.update_combo(self.form.note_type, self.config["note_type"])
        self.update_field_items()
        self.update_combo(self.form.source_field, self.config["source_field"])
        self.update_combo(self.form.destination_field, self.config["destination_field"])
        self.form.overwrite_destination.setChecked(self.config["overwrite_destination"])
        for item in self.config["regex_formatter"]:
            self.add_regex_item(**item)

        self.form.browse.clicked.connect(self.on_browse)
        self.form.search.clicked.connect(self.on_search)
        self.form.text_format.currentIndexChanged.connect(self.on_text_format_change)
        self.form.prev.clicked.connect(self.on_prev)
        self.form.next.clicked.connect(self.on_next)
        self.form.start.clicked.connect(self.on_start)
        self.form.add.clicked.connect(self.on_item_add)
        self.form.remove.clicked.connect(self.on_item_remove)
        self.form.clone.clicked.connect(self.on_item_clone)

        self.form.note_type.currentIndexChanged.connect(self.update_field_items)
        self.form.note_type.currentIndexChanged.connect(
            lambda: self.on_combo_change(self.form.note_type)
        )
        self.form.source_field.currentIndexChanged.connect(
            lambda: self.on_combo_change(self.form.source_field)
        )
        self.form.destination_field.currentIndexChanged.connect(
            lambda: self.on_combo_change(self.form.destination_field)
        )
        self.form.overwrite_destination.stateChanged.connect(
            lambda: self.on_radio_change(self.form.overwrite_destination)
        )

    def update_dict_path(self, path: str) -> None:
        if Dictionary.validate_file(path):
            self.form.dictionary_title.setText(Dictionary.fetch_title(path))

    def update_combo(self, combo: QComboBox, value: str) -> None:
        if value not in [combo.itemText(i) for i in range(combo.count())]:
            value = combo.itemText(0)
        combo.setCurrentText(value)

    def update_field_items(self) -> None:
        note_type = self.form.note_type.currentText()
        note_type = mw.col.models.by_name(note_type)
        field_names = mw.col.models.field_names(note_type)

        self.form.source_field.clear()
        self.form.destination_field.clear()

        self.form.source_field.addItems(field_names)
        self.form.destination_field.addItems(field_names)

    def update_definition_view(self, definition: str) -> None:
        self.update_definition_preview(definition)
        self.update_definition_source(definition)

    def update_definition_preview(self, text: str) -> None:
        self.form.definition_preview.update_html(text)

    def update_definition_source(self, text: str) -> None:
        if "HTML" in self.config["text_format"]:
            text = BeautifulSoup(text, "html.parser").prettify()
        self.form.definition_source.setPlainText(text)

    def import_dictionary(self, path: str) -> None:
        def save(path: str):
            self.dictionary = Dictionary(path)

        QueryOp(
            op=lambda col: save(path),
            success=lambda _: _,
            parent=self.parent_window,
        ).with_progress("Importing dictionary...").run_in_background()

    def on_text_format_change(self) -> None:
        self.config["text_format"] = self.form.text_format.currentText()
        self.on_search()

    def on_combo_change(self, combo: QComboBox) -> None:
        self.config[combo.objectName()] = combo.currentText()

    def on_radio_change(self, radio: QRadioButton) -> None:
        self.config[radio.objectName()] = radio.isChecked()

    def on_prev(self) -> None:
        current_index = self.form.stackedWidget.currentIndex()
        if current_index > 0:
            self.form.stackedWidget.setCurrentIndex(current_index - 1)

    def on_next(self) -> None:
        current_index = self.form.stackedWidget.currentIndex()
        if current_index < self.form.stackedWidget.count() - 1:
            self.form.stackedWidget.setCurrentIndex(current_index + 1)

    def on_browse(self) -> None:
        path = QFileDialog.getOpenFileName(
            self, "Open the dictionary", "", "ZIP Files (*.zip)"
        )[0]

        if not path:
            return

        if Dictionary.validate_file(path):
            self.config["dictionary_path"] = path
            self.form.dictionary_title.setText(Dictionary.fetch_title(path))
            self.import_dictionary(path)
        else:
            tooltip("Select a valid dictionary file.", parent=self.parent_window)

    def on_search(self) -> None:
        def lookup_definition(word: str) -> str:
            definition = self.dictionary.find_definition(word, self.config["text_format"])
            for item in self.config["regex_formatter"]:
                definition = apply_regex(definition, item)
            return definition if definition else f"No entries found for '{word}'."

        word = self.form.word.text()

        if not word:
            return

        if self.dictionary is None:
            if Dictionary.validate_file(self.config["dictionary_path"]):
                self.import_dictionary(self.config["dictionary_path"])
            else:
                tooltip("Select a valid dictionary file.", parent=self.parent_window)
                return

        QueryOp(
            op=lambda _: lookup_definition(word),
            success=lambda definition: self.update_definition_view(definition),
            parent=self.parent_window,
        ).run_in_background()

    def on_start(self) -> None:
        def op(col: Collection) -> OpChangesWithCount:
            if self.editor is not None:
                note = add_note_definition(self.editor.note, self.dictionary)

                if note is None:
                    return OpChangesWithCount(changes=None, count=0)

                return OpChangesWithCount(changes=col.update_note(note), count=1)
            else:
                notes = bulk_add_note_definition(self.nids, self.dictionary)
                return OpChangesWithCount(
                    changes=col.update_notes(notes), count=len(notes)
                )

        def on_success(changes: OpChangesWithCount) -> None:
            tooltip(f"Updated {changes.count} notes.", parent=self.parent_window)

        self.save_config()
        if self.dictionary is None:
            if Dictionary.validate_file(self.config["dictionary_path"]):
                self.import_dictionary(self.config["dictionary_path"])
            else:
                tooltip("Select a valid dictionary file.", parent=self.parent_window)
                return

        CollectionOp(self.parent_window, op).success(on_success).run_in_background()
        self.close()

    def save_config(self) -> None:
        mw.addonManager.writeConfig(__name__, self.config)

    def add_regex_item(
        self,
        name: str,
        pattern: str = "",
        replacement: str = "",
        count: str = "",
        flags: str = "",
        idx: int = -1,
    ) -> tuple[QListWidgetItem, RegexEditWidget]:
        item = QListWidgetItem()
        item.setSizeHint(QSize(411, 22))
        widget = RegexEditWidget(name, pattern, replacement, count, flags)

        idx = idx if idx >= 0 else self.form.regex_list.count()

        self.form.regex_list.insertItem(idx, item)
        self.form.regex_list.setItemWidget(item, widget)

        widget.up_clicked.connect(self.on_item_up)
        widget.down_clicked.connect(self.on_item_down)
        widget.edit_clicked.connect(self.on_item_edit)

        return item, widget

    def on_item_up(self, widget: RegexEditWidget) -> None:
        item = self.form.regex_list.itemAt(widget.pos())
        idx = self.form.regex_list.row(item)

        if idx > 0:
            self.form.regex_list.takeItem(idx)
            item, widget = self.add_regex_item(**self.regex_to_dict(widget), idx=idx - 1)
            self.config["regex_formatter"].pop(idx)
            self.config["regex_formatter"].insert(idx - 1, self.regex_to_dict(widget))

        item.setSelected(True)

    def on_item_down(self, widget: RegexEditWidget) -> None:
        item = self.form.regex_list.itemAt(widget.pos())
        idx = self.form.regex_list.row(item)

        if idx < self.form.regex_list.count() - 1:
            self.form.regex_list.takeItem(idx)
            item, widget = self.add_regex_item(**self.regex_to_dict(widget), idx=idx + 1)
            self.config["regex_formatter"].pop(idx)
            self.config["regex_formatter"].insert(idx + 1, self.regex_to_dict(widget))

        item.setSelected(True)

    def on_item_edit(self, widget: RegexEditWidget) -> None:
        item = self.form.regex_list.itemAt(widget.pos())
        item.setSizeHint(widget.sizeHint())
        idx = self.form.regex_list.row(item)

        if widget.collapsed:
            self.form.regex_list.setSelectionMode(
                QAbstractItemView.SelectionMode.SingleSelection
            )
            item.setSelected(True)
            self.form.regex_list.verticalScrollBar().setDisabled(False)
            self.config["regex_formatter"][idx] = self.regex_to_dict(widget)

        else:
            self.form.regex_list.scrollToItem(item)
            item.setSelected(False)
            self.form.regex_list.setSelectionMode(
                QAbstractItemView.SelectionMode.NoSelection
            )
            self.form.regex_list.verticalScrollBar().setDisabled(True)

    def on_item_clone(self) -> None:
        item = self.form.regex_list.currentItem()
        idx = self.form.regex_list.row(item)
        item = self.regex_to_dict(item)
        self.add_regex_item(**item, idx=idx + 1)
        self.config["regex_formatter"].insert(idx + 1, item)

    def on_item_remove(self) -> None:
        item = self.form.regex_list.currentItem()
        idx = self.form.regex_list.row(item)
        self.form.regex_list.takeItem(idx)
        self.config["regex_formatter"].pop(idx)

    def on_item_add(self) -> None:
        dialog = AddRegexDialog()
        dialog.exec()

        if dialog.result() != QDialog.DialogCode.Accepted:
            return

        regex_args = dialog.regex_mapping(dialog.current_item.text())
        _, widget = self.add_regex_item(*regex_args)
        self.config["regex_formatter"].append(self.regex_to_dict(widget))

    def regex_to_dict(self, item: Union[RegexEditWidget, QListWidgetItem]) -> dict:
        if isinstance(item, RegexEditWidget):
            widget = item
        elif isinstance(item, QListWidgetItem):
            widget = self.form.regex_list.itemWidget(item)
        return {
            "name": widget.get_name(),
            "pattern": widget.get_pattern(),
            "replacement": widget.get_replacement(),
            "count": widget.get_count(),
            "flags": widget.get_flags(),
        }


def bulk_add_note_definition(nids: list[int], dictionary: Dictionary) -> list[Note]:
    note_list = []
    for i, note_id in enumerate(nids, 1):
        note = mw.col.get_note(note_id)
        note = add_note_definition(note, dictionary)

        if isinstance(note, Note):
            note_list.append(note)

        aqt.mw.taskman.run_on_main(
            lambda: aqt.mw.progress.update(
                label=f"Fetching definitions: {i}/{len(nids)}",
                value=i,
                max=len(nids),
            )
        )
    return note_list


def add_note_definition(note: Note, dictionary: Dictionary) -> Union[Note, None]:
    config = mw.addonManager.getConfig(__name__)

    if not validate_update(note, config):
        return None

    definition = dictionary.find_definition(
        note[config["source_field"]], config["text_format"]
    )

    for item in config["regex_formatter"]:
        definition = apply_regex(definition, item)

    if not definition:
        return None

    note[config["destination_field"]] = definition

    return note


def validate_update(note: Note, config: dict) -> bool:
    note_type = mw.col.models.get(note.note_type()["id"])["name"]
    note_fields = mw.col.models.field_names(note.note_type())

    if config["note_type"] != note_type:
        return False
    if config["source_field"] not in note_fields:
        return False
    if config["destination_field"] not in note_fields:
        return False
    if note[config["destination_field"]] != "" and not config["overwrite_destination"]:
        return False

    return True


def apply_regex(text: str, regex_args: dict) -> str:
    pattern = regex_args["pattern"]
    repl = regex_args["replacement"]
    count = int(regex_args["count"])
    flags = parse_regex_flags(regex_args["flags"])

    try:
        return re.sub(pattern, repl, text, count, flags)
    except re.error as e:
        logging.error(e)
        return text


def parse_regex_flags(flags: str) -> int:
    flags = flags.replace(" ", "").split("|")
    flag_mask = 0
    for flag in flags:
        flag_mask |= getattr(re, flag)
    return flag_mask
