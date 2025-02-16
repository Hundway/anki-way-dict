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
    QGroupBox,
    QLabel,
    QCheckBox,
    QComboBox,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QTabWidget,
    QApplication,
    QDialog,
    QWebEngineView,
    QWebEngineSettings,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(461, 461)
        Dialog.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Dialog.setStyleSheet("")
        self.start = QPushButton(parent=Dialog)
        self.start.setGeometry(QRect(10, 430, 441, 23))
        self.start.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.start.setObjectName("start")
        self.groupBox = QGroupBox(parent=Dialog)
        self.groupBox.setGeometry(QRect(10, 280, 441, 141))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QRect(10, 20, 131, 21))
        self.label_2.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QRect(10, 50, 131, 21))
        self.label_3.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.label_3.setObjectName("label_3")
        self.overwrite_field = QCheckBox(parent=self.groupBox)
        self.overwrite_field.setGeometry(QRect(150, 110, 81, 21))
        self.overwrite_field.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.overwrite_field.setText("")
        self.overwrite_field.setObjectName("overwrite_field")
        self.label_5 = QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QRect(10, 110, 131, 21))
        self.label_5.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.label_5.setObjectName("label_5")
        self.note_type = QComboBox(parent=self.groupBox)
        self.note_type.setGeometry(QRect(150, 20, 281, 22))
        self.note_type.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.note_type.setObjectName("note_type")
        self.destination_field = QComboBox(parent=self.groupBox)
        self.destination_field.setGeometry(QRect(150, 80, 281, 22))
        self.destination_field.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.destination_field.setObjectName("destination_field")
        self.source_field = QComboBox(parent=self.groupBox)
        self.source_field.setGeometry(QRect(150, 50, 281, 22))
        self.source_field.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.source_field.setObjectName("source_field")
        self.label_4 = QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QRect(10, 80, 131, 21))
        self.label_4.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QGroupBox(parent=Dialog)
        self.groupBox_2.setGeometry(QRect(10, 10, 441, 261))
        self.groupBox_2.setAcceptDrops(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.search = QPushButton(parent=self.groupBox_2)
        self.search.setGeometry(QRect(310, 120, 121, 23))
        self.search.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.search.setObjectName("search")
        self.word = QLineEdit(parent=self.groupBox_2)
        self.word.setGeometry(QRect(310, 90, 121, 21))
        self.word.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.word.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.word.setText("")
        self.word.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word.setObjectName("word")
        self.word.setMaxLength(50)
        self.browse = QPushButton(parent=self.groupBox_2)
        self.browse.setGeometry(QRect(310, 40, 121, 23))
        self.browse.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.browse.setObjectName("browse")
        self.label = QLabel(parent=self.groupBox_2)
        self.label.setGeometry(QRect(10, 20, 191, 21))
        self.label.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.label.setObjectName("label")
        self.dictionary_path = QLineEdit(parent=self.groupBox_2)
        self.dictionary_path.setGeometry(QRect(10, 40, 281, 21))
        self.dictionary_path.setAcceptDrops(True)
        self.dictionary_path.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.dictionary_path.setText("")
        self.dictionary_path.setReadOnly(True)
        self.dictionary_path.setObjectName("dictionary_path")
        self.label_7 = QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QRect(310, 190, 121, 21))
        self.label_7.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.tabWidget = QTabWidget(parent=self.groupBox_2)
        self.tabWidget.setGeometry(QRect(10, 70, 281, 181))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName("tab_1")
        self.definition_preview = QWebEngineView(parent=self.tab_1)
        self.definition_preview.setGeometry(QRect(-1, -1, 281, 161))
        self.definition_preview.setAutoFillBackground(True)
        self.definition_preview.setStyleSheet("QTextEdit {\n    background: red;\n}")
        self.definition_preview.setObjectName("definition_preview")
        self.definition_preview.settings().setAttribute(
            QWebEngineSettings.WebAttribute.JavascriptEnabled, False
        )
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.definition_source = QTextEdit(parent=self.tab_2)
        self.definition_source.setGeometry(QRect(0, 0, 281, 161))
        self.definition_source.setStyleSheet("")
        self.definition_source.setReadOnly(True)
        self.definition_source.setObjectName("definition_source")
        self.tabWidget.addTab(self.tab_2, "")
        self.text_format = QComboBox(parent=self.groupBox_2)
        self.text_format.setGeometry(QRect(310, 210, 121, 21))
        self.text_format.setLocale(
            QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
        )
        self.text_format.setObjectName("text_format")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Waydict"))
        self.start.setText(_translate("Dialog", "Start"))
        self.groupBox.setTitle(_translate("Dialog", "Note options"))
        self.label_2.setText(_translate("Dialog", "Note type:"))
        self.label_3.setText(_translate("Dialog", "Source field:"))
        self.label_5.setText(_translate("Dialog", "Overwrite destination:"))
        self.label_4.setText(_translate("Dialog", "Destination field:"))
        self.groupBox_2.setTitle(_translate("Dialog", "Dictionary options"))
        self.search.setText(_translate("Dialog", "Search"))
        self.word.setPlaceholderText(_translate("Dialog", "Write a word"))
        self.browse.setText(_translate("Dialog", "Browse"))
        self.label.setText(_translate("Dialog", "Select a dictionary:"))
        self.label_7.setText(_translate("Dialog", "Text format:"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_1), _translate("Dialog", "Preview")
        )
        self.definition_source.setHtml(
            _translate(
                "Dialog",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
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
            r"QScrollBar::handle {[^\}]*background-color: (#[0-9a-z]{6});", style_sheet
        )[0]
        scroll_color_hover = re.findall(
            r"QScrollBar::handle:hover {[^\}]*background-color: (#[0-9a-z]{6});",
            style_sheet,
        )[0]
        scroll_color_active = re.findall(
            r"QScrollBar::handle:pressed {[^\}]*background-color: (#[0-9a-z]{6});",
            style_sheet,
        )[0]
        return scroll_color, scroll_color_hover, scroll_color_active

    def webengine_background(self, style_sheet):
        background_color = re.findall(
            r"QTextEdit[^\{}]*{[^\}]*background: #([0-9a-z]{6});", style_sheet
        )[0]
        return background_color
