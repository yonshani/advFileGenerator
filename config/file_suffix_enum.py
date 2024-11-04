from enum import Enum

from adodbapi.process_connect_string import process


class FileSuffixEnum(Enum):



    lowercase_text = ".txt"
    python = ".py"
    batch = ".bat"
    csv = ".csv"
    c_sharp = ".cs"
    json = ".json"
    pem = ".pem"
    uppercase_text = ".TXT"


    def __init__(self,suffix):
        self.suffix = suffix

class FileSuffixHandler:
    @property
    def return_enum_list(self):
        """Return a list of all file suffixes."""
        return [suffix.value for suffix in FileSuffixEnum]