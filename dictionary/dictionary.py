import orjson
import os
from collections import defaultdict
from zipfile import ZipFile
from .parse import parse_definitions
from .format import format_definitions


class Dictionary:
    def __init__(self, path: str):
        self.path = path
        self.title = self.fetch_title(path)
        self.version = self.fetch_version(path)
        self.dictionary = self._import_dictionary(path)

    def find_definition(self, word: str, text_format: str = "HTML-Full") -> str:
        """Fetch definitions for a given word."""
        if not word:
            return ""

        entries = self.dictionary[word.lower()]

        if not entries:
            return ""

        entries = self._filter_entries(entries)
        entries = self._get_glossaries(entries)
        definitions = parse_definitions(entries, self.title)
        definitions = format_definitions(definitions, text_format)

        return definitions

    @staticmethod
    def fetch_title(path: str) -> str:
        """Get the title of the dictionary from the given `path`."""
        with ZipFile(path, "r") as zip_file:
            with zip_file.open("index.json") as index:
                title = orjson.loads(index.read())["title"]
        return title

    @staticmethod
    def fetch_version(path: str) -> str:
        """Get the version of the dictionary entries in the given `path`."""
        with ZipFile(path, "r") as zip_file:
            with zip_file.open("index.json") as index:
                version = orjson.loads(index.read())["format"]
        return version

    @staticmethod
    def validate_file(path: str) -> bool:
        """Verify if `path` has a valid dictionary file.
        It must be a zip with an index and term bank json files."""
        if not os.path.isfile(path):
            return False
        if not path.endswith(".zip"):
            return False
        with ZipFile(path, "r") as zip_file:
            if "index.json" not in zip_file.namelist():
                return False
            if not any(f.lower().startswith("term_bank") for f in zip_file.namelist()):
                return False
        return True

    def _import_dictionary(self, path: str) -> dict[str:list]:
        """Import all term banks from the given `path` and return a DataFrame."""
        with ZipFile(path, "r") as zip_file:
            dictionary = []
            for file in self._list_term_banks(zip_file):
                dictionary.extend(orjson.loads(zip_file.read(file)))
        return self._build_database(dictionary)

    def _build_database(self, dictionary: list[list]) -> dict[str:list]:
        """Build a database of entries from the given `dictionary` list."""
        database = defaultdict(list)
        for entry in dictionary:
            database[entry[0].lower()].append(entry)
            database[entry[1].lower()].append(entry)
        return database

    def _list_term_banks(self, zip_file: ZipFile) -> list[str]:
        """Get a list of all term bank files in a given `zip_file`."""
        term_bank_files = [
            file_name
            for file_name in zip_file.namelist()
            if file_name.lower().startswith("term_bank")
        ]
        return term_bank_files

    def _filter_entries(self, entries: list) -> list:
        """Filter the most relevant entries."""
        reading = self._max_score_reading(entries)
        entries = filter(lambda entry: entry[1] == reading, entries)
        return sorted(entries, key=lambda entry: entry[4], reverse=True)

    def _max_score_reading(self, entries: list) -> str:
        """Get the reading with the highest score."""
        scores = [entry[4] for entry in entries]
        return entries[scores.index(max(scores))][1]

    def _get_glossaries(self, entries: list) -> list:
        """Get the glossary from the entries."""
        if self.version == 1:
            term_bank_reader = self._read_term_bank_entry_v1
        elif self.version == 3:
            term_bank_reader = self._reader_term_bank_entry_v3
        return [term_bank_reader(entry)[5] for entry in entries]

    def _read_term_bank_entry_v1(self, entry: list) -> list:
        """Read a term bank entry from version 1."""
        term, reading, def_tags, rules, score = entry[:5]
        glossary = entry[5:]
        reading = reading if reading else term
        return [term, reading, def_tags, rules, score, glossary]

    def _reader_term_bank_entry_v3(self, entry: list) -> list:
        """Read a term bank entry from version 3."""
        term, reading, def_tags, rules, score, glossary, sequence, term_tags = entry
        reading = reading if reading else term
        return [term, reading, def_tags, rules, score, glossary, sequence, term_tags]
