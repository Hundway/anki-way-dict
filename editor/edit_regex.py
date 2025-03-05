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
)


class Ui_regex_edit(QWidget):
    def setupUi(self, regex_edit):
        regex_edit.setObjectName("regex_edit")
        regex_edit.resize(411, 71)
        regex_edit.setStyleSheet("")
        self.name = QLabel(parent=regex_edit)
        self.name.setGeometry(QRect(1, 0, 271, 20))
        self.name.setObjectName("name")
        self.pattern_label = QLabel(parent=regex_edit)
        self.pattern_label.setGeometry(QRect(1, 20, 181, 21))
        self.pattern_label.setObjectName("pattern_label")
        self.pattern = QLineEdit(parent=regex_edit)
        self.pattern.setGeometry(QRect(0, 40, 181, 21))
        self.pattern.setObjectName("pattern")
        self.replacement_label = QLabel(parent=regex_edit)
        self.replacement_label.setGeometry(QRect(215, 20, 181, 21))
        self.replacement_label.setObjectName("replacement_label")
        self.replacement = QLineEdit(parent=regex_edit)
        self.replacement.setGeometry(QRect(214, 40, 181, 21))
        self.replacement.setObjectName("replacement")
        self.up = QToolButton(parent=regex_edit)
        self.up.setGeometry(QRect(280, 0, 20, 20))
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
        self.down.setGeometry(QRect(305, 0, 20, 20))
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
        self.edit.setGeometry(QRect(330, 0, 20, 20))
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

        self.retranslateUi(regex_edit)
        QMetaObject.connectSlotsByName(regex_edit)

    def retranslateUi(self, regex_edit):
        _translate = QCoreApplication.translate
        regex_edit.setWindowTitle(_translate("regex_edit", "Form"))
        self.name.setText(_translate("regex_edit", "Regex label"))
        self.pattern_label.setText(_translate("regex_edit", "Pattern"))
        self.replacement_label.setText(_translate("regex_edit", "Replacement"))


class RegexEditWidget(QWidget):
    up_clicked = pyqtSignal(QWidget)
    down_clicked = pyqtSignal(QWidget)
    edit_clicked = pyqtSignal(QWidget)

    def __init__(self, name: str, pattern: str = "", replacement: str = "", parent=None):
        super().__init__(parent)
        self.ui = Ui_regex_edit()
        self.ui.setupUi(self)

        self.name = name
        self.pattern = pattern
        self.replacement = replacement
        self.set_name(self.name)
        self.set_pattern(self.pattern)
        self.set_replacement(self.replacement)
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

    def set_pattern(self, name: str):
        self.ui.pattern.setText(name)

    def set_replacement(self, name: str):
        self.ui.replacement.setText(name)

    def collapse(self):
        self.toggle_name_editable(False)
        self._reshape((401, 20))

    def expand(self):
        self.toggle_name_editable(True)
        self._reshape((401, 66))

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
