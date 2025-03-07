from aqt.qt import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QLabel,
    QToolButton,
    QLineEdit,
    QWidget,
    QIcon,
    QPixmap,
    QSize,
    pyqtSignal,
    QDialog,
    QListWidget,
    QListWidgetItem,
    QDialogButtonBox,
    Qt,
)


class Ui_regex_edit(QWidget):
    def setupUi(self, regex_edit):
        regex_edit.setObjectName("regex_edit")
        regex_edit.resize(421, 71)
        regex_edit.setStyleSheet("")
        self.name = QLabel(parent=regex_edit)
        self.name.setGeometry(QRect(10, 0, 311, 20))
        self.name.setObjectName("name")
        self.pattern_label = QLabel(parent=regex_edit)
        self.pattern_label.setGeometry(QRect(10, 20, 181, 21))
        self.pattern_label.setObjectName("pattern_label")
        self.pattern = QLineEdit(parent=regex_edit)
        self.pattern.setGeometry(QRect(9, 40, 181, 21))
        self.pattern.setObjectName("pattern")
        self.replacement_label = QLabel(parent=regex_edit)
        self.replacement_label.setGeometry(QRect(229, 20, 181, 21))
        self.replacement_label.setObjectName("replacement_label")
        self.replacement = QLineEdit(parent=regex_edit)
        self.replacement.setGeometry(QRect(228, 40, 181, 21))
        self.replacement.setObjectName("replacement")
        self.up = QToolButton(parent=regex_edit)
        self.up.setGeometry(QRect(340, 0, 20, 20))
        self.up.setStyleSheet("border: none; background: transparent;")
        icon = QIcon()
        icon.addPixmap(
            QPixmap(
                r"C:\Users\Hundway\AppData\Roaming\Anki2\addons21\anki-way-dict\graphics\icons\up.png"
            ),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.up.setIcon(icon)
        self.up.setIconSize(QSize(16, 20))
        self.up.setObjectName("up")
        self.down = QToolButton(parent=regex_edit)
        self.down.setGeometry(QRect(365, 0, 20, 20))
        self.down.setStyleSheet("border: none; background: transparent;")
        icon1 = QIcon()
        icon1.addPixmap(
            QPixmap(
                r"C:\Users\Hundway\AppData\Roaming\Anki2\addons21\anki-way-dict\graphics\icons\down.png"
            ),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.down.setIcon(icon1)
        self.down.setIconSize(QSize(16, 20))
        self.down.setObjectName("down")
        self.edit = QToolButton(parent=regex_edit)
        self.edit.setGeometry(QRect(390, 0, 20, 20))
        self.edit.setStyleSheet("border: none; background: transparent;")
        icon2 = QIcon()
        icon2.addPixmap(
            QPixmap(
                r"C:\Users\Hundway\AppData\Roaming\Anki2\addons21\anki-way-dict\graphics\icons\edit.png"
            ),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.edit.setIcon(icon2)
        self.edit.setIconSize(QSize(16, 20))
        self.edit.setObjectName("edit")
        self.count = QLineEdit(parent=regex_edit)
        self.count.setGeometry(QRect(9, 80, 181, 21))
        self.count.setObjectName("count")
        self.count_label = QLabel(parent=regex_edit)
        self.count_label.setGeometry(QRect(10, 60, 181, 21))
        self.count_label.setObjectName("count_label")
        self.flags = QLineEdit(parent=regex_edit)
        self.flags.setGeometry(QRect(229, 80, 180, 21))
        self.flags.setObjectName("flags")
        self.flags_label = QLabel(parent=regex_edit)
        self.flags_label.setGeometry(QRect(230, 60, 180, 21))
        self.flags_label.setObjectName("flags_label")

        self.retranslateUi(regex_edit)
        QMetaObject.connectSlotsByName(regex_edit)

    def retranslateUi(self, regex_edit):
        _translate = QCoreApplication.translate
        regex_edit.setWindowTitle(_translate("regex_edit", "Form"))
        self.name.setText(_translate("regex_edit", "Regex label"))
        self.pattern_label.setText(_translate("regex_edit", "Pattern"))
        self.replacement_label.setText(_translate("regex_edit", "Replacement"))
        self.count_label.setText(_translate("regex_edit", "Count"))
        self.flags_label.setText(_translate("regex_edit", "Flags"))


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


class Ui_add_regex(object):
    def setupUi(self, AddRegex):
        AddRegex.setObjectName("AddRegex")
        AddRegex.resize(231, 221)
        self.buttonBox = QDialogButtonBox(parent=AddRegex)
        self.buttonBox.setGeometry(QRect(10, 190, 211, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.listWidget = QListWidget(parent=AddRegex)
        self.listWidget.setGeometry(QRect(10, 10, 211, 181))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("border: none;")
        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = QListWidgetItem()
        self.listWidget.addItem(item)

        self.retranslateUi(AddRegex)
        self.buttonBox.accepted.connect(AddRegex.accept)  # type: ignore
        self.buttonBox.rejected.connect(AddRegex.reject)  # type: ignore
        QMetaObject.connectSlotsByName(AddRegex)

    def retranslateUi(self, AddRegex):
        _translate = QCoreApplication.translate
        AddRegex.setWindowTitle(_translate("AddRegex", "Add regex"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("AddRegex", "Custom"))
        item = self.listWidget.item(1)
        item.setText(_translate("AddRegex", "Redirect queries"))
        item = self.listWidget.item(2)
        item.setText(_translate("AddRegex", "Remove element"))
        item = self.listWidget.item(3)
        item.setText(_translate("AddRegex", "Remove empty elements"))
        item = self.listWidget.item(4)
        item.setText(_translate("AddRegex", "Remove styles"))
        item = self.listWidget.item(5)
        item.setText(_translate("AddRegex", "Remove tag"))
        item = self.listWidget.item(6)
        item.setText(_translate("AddRegex", "Trim leading spaces"))
        self.listWidget.setSortingEnabled(__sortingEnabled)


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
