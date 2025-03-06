from aqt import mw
from aqt.theme import colors
from aqt.theme import theme_manager as tm
from aqt.qt import (
    QUrl,
    QTextEdit,
    QWebEngineView,
    QWebEngineSettings,
)


class DefinitionWebView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style = self._get_style()
        self.update_html("")
        self.settings().setAttribute(
            QWebEngineSettings.WebAttribute.JavascriptEnabled, False
        )

    def update_html(self, body):
        if not body:
            placeholder = """
                The definition of the word should appear here
                after pressing the "search" button.
            """
            body = f'<span class="placeholder">{placeholder}</span>'

        self.setHtml(
            f"<html><head>{self.style}</head>{body}</html>",
            QUrl(f"{mw.serverURL()}_anki/waydict?id={id(self)}"),
        )

    def _get_style(self):
        font_size, font_style, font_color = self._get_font_style()
        return f"""
            <style>
                body {{
                    background-color: {tm.var(colors.CANVAS)};
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
                .placeholder {{
                    color: {tm.var(colors.FG_SUBTLE)};
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
                    background-color: {tm.var(colors.SCROLLBAR_BG)};
                    background-clip: padding-box;
                }}
                ::-webkit-scrollbar-thumb:hover {{
                    background-color: {tm.var(colors.SCROLLBAR_BG_HOVER)};
                }}
                ::-webkit-scrollbar-thumb:active {{
                    background-color: {tm.var(colors.SCROLLBAR_BG_ACTIVE)};
                }}
            </style>
        """

    def _get_font_style(self):
        pallete = QTextEdit().palette()
        foreground = QTextEdit().foregroundRole()

        font = QTextEdit().font()
        font_size = font.pointSize()
        font_style = font.family()
        font_color = pallete.color(foreground).name()

        return font_size, font_style, font_color
