import re
from aqt import mw
from aqt.qt import (
    QLocale,
    Qt,
    QCoreApplication,
    QMetaObject,
    QRect,
    QUrl,
    QWidget,
    QLabel,
    QCheckBox,
    QComboBox,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QTabWidget,
    QWebEngineView,
    QWebEngineSettings,
    QFrame,
    QFont,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(461, 481)
        Dialog.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Dialog.setStyleSheet("")
        self.start = QPushButton(parent=Dialog)
        self.start.setGeometry(QRect(10, 450, 441, 23))
        self.start.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.start.setObjectName("start")
        self.start.clearFocus()
        self.label_3 = QLabel(parent=Dialog)
        self.label_3.setGeometry(QRect(20, 350, 131, 21))
        self.label_3.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(parent=Dialog)
        self.label_4.setGeometry(QRect(20, 380, 131, 21))
        self.label_4.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.label_4.setObjectName("label_4")
        self.destination_field = QComboBox(parent=Dialog)
        self.destination_field.setGeometry(QRect(160, 380, 281, 22))
        self.destination_field.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.destination_field.setObjectName("destination_field")
        self.note_type = QComboBox(parent=Dialog)
        self.note_type.setGeometry(QRect(160, 320, 281, 22))
        self.note_type.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.note_type.setObjectName("note_type")
        self.line_2 = QFrame(parent=Dialog)
        self.line_2.setGeometry(QRect(20, 300, 421, 20))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QLabel(parent=Dialog)
        self.label_2.setGeometry(QRect(20, 320, 131, 21))
        self.label_2.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.label_2.setObjectName("label_2")
        self.overwrite_field = QCheckBox(parent=Dialog)
        self.overwrite_field.setGeometry(QRect(160, 410, 81, 21))
        self.overwrite_field.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.overwrite_field.setText("")
        self.overwrite_field.setObjectName("overwrite_field")
        self.label_6 = QLabel(parent=Dialog)
        self.label_6.setGeometry(QRect(20, 280, 191, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.source_field = QComboBox(parent=Dialog)
        self.source_field.setGeometry(QRect(160, 350, 281, 22))
        self.source_field.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.source_field.setObjectName("source_field")
        self.label_5 = QLabel(parent=Dialog)
        self.label_5.setGeometry(QRect(20, 410, 131, 21))
        self.label_5.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.label_5.setObjectName("label_5")
        self.search = QPushButton(parent=Dialog)
        self.search.setGeometry(QRect(320, 130, 121, 23))
        self.search.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.search.setObjectName("search")
        self.tabWidget = QTabWidget(parent=Dialog)
        self.tabWidget.setGeometry(QRect(20, 90, 281, 181))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName("tab_1")
        self.definition_preview = QWebEngineView(parent=self.tab_1)
        self.definition_preview.setGeometry(QRect(-1, -1, 281, 161))
        self.definition_preview.setAutoFillBackground(True)
        self.definition_preview.setStyleSheet("QTextEdit {\n    background: red;\n}")
        self.definition_preview.setObjectName("definition_preview")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.definition_source = QTextEdit(parent=self.tab_2)
        self.definition_source.setGeometry(QRect(0, 0, 281, 161))
        self.definition_source.setStyleSheet("")
        self.definition_source.setReadOnly(True)
        self.definition_source.setObjectName("definition_source")
        self.tabWidget.addTab(self.tab_2, "")
        self.dictionary_path = QLineEdit(parent=Dialog)
        self.dictionary_path.setGeometry(QRect(20, 50, 281, 21))
        self.dictionary_path.setAcceptDrops(True)
        self.dictionary_path.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.dictionary_path.setText("")
        self.dictionary_path.setReadOnly(True)
        self.dictionary_path.setObjectName("dictionary_path")
        self.text_format = QComboBox(parent=Dialog)
        self.text_format.setGeometry(QRect(320, 250, 121, 21))
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
        self.label_7.setObjectName("label_7")
        self.label = QLabel(parent=Dialog)
        self.label.setGeometry(QRect(20, 10, 191, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.word = QLineEdit(parent=Dialog)
        self.word.setGeometry(QRect(320, 100, 121, 21))
        self.word.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.word.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.word.setText("")
        self.word.setMaxLength(30)
        self.word.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word.setObjectName("word")

        self.definition_preview.settings().setAttribute(
            QWebEngineSettings.WebAttribute.JavascriptEnabled, False
        )
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Waydict"))
        self.start.setText(_translate("Dialog", "Start"))
        self.label_3.setText(_translate("Dialog", "Source field"))
        self.label_4.setText(_translate("Dialog", "Destination field"))
        self.label_2.setText(_translate("Dialog", "Note type"))
        self.label_6.setText(_translate("Dialog", "Note options"))
        self.label_5.setText(_translate("Dialog", "Overwrite destination"))
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
        self.dictionary_path.setPlaceholderText(
            _translate("Dialog", "Select your dictionary")
        )
        self.browse.setText(_translate("Dialog", "Browse"))
        self.label_7.setText(_translate("Dialog", "Text format"))
        self.label.setText(_translate("Dialog", "Dictionary options"))
        self.word.setPlaceholderText(_translate("Dialog", "Enter a word"))
        self.setupWebEngineStyle()

    def setupWebEngineStyle(self):
        style_sheet = mw.app.styleSheet()
        font_size, font_style, font_color = self.webengine_font()
        background_color = self.webengine_background(style_sheet)
        scroll, scroll_hover, scroll_active = self.webengine_scrollbar(style_sheet)

        self.definition_preview.html = f"""
        <html>
            <head>
            <style>
                body {{
                    background-color: {background_color};
                    color: {font_color};
                    font-size: {font_size}pt;
                    font-family: {font_style};
                    overflow-y: scroll;
                    margin: 0;
                    border: 0;
                    padding: 0.7em;
                }}
                ol {{
                    margin: 0;
                    border: 0;
                    padding: 0 0 0 1em;
                }}
                ul {{
                    margin: 0;
                    border: 0;
                    padding: 0 0 0 3em;
                }}
                ::-webkit-scrollbar {{
                    width: 12vmin;
                    background-color: transparent;
                }}
                ::webkit-scrollbar-track {{
                    background-color: transparent;
                }}
                ::-webkit-scrollbar-thumb {{
                    border-color: transparent;
                    border-style: solid;
                    border-width: 2vmin;
                    border-radius: 15px;
                    background-color: {scroll};
                    background-clip: padding-box;
                }}
                ::-webkit-scrollbar-thumb:hover {{
                    background-color: {scroll_hover};
                }}
                ::-webkit-scrollbar-thumb:active {{
                    background-color: {scroll_active};
                }}
            </style>
            </head>
            <body>
            </body>
        </html>
        """
        self.definition_preview.setHtml(self.definition_preview.html, QUrl("file://"))

    def webengine_font(self):
        pallete = self.definition_source.palette()
        foreground = self.definition_source.foregroundRole()
        font = self.definition_source.font()
        font_color = pallete.color(foreground).name()
        return font.pointSize(), font.family(), font_color

    def webengine_scrollbar(self, style_sheet):
        scroll_color = re.findall(
            r"QScrollBar::handle {[^\}]*background-color: ([^;]*);", style_sheet
        )
        scroll_color_hover = re.findall(
            r"QScrollBar::handle:hover {[^\}]*background-color: ([^;]*);",
            style_sheet,
        )
        scroll_color_active = re.findall(
            r"QScrollBar::handle:pressed {[^\}]*background-color: ([^;]*);",
            style_sheet,
        )

        scroll_color = scroll_color[0] if scroll_color else ""
        scroll_color_hover = scroll_color_hover[0] if scroll_color_hover else ""
        scroll_color_active = scroll_color_active[0] if scroll_color_active else ""

        return scroll_color, scroll_color_hover, scroll_color_active

    def webengine_background(self, style_sheet):
        background_color = re.findall(
            r"QTextEdit[^\{}]*{[^\}]*background: ([^;]*);", style_sheet
        )
        return background_color[0] if background_color else ""
