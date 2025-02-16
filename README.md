# Waydict: dictionary importer
Waydict is an open-source, free [anki](https://apps.ankiweb.net/) add-on that lets you import your favorite term dictionary and add its definitions to notes.

<p align="center">
  <img src="https://github.com/user-attachments/assets/93597321-2f43-48c2-b495-aa19b01bf543" style="width: 25vw;">
</p>

## Usage
After installation, the add-on can be accessed in multiple ways.
Selecting any option will open a dialog to process all notes currently selected. 
First you should set a dictionary and a note configuration, after pressing `Start` notes will be updated.
To access the dialog, choose one of the following options on browser menu:

- `定` button inside note editor.
- `Add definition` action in edit menu or right-click context menu.

### 1. Select a dictionary

At top-right of the dialog there's a `Browse` button that will let you select a *zip* file containing the dictionary entries.
To check if a dictionary was properly imported, use the `Preview` tab to search a word definition.

There are three text formats to choose from:
- `HTML-Full`: keep all html.
- `HTML-Brief`: keep only list elements, discard styles. 
- `Plain-Text`: format list elements to plain text.

<p align="center">
    <img src="https://github.com/user-attachments/assets/90150669-771e-49d2-ad62-02078670923d" style="width: 23vw"></img>
</p>

> Only dictionaries on [yomitan](https://github.com/yomidevs/yomitan) format are currently supported.
> To access a handful of those, please refer to [yomitan wiki](https://yomitan.wiki/dictionaries/).

### 2. Set note options

Given a selection of notes, definitions will only be added on those that matches the given note configuration:

- `Note type`: note type of the target.
- `Source field`: field that contains the word to be searched.
- `Destination field`: field in which definitions will be added.
- `Overwrite destination`: overwrite destination even if has content.

## Installation

### AnkiWeb
The easiest way to install Waydict is through [AnkiWeb](https://ankiweb.net/shared/info/377012597?cb=1739746670083) addon code: `377012597`.

- 1. Open Anki > Tools > Add-ons > `Get Add-ons...`.
- 2. Paste the code and hit `Ok`.

### Manual installation
- 1. Download the *Waydict.zip* file from the latest release. 
- 2. Open Anki > Tools > Add-ons > `Install from file...`.
- 3. Select and open the downloaded file.

## Contributing
Contributions are welcome! Please feel free to:
- Report [issues](https://github.com/Hundway/anki-way-dict/issues).
- Request a [feature](https://github.com/Hundway/anki-way-dict/issues).
- Send [pull requests](https://github.com/Hundway/anki-way-dict/pulls).
