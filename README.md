# Waydict: dictionary importer

![Release](https://img.shields.io/github/v/release/Hundway/anki-way-dict?include_prereleases)
![Latest Commit](https://img.shields.io/github/last-commit/Hundway/anki-way-dict)
[![Rate on AnkiWeb](https://glutanimate.com/logos/ankiweb-rate.svg)](https://ankiweb.net/shared/info/377012597)
![GitHub](https://img.shields.io/github/license/Hundway/anki-way-dict)

Waydict is an open-source, free [anki](https://apps.ankiweb.net/) add-on that lets you import your favorite dictionary and add its definitions to notes.

<div align="center">
  <img src="https://github.com/user-attachments/assets/55e6d836-09e3-42fa-8cea-ac2ac48ed8f0" style="width: 45%;">
</div>

## Usage
After installation, the add-on can be accessed in multiple ways.
Selecting any option will open a dialog to process all notes currently selected. 
First, you should set a dictionary and a note configuration; after pressing `Start`, notes will be updated.
To access the dialog, choose one of the following options on the browser menu:

- `定` button inside note editor.
- `Add definition` action in edit menu or right-click context menu.

| Note editor | Edit Menu | Context Menu |
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://github.com/user-attachments/assets/f618f907-357e-4fd9-a267-2d1a2aaff84c" style="width: 280px; height: 350px"> | <img src="https://github.com/user-attachments/assets/38644558-bd0a-4040-a29e-191ba0c1dcec" style="width: 350px; height: 350px;"> | <img src="https://github.com/user-attachments/assets/6b631119-e820-4ad9-baea-8b825e1a6064" style="width: 350px; height: 350px;">

### 1. Select a dictionary

At the top-right of the dialog, there's a `Browse` button that will let you select a *zip* file containing the dictionary entries.
To check if a dictionary was properly imported, use the `Preview` tab to search a word definition.

There are three text formats to choose from:
- `HTML-Full`: keep all HTML.
- `HTML-Brief`: keep only list elements, discard styles. 
- `Plain-Text`: format list elements to plain text.

<p align="center">
    <img src="https://github.com/user-attachments/assets/90150669-771e-49d2-ad62-02078670923d" style="width: 60%;">
</p>

> [!WARNING]
> Only dictionaries on [yomitan](https://github.com/yomidevs/yomitan) format are currently supported.
> To access a handful of those, please refer to yomitan [wiki](https://yomitan.wiki/dictionaries/).

### 2. Set note options

Given a selection of notes, definitions will only be added on those that match the given note configuration:

- `Note type`: target note type.
- `Source field`: field with the word to be searched.
- `Destination field`: field in which definitions will be added.
- `Overwrite destination`: overwrite destination even if it has content.

## Installation

### AnkiWeb
The easiest way to install Waydict is through [AnkiWeb](https://ankiweb.net/shared/info/377012597?cb=1739746670083) add-on code: `377012597`.

1. Open Anki > Tools > Add-ons > `Get Add-ons`.
2. Paste the code and hit `Ok`.

### Manual installation
1. Download *waydict.zip* file from the [latest release](https://github.com/Hundway/anki-way-dict/releases). 
2. Open Anki > Tools > Add-ons > `Install from file`.
3. Select and open the downloaded file.

## Contributing
Contributions are welcome! Please feel free to:
- Report [issues](https://github.com/Hundway/anki-way-dict/issues).
- Request a [feature](https://github.com/Hundway/anki-way-dict/issues).
- Send [pull requests](https://github.com/Hundway/anki-way-dict/pulls).
