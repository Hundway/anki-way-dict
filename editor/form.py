from aqt.qt import (
    QLocale,
    Qt,
    QCoreApplication,
    QMetaObject,
    QRect,
    QWidget,
    QLabel,
    QCheckBox,
    QComboBox,
    QPushButton,
    QToolButton,
    QLineEdit,
    QTextEdit,
    QTabWidget,
    QFrame,
    QFont,
    QStackedWidget,
    QListWidget,
    QIcon,
    QPixmap,
    QIcon,
)
from pathlib import Path
from .definition_web_view import DefinitionWebView


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(460, 470)
        Dialog.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.dictionary_options_label = QLabel(parent=Dialog)
        self.dictionary_options_label.setGeometry(QRect(20, 10, 191, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dictionary_options_label.setFont(font)
        self.dictionary_options_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.dictionary_options_label.setObjectName("dictionary_options_label")
        self.dictionary_options_line = QFrame(parent=Dialog)
        self.dictionary_options_line.setGeometry(QRect(20, 30, 421, 20))
        self.dictionary_options_line.setFrameShape(QFrame.Shape.HLine)
        self.dictionary_options_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.dictionary_options_line.setObjectName("dictionary_options_line")
        self.dictionary_title = QLineEdit(parent=Dialog)
        self.dictionary_title.setGeometry(QRect(20, 50, 281, 21))
        self.dictionary_title.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.dictionary_title.setAcceptDrops(True)
        self.dictionary_title.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.dictionary_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dictionary_title.setReadOnly(True)
        self.dictionary_title.setObjectName("dictionary_title")
        self.browse = QPushButton(parent=Dialog)
        self.browse.setGeometry(QRect(320, 50, 121, 23))
        self.browse.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.browse.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        icon = QIcon()
        icon.addPixmap(
            QPixmap(str(Path(__file__).parent.parent / "graphics/icons/browse.png")),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.browse.setIcon(icon)
        self.browse.setObjectName("browse")
        self.tabWidget = QTabWidget(parent=Dialog)
        self.tabWidget.setGeometry(QRect(20, 90, 281, 181))
        self.tabWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.preview = QWidget()
        self.preview.setObjectName("preview")
        self.definition_preview = DefinitionWebView(parent=self.preview)
        self.definition_preview.setGeometry(QRect(0, 0, 281, 156))
        self.definition_preview.setAutoFillBackground(True)
        self.definition_preview.setObjectName("definition_preview")
        self.tabWidget.addTab(self.preview, "")
        self.source = QWidget()
        self.source.setObjectName("source")
        self.definition_source = QTextEdit(parent=self.source)
        self.definition_source.setGeometry(QRect(-1, 0, 281, 156))
        self.definition_source.setStyleSheet("")
        self.definition_source.setReadOnly(True)
        self.definition_source.setObjectName("definition_source")
        self.tabWidget.addTab(self.source, "")
        self.word = QLineEdit(parent=Dialog)
        self.word.setGeometry(QRect(320, 100, 121, 21))
        self.word.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.word.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.word.setMaxLength(30)
        self.word.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word.setObjectName("word")
        self.search = QPushButton(parent=Dialog)
        self.search.setGeometry(QRect(320, 130, 121, 23))
        self.search.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.search.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        icon1 = QIcon()
        icon1.addPixmap(
            QPixmap(str(Path(__file__).parent.parent / "graphics/icons/search.png")),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.search.setIcon(icon1)
        self.search.setObjectName("search")
        self.text_format_label = QLabel(parent=Dialog)
        self.text_format_label.setGeometry(QRect(320, 220, 121, 21))
        self.text_format_label.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.text_format_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_format_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.text_format_label.setObjectName("text_format_label")
        self.text_format = QComboBox(parent=Dialog)
        self.text_format.setGeometry(QRect(320, 250, 121, 21))
        self.text_format.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.text_format.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.text_format.setObjectName("text_format")
        self.stackedWidget = QStackedWidget(parent=Dialog)
        self.stackedWidget.setGeometry(QRect(20, 280, 421, 191))
        self.stackedWidget.setObjectName("stackedWidget")
        self.note_options = QWidget()
        self.note_options.setObjectName("note_options")
        self.note_options_label = QLabel(parent=self.note_options)
        self.note_options_label.setGeometry(QRect(0, 0, 191, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.note_options_label.setFont(font)
        self.note_options_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.note_options_label.setObjectName("note_options_label")
        self.note_options_line = QFrame(parent=self.note_options)
        self.note_options_line.setGeometry(QRect(0, 20, 421, 20))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.note_options_line.setFont(font)
        self.note_options_line.setStyleSheet("border-color: red;")
        self.note_options_line.setFrameShape(QFrame.Shape.HLine)
        self.note_options_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.note_options_line.setObjectName("note_options_line")
        self.note_type_label = QLabel(parent=self.note_options)
        self.note_type_label.setGeometry(QRect(0, 40, 131, 21))
        self.note_type_label.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.note_type_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.note_type_label.setObjectName("note_type_label")
        self.note_type = QComboBox(parent=self.note_options)
        self.note_type.setGeometry(QRect(140, 40, 281, 22))
        self.note_type.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.note_type.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.note_type.setObjectName("note_type")
        self.source_field_label = QLabel(parent=self.note_options)
        self.source_field_label.setGeometry(QRect(0, 70, 131, 21))
        self.source_field_label.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.source_field_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.source_field_label.setObjectName("source_field_label")
        self.source_field = QComboBox(parent=self.note_options)
        self.source_field.setGeometry(QRect(140, 70, 281, 22))
        self.source_field.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.source_field.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.source_field.setObjectName("source_field")
        self.destination_field_label = QLabel(parent=self.note_options)
        self.destination_field_label.setGeometry(QRect(0, 100, 131, 21))
        self.destination_field_label.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.destination_field_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.destination_field_label.setObjectName("destination_field_label")
        self.destination_field = QComboBox(parent=self.note_options)
        self.destination_field.setGeometry(QRect(140, 100, 281, 22))
        self.destination_field.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.destination_field.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.destination_field.setObjectName("destination_field")
        self.overwrite_destination_label = QLabel(parent=self.note_options)
        self.overwrite_destination_label.setGeometry(QRect(0, 130, 131, 21))
        self.overwrite_destination_label.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.overwrite_destination_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.overwrite_destination_label.setObjectName("overwrite_destination_label")
        self.overwrite_destination = QCheckBox(parent=self.note_options)
        self.overwrite_destination.setGeometry(QRect(140, 130, 81, 21))
        self.overwrite_destination.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.overwrite_destination.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.overwrite_destination.setText("")
        self.overwrite_destination.setObjectName("overwrite_destination")
        self.start = QPushButton(parent=self.note_options)
        self.start.setGeometry(QRect(0, 160, 421, 23))
        self.start.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.start.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        icon2 = QIcon()
        icon2.addPixmap(
            QPixmap(str(Path(__file__).parent.parent / "graphics/icons/start.png")),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.start.setIcon(icon2)
        self.start.setObjectName("start")
        self.stackedWidget.addWidget(self.note_options)
        self.regex_formatter = QWidget()
        self.regex_formatter.setObjectName("regex_formatter")
        self.regex_formatter_label = QLabel(parent=self.regex_formatter)
        self.regex_formatter_label.setGeometry(QRect(0, 0, 191, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.regex_formatter_label.setFont(font)
        self.regex_formatter_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.regex_formatter_label.setObjectName("entry_style_label")
        self.entry_style_line = QFrame(parent=self.regex_formatter)
        self.entry_style_line.setGeometry(QRect(0, 20, 421, 20))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.entry_style_line.setFont(font)
        self.entry_style_line.setStyleSheet("border-color: red;")
        self.entry_style_line.setFrameShape(QFrame.Shape.HLine)
        self.entry_style_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.entry_style_line.setObjectName("entry_style_line")
        self.regex_list = QListWidget(parent=self.regex_formatter)
        self.regex_list.setGeometry(QRect(0, 40, 421, 111))
        self.regex_list.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.regex_list.setStyleSheet("QListWidget{background-color: transparent;}")
        self.regex_list.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.regex_list.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.regex_list.setObjectName("regex_list")
        self.add = QPushButton(parent=self.regex_formatter)
        self.add.setGeometry(QRect(0, 160, 131, 23))
        self.add.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.add.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        icon3 = QIcon()
        icon3.addPixmap(
            QPixmap(
                str(Path(__file__).resolve().parent.parent / "graphics/icons/add.png")
            ),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.add.setIcon(icon3)
        self.add.setObjectName("add")
        self.remove = QPushButton(parent=self.regex_formatter)
        self.remove.setGeometry(QRect(140, 160, 141, 23))
        self.remove.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.remove.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        icon4 = QIcon()
        icon4.addPixmap(
            QPixmap(
                str(Path(__file__).resolve().parent.parent / "graphics/icons/remove.png")
            ),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.remove.setIcon(icon4)
        self.remove.setObjectName("remove")
        self.clone = QPushButton(parent=self.regex_formatter)
        self.clone.setGeometry(QRect(290, 160, 131, 23))
        self.clone.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.clone.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        # show current path

        icon5 = QIcon()
        icon5.addPixmap(
            QPixmap(
                str(Path(__file__).resolve().parent.parent / "graphics/icons/clone.png")
            ),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.clone.setIcon(icon5)
        self.clone.setObjectName("clone")
        self.stackedWidget.addWidget(self.regex_formatter)
        self.next = QToolButton(parent=Dialog)
        self.next.setGeometry(QRect(420, 290, 25, 19))
        self.next.setStyleSheet("border: none; background: transparent;")
        self.next.setArrowType(Qt.ArrowType.RightArrow)
        self.next.setObjectName("next")
        self.prev = QToolButton(parent=Dialog)
        self.prev.setGeometry(QRect(400, 290, 25, 19))
        self.prev.setStyleSheet("border: none; background: transparent;")
        self.prev.setArrowType(Qt.ArrowType.LeftArrow)
        self.prev.setObjectName("prev")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Waydict"))
        self.dictionary_options_label.setText(_translate("Dialog", "Dictionary options"))
        self.dictionary_title.setPlaceholderText(
            _translate("Dialog", "Select your dictionary")
        )
        self.browse.setText(_translate("Dialog", "Browse"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.preview), _translate("Dialog", "Preview")
        )
        self.definition_source.setPlaceholderText(
            _translate(
                "Dialog",
                'The definition of the word should appear here after pressing the "search" button.',
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.source), _translate("Dialog", "Source")
        )
        self.word.setPlaceholderText(_translate("Dialog", "Enter a word"))
        self.search.setText(_translate("Dialog", "Search"))
        self.text_format_label.setText(_translate("Dialog", "Text format"))
        self.note_options_label.setText(_translate("Dialog", "Note options"))
        self.note_type_label.setText(_translate("Dialog", "Note type"))
        self.source_field_label.setText(_translate("Dialog", "Source field"))
        self.destination_field_label.setText(_translate("Dialog", "Destination field"))
        self.overwrite_destination_label.setText(
            _translate("Dialog", "Overwrite destination")
        )
        self.start.setText(_translate("Dialog", "Add definition(s)"))
        self.regex_formatter_label.setText(_translate("Dialog", "Regex formatter"))
        self.add.setText(_translate("Dialog", "Add"))
        self.remove.setText(_translate("Dialog", "Remove"))
        self.clone.setText(_translate("Dialog", "Clone"))
        self.next.setText(_translate("Dialog", "..."))
        self.prev.setText(_translate("Dialog", "..."))
