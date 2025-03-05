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
    QListWidgetItem,
    QSize,
)
from .edit_regex import RegexEditWidget
from .definition_web_view import DefinitionWebView


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(461, 481)
        Dialog.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.search = QPushButton(parent=Dialog)
        self.search.setGeometry(QRect(320, 130, 121, 23))
        self.search.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.search.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.search.setObjectName("search")
        self.tabWidget = QTabWidget(parent=Dialog)
        self.tabWidget.setGeometry(QRect(20, 90, 281, 181))
        self.tabWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName("tab_1")
        self.definition_preview = DefinitionWebView(parent=self.tab_1)
        self.definition_preview.setGeometry(QRect(-1, -1, 281, 151))
        self.definition_preview.setAutoFillBackground(True)
        self.definition_preview.setObjectName("definition_preview")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.definition_source = QTextEdit(parent=self.tab_2)
        self.definition_source.setGeometry(QRect(0, 0, 281, 151))
        self.definition_source.setStyleSheet("")
        self.definition_source.setReadOnly(True)
        self.definition_source.setObjectName("definition_source")
        self.tabWidget.addTab(self.tab_2, "")
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
        self.text_format = QComboBox(parent=Dialog)
        self.text_format.setGeometry(QRect(320, 250, 121, 21))
        self.text_format.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.text_format.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.text_format.setObjectName("text_format")
        self.line = QFrame(parent=Dialog)
        self.line.setGeometry(QRect(20, 30, 421, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.browse = QPushButton(parent=Dialog)
        self.browse.setGeometry(QRect(320, 50, 121, 23))
        self.browse.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.browse.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.browse.setObjectName("browse")
        self.label_7 = QLabel(parent=Dialog)
        self.label_7.setGeometry(QRect(320, 220, 121, 21))
        self.label_7.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.label_7.setObjectName("label_7")
        self.label = QLabel(parent=Dialog)
        self.label.setGeometry(QRect(20, 10, 191, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.label.setObjectName("label")
        self.word = QLineEdit(parent=Dialog)
        self.word.setGeometry(QRect(320, 100, 121, 21))
        self.word.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.word.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.word.setMaxLength(30)
        self.word.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word.setObjectName("word")
        self.stackedWidget = QStackedWidget(parent=Dialog)
        self.stackedWidget.setGeometry(QRect(20, 280, 421, 191))
        self.stackedWidget.setObjectName("stackedWidget")
        self.note_options = QWidget()
        self.note_options.setObjectName("note_options")
        self.label_3 = QLabel(parent=self.note_options)
        self.label_3.setGeometry(QRect(0, 70, 131, 21))
        self.label_3.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.label_3.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.label_3.setObjectName("label_3")
        self.label_5 = QLabel(parent=self.note_options)
        self.label_5.setGeometry(QRect(0, 130, 131, 21))
        self.label_5.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.label_5.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.label_5.setObjectName("label_5")
        self.label_2 = QLabel(parent=self.note_options)
        self.label_2.setGeometry(QRect(0, 40, 131, 21))
        self.label_2.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.label_2.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.label_2.setObjectName("label_2")
        self.label_6 = QLabel(parent=self.note_options)
        self.label_6.setGeometry(QRect(0, 0, 191, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.label_6.setObjectName("label_6")
        self.label_4 = QLabel(parent=self.note_options)
        self.label_4.setGeometry(QRect(0, 100, 131, 21))
        self.label_4.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.label_4.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.label_4.setObjectName("label_4")
        self.destination_field = QComboBox(parent=self.note_options)
        self.destination_field.setGeometry(QRect(140, 100, 281, 22))
        self.destination_field.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.destination_field.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.destination_field.setObjectName("destination_field")
        self.note_type = QComboBox(parent=self.note_options)
        self.note_type.setGeometry(QRect(140, 40, 281, 22))
        self.note_type.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.note_type.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.note_type.setObjectName("note_type")
        self.line_2 = QFrame(parent=self.note_options)
        self.line_2.setGeometry(QRect(0, 20, 421, 20))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("border-color: red;")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.start = QPushButton(parent=self.note_options)
        self.start.setGeometry(QRect(0, 160, 421, 23))
        self.start.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.start.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.start.setObjectName("start")
        self.overwrite_destination = QCheckBox(parent=self.note_options)
        self.overwrite_destination.setGeometry(QRect(140, 130, 81, 21))
        self.overwrite_destination.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.overwrite_destination.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.overwrite_destination.setText("")
        self.overwrite_destination.setObjectName("overwrite_destination")
        self.source_field = QComboBox(parent=self.note_options)
        self.source_field.setGeometry(QRect(140, 70, 281, 22))
        self.source_field.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.source_field.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.source_field.setObjectName("source_field")
        self.stackedWidget.addWidget(self.note_options)
        self.entry_format = QWidget()
        self.entry_format.setObjectName("entry_format")
        self.line_3 = QFrame(parent=self.entry_format)
        self.line_3.setGeometry(QRect(0, 20, 421, 20))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_3.setFont(font)
        self.line_3.setStyleSheet("border-color: red;")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.regex_list = QListWidget(parent=self.entry_format)
        self.regex_list.setGeometry(QRect(0, 41, 421, 141))
        self.regex_list.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.regex_list.setStyleSheet(
            "QListWidget{background-color: transparent; padding: 5px;}"
        )
        self.regex_list.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.regex_list.setObjectName("regex_list")
        self.label_8 = QLabel(parent=self.entry_format)
        self.label_8.setGeometry(QRect(0, 0, 191, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.entry_format)
        self.prev = QToolButton(parent=Dialog)
        self.prev.setGeometry(QRect(400, 290, 25, 19))
        self.prev.setStyleSheet("border: none; background: transparent;")
        self.prev.setArrowType(Qt.ArrowType.LeftArrow)
        self.prev.setObjectName("prev")
        self.next = QToolButton(parent=Dialog)
        self.next.setGeometry(QRect(420, 290, 25, 19))
        self.next.setStyleSheet("border: none; background: transparent;")
        self.next.setArrowType(Qt.ArrowType.RightArrow)
        self.next.setObjectName("next")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Waydict"))
        self.search.setText(_translate("Dialog", "Search"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_1), _translate("Dialog", "Preview")
        )
        self.definition_source.setPlaceholderText(
            _translate(
                "Dialog",
                'The definition of the word should appear here after pressing the "search" button.',
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Source")
        )
        self.dictionary_title.setPlaceholderText(
            _translate("Dialog", "Select your dictionary")
        )
        self.browse.setText(_translate("Dialog", "Browse"))
        self.label_7.setText(_translate("Dialog", "Text format"))
        self.label.setText(_translate("Dialog", "Dictionary options"))
        self.word.setPlaceholderText(_translate("Dialog", "Enter a word"))
        self.label_3.setText(_translate("Dialog", "Source field"))
        self.label_5.setText(_translate("Dialog", "Overwrite destination"))
        self.label_2.setText(_translate("Dialog", "Note type"))
        self.label_6.setText(_translate("Dialog", "Note options"))
        self.label_4.setText(_translate("Dialog", "Destination field"))
        self.start.setText(_translate("Dialog", "Start"))
        self.label_8.setText(_translate("Dialog", "Entry style"))
        self.prev.setText(_translate("Dialog", "..."))
        self.next.setText(_translate("Dialog", "..."))
