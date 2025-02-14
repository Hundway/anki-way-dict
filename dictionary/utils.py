import re


def double_to_single_quotes(text: str) -> str:
    """Convert double quotes to single quotes."""
    return text.replace('"', "'")


def camel_to_dash(text: str) -> str:
    """Convert camel case to dash case."""
    return re.sub(r"(?<=[a-z])([A-Z])", r"-\1", text).lower()


def redirect_queries(text: str) -> str:
    """Redirect queries to the Jisho website."""
    return re.sub(r'"\?query=(.+?)&[^"]+"', r'"https://jisho.org/search/\1"', text)


def remove_all_tags(text: str) -> str:
    """Remove all HTML tags from the text."""
    return re.sub(r"<[^>]*>", "", text)


def remove_element(text: str, tag: str) -> str:
    """Remove the specified HTML element from the text."""
    return re.sub(rf"<{tag}[^>]*>.*?</{tag}>", "", text)


def remove_tags(text: str, tag_list: list[str], replacement: str = "") -> str:
    """Remove the specified HTML tags from the text."""
    for tag in tag_list:
        text = re.sub(rf"<{tag}>|<{tag} [^>]*>", replacement, text)
        text = re.sub(rf"</{tag}>", replacement, text)
    return text


def remove_all_attributes(text: str) -> str:
    """Remove all attributes from the text."""
    excluded_attributes = ["href"]
    excluded_attributes = "|".join(excluded_attributes)
    return re.sub(rf' (?!{excluded_attributes})[a-z\-]+="[^"]+"', "", text)


def remove_images(text: str) -> str:
    """Remove images from the text."""
    text = re.sub(r"<img[^>]*>", "", text)
    return re.sub(r"</img>", "", text)


def remove_queries(text: str) -> str:
    """Remove element with queries from the text."""
    return re.sub(r'<a[^>]*href="[^"]*query=[^"]*"[^>]*>.*?</a>', "", text)


def remove_empty_tags(text: str) -> str:
    """Remove empty tags from the text."""
    cleaned_text = re.sub(r"<[^/>]*></[^>]*>", "", text)
    while text != cleaned_text:
        text = cleaned_text
        cleaned_text = re.sub(r"<[^/>]*></[^>]*>", "", text)
    return re.sub(r"<[^/>]*></[^>]*>", "", text)


def remove_leading_spaces(text: str) -> str:
    """Remove leading spaces from the text."""
    return re.sub(r"(^|\n)( )+", r"\1", text)


def reduce_occurence(text: str, character: str) -> str:
    """Remove multiple occurrences of a character from the text."""
    return re.sub(rf"({character})+", r"\1", text)


def trim_newline(text: str) -> str:
    """Trim newlines at the beginning and end of the text."""
    if text.startswith("\n"):
        text = text[1:]
    if text.endswith("\n"):
        text = text[:-1]
    return text
