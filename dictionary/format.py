from bs4 import BeautifulSoup
from .utils import (
    redirect_queries,
    remove_all_tags,
    remove_element,
    remove_tags,
    remove_all_attributes,
    remove_images,
    remove_empty_tags,
    remove_leading_spaces,
    reduce_occurence,
    trim_newline,
)


def format_definitions(definitions: str, text_format: str) -> str:
    if text_format == "HTML-Full":
        return format_html_full(definitions)
    elif text_format == "HTML-Brief":
        return format_html_brief(definitions)
    elif text_format == "Plain-Text":
        return format_plain_text(definitions)
    raise ValueError(
        'Invalid text format "{text_format}". Use "HTML-Full", "HTML-Brief", or "Plain-Text".'
    )


def format_html_full(text: str) -> str:
    """Maintain all the html present in the definitions."""
    text = redirect_queries(text)
    text = text.replace("\n", "<br>")
    return text


def format_html_brief(text: str) -> str:
    """Format html text to a brief form.

    This function removes all non-essential elements and attributes, keeping
    only list elements (ol, ul, li), img tags, and links. Queries are all
    redirected to jisho.org. Leading spaces are removed and newlines are
    trimmed at the beginning and end of the text.
    """
    # Redirect queries to the Jisho website
    text = redirect_queries(text)

    # Remove unwanted HTML elements
    text = remove_element(text, "table")
    text = remove_images(text)
    text = remove_all_attributes(text)

    # Clear empty tags to avoid formatting issues
    text = remove_empty_tags(text)

    # Remove HTML tags while maintaining the structure of block/inline
    block_tags = ["div", "p", "dl", "dt", "dd", "table", "tr"]
    inline_tags = ["span", "b", "i", "u", "em", "strong", "sub", "td", "th"]
    text = remove_tags(text, block_tags, "\n")
    text = remove_tags(text, inline_tags, " ")

    # Reduce multiple occurrences of spaces and newlines
    text = reduce_occurence(text, " ")
    text = reduce_occurence(text, "\n")
    text = reduce_occurence(text, "\.")

    # Remove leading spaces and trim newlines at the beginning and end
    text = remove_leading_spaces(text)
    text = trim_newline(text)

    # Replace newlines with HTML line breaks
    text = text.replace("\n", "<br>")
    text = text.replace("li><br>", "li>")
    text = text.replace("ol><br>", "ol>")
    text = text.replace("ul><br>", "ul>")
    text = text.replace("li> ", "li>")
    text = text.replace("ol> ", "ol>")
    text = text.replace("ul> ", "ul>")

    return text


def format_plain_text(text: str) -> str:
    """Format html text to plain.

    This function removes all HTML elements and attributes, keeping only the
    text content. Ul elements are formatted with a semicolon and ol elements
    are formatted with a number and a period. Queries are all redirected to
    jisho.org. Leading spaces are removed and newlines are trimmed at the
    beginning and end of the text.
    """
    # Remove unwanted HTML elements
    text = remove_element(text, "table")
    text = remove_images(text)

    # Clear empty tags to avoid formatting issues
    text = remove_empty_tags(text)

    # Format list elements
    text = format_ul_plain(text)
    text = format_ol_plain(text)

    # Remove HTML tags while maintaining the structure of block/inline
    block_tags = ["div", "p", "ol", "dl", "dt", "dd", "table", "tr"]
    inline_tags = [
        "span",
        "a",
        "b",
        "i",
        "u",
        "em",
        "strong",
        "sub",
        "td",
        "th",
    ]
    text = remove_tags(text, block_tags, "\n")
    text = remove_tags(text, inline_tags, " ")
    text = remove_all_tags(text)

    # Reduce multiple occurrences of spaces and newlines
    text = reduce_occurence(text, " ")
    text = reduce_occurence(text, "\n")
    text = reduce_occurence(text, "\.")

    # Remove leading spaces and trim newlines at the beginning and end
    text = remove_leading_spaces(text)
    text = trim_newline(text)

    return text.replace("\n", "<br>")


def format_ul_plain(text: str) -> str:
    """Format unordered lists to plain text."""
    soup = BeautifulSoup(text, "html.parser")

    for ul in soup.find_all("ul"):
        children = ul.find_all("li", recursive=False)

        for child in children:
            if child.text[-1].isalpha():
                child.insert_after("; ")
        if child.text[-1].isalpha():
            child.next_sibling.replace_with(".\n")

    return str(soup)


def format_ol_plain(text: str) -> str:
    """Format ordered lists to plain text."""
    soup = BeautifulSoup(text, "html.parser")

    for ol in soup.find_all("ol"):
        children = ol.findAll("li", recursive=False)

        for i, child in enumerate(children):
            if len(children) > 1:
                child.insert_before(f"{i + 1}. ")
            if not child.text[-1].isalpha() or child.string is None:
                child.insert_after("\n")
            else:
                child.insert_after(".\n")
    return str(soup)
