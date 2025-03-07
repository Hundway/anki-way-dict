from aqt.qt import (
    QLabel,
    QLineEdit,
    QWidget,
    QSize,
    pyqtSignal,
    QDialog,
)
from .add_regex_form import Ui_add_regex
from .regex_editor_form import Ui_regex_edit


class RegexEditWidget(QWidget):
    up_clicked = pyqtSignal(QWidget)
    down_clicked = pyqtSignal(QWidget)
    edit_clicked = pyqtSignal(QWidget)

    def __init__(
        self,
        name: str,
        pattern: str = "",
        replacement: str = "",
        count: str = "",
        flags: str = "",
    ):
        super().__init__()
        self.ui = Ui_regex_edit()
        self.ui.setupUi(self)
        self.set_name(name)
        self.set_pattern(pattern)
        self.set_replacement(replacement)
        self.set_count(count)
        self.set_flags(flags)
        self.geometry = QSize(401, 20)
        self.collapsed = True

        self.ui.up.clicked.connect(self.on_up)
        self.ui.down.clicked.connect(self.on_down)
        self.ui.edit.clicked.connect(self.on_edit)

    def on_up(self):
        self.up_clicked.emit(self)

    def on_down(self):
        self.down_clicked.emit(self)

    def on_edit(self):
        if self.collapsed:
            self.expand()
        else:
            self.collapse()
        self.collapsed = not self.collapsed
        self.edit_clicked.emit(self)

    def set_name(self, name: str):
        self.ui.name.setText(name)

    def set_pattern(self, pattern: str):
        self.ui.pattern.setText(pattern)

    def set_replacement(self, replacement: str):
        self.ui.replacement.setText(replacement)

    def set_count(self, count: str):
        self.ui.count.setText(count)

    def set_flags(self, flags: str):
        self.ui.flags.setText(flags)

    def get_name(self):
        return self.ui.name.text()

    def get_pattern(self):
        return self.ui.pattern.text()

    def get_replacement(self):
        return self.ui.replacement.text()

    def get_count(self):
        return self.ui.count.text()

    def get_flags(self):
        return self.ui.flags.text()

    def collapse(self):
        self.toggle_name_editable(False)
        self._reshape((401, 20))

    def expand(self):
        self.toggle_name_editable(True)
        self._reshape((401, 111))

    def toggle_name_editable(self, editable: bool):
        self.name = self.ui.name.text()
        geometry = self.ui.name.geometry()
        self.ui.name.deleteLater()

        if editable:
            geometry.setX(geometry.x() - 4)
            self.ui.name = QLineEdit(self.name, self)
            self.ui.name.setStyleSheet("border: none; background: transparent;")
        else:
            geometry.setX(geometry.x() + 4)
            self.ui.name = QLabel(self.name, self)

        self.ui.name.setGeometry(geometry)
        self.ui.name.show()

    def _reshape(self, size: tuple):
        self.ui.resize(*size)
        self.geometry = QSize(*size)

    def sizeHint(self):
        return self.geometry


class AddRegexDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_add_regex()
        self.ui.setupUi(self)

    def accept(self):
        self.current_item = self.ui.listWidget.currentItem()
        if self.current_item:
            super().accept()

    def regex_mapping(self, name):
        regex_map = {
            "Custom": ["Custom", "", "", "", ""],
            "Redirect queries": [
                "Redirect queries",
                r"\"?query=(.+?)&[^\"]+\"",
                r"https://www.google.com/search?q=\2",
                "",
                "",
            ],
            "Remove element": [
                "Remove element",
                r"<element[^>]*>.*?</element>",
                "",
                "",
                "",
            ],
            "Remove empty elements": [
                "Remove empty elements",
                r"<[^/>]*>\s*</[^>]*>",
                "",
                "",
                "",
            ],
            "Remove styles": ["Remove styles", r"style=\"[^\"]*\"", "", "", ""],
            "Remove tag": ["Remove tag", r"<tag[^>]*>", "", "", ""],
            "Trim leading spaces": ["Trim leading spaces", r"^\s+", "", "", ""],
        }
        return regex_map[name]
