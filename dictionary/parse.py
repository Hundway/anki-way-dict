from typing import Union
from .utils import double_to_single_quotes, camel_to_dash


def parse_definitions(
    definitions: list[list[Union[str, dict, list]]], dict_title: str = ""
) -> str:
    """Parse definitions extracted from a `Dictionary` and return it as an html string."""
    title = f'<li data-dictionary="{dict_title}">' if dict_title else "<li>"
    text = "<ol>"
    for entry in definitions:
        text += title + parse_entry(entry) + "</li>"
    return text + "</ol>"


def parse_entry(entry: list[Union[str, dict, list]]) -> str:
    """Parse the entries of a `Dictionary` and return them as an html string."""
    if len(entry) == 1:
        return parse_content(entry[0])

    definitions = (f"<li>{parse_content(definition)}</li>" for definition in entry)
    return "<ul>" + "".join(definitions) + "</ul>"


def parse_content(content: Union[str, dict, list]) -> str:
    """Parse the content of an entry and return it as a string."""
    if isinstance(content, str):
        return content
    elif isinstance(content, dict):
        return parse_dict(content)
    elif isinstance(content, list):
        return "".join(parse_content(item) for item in content)
    raise TypeError(f"Invalid content type: {type(content)}")


def parse_dict(structure: dict) -> str:
    """Parse a dictionary containing HTML structure and return it as a string."""
    tag = structure.get("tag", "")
    content = parse_content(structure.get("content", ""))

    if not tag:
        return content

    attributes = parse_attributes(structure)
    return f"<{tag}{attributes}>{content}</{tag}>"


def parse_attributes(structure: dict) -> str:
    """Parse the attributes of a html element and return them as a string."""
    attributes = ""
    for key, value in structure.items():
        if key in ("content", "tag"):
            continue
        elif key == "style":
            attributes += parse_style(value)
        elif key == "data":
            attributes += parse_data(value)
        else:
            attributes += f' {key}="{value}"'
    return attributes


def parse_data(attributes: dict) -> str:
    """Parse the values of a data attribute and return it as a string."""
    text = ""
    for key, value in attributes.items():
        text += f' data-{key}="{value}"'
    return text


def parse_style(style: dict) -> str:
    """Parse a style attribute and return it as a string."""
    text = ""
    for key, value in style.items():
        if isinstance(value, str):
            if '"' in value:
                value = double_to_single_quotes(value)
            value = camel_to_dash(value)
        text += f"{camel_to_dash(key)}: {value};"
    return f' style="{text}"'
