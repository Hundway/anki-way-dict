import os
import anki.hooks
import aqt
from aqt.editor import Editor
from aqt.browser import Browser
from aqt.utils import tooltip
from aqt.qt import QMenu
from .gui import EditorDialog


def editor_action(browser: Browser, menu: QMenu = None) -> None:
    def open_editor_for_selected_notes(browser: Browser) -> None:
        nids = browser.selectedNotes()
        if nids:
            EditorDialog(browser, nids)
        else:
            tooltip("No cards selected.")

    if menu is None:
        menu = browser.form.menuEdit

    menu.addSeparator()
    menu.addAction(
        "WayDict: Add definition", lambda: open_editor_for_selected_notes(browser)
    )


def editor_button(buttons: list[str], editor: Editor) -> list[str]:
    new_button = editor.addButton(
        os.path.dirname(__file__) + "/graphics/icons/editor.png",
        "WayDict: Add definition",
        EditorDialog,
        tip="Add definition",
    )
    buttons.append(new_button)


# Register action in Anki > browse > editor
anki.hooks.addHook("browser.setupMenus", editor_action)

# Register button in Anki > browse > edit
aqt.gui_hooks.editor_did_init_buttons.append(editor_button)

# Register action in Anki > browse > editor
aqt.gui_hooks.browser_will_show_context_menu.append(editor_action)
