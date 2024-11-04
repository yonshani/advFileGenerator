from enum import Enum

class FileExtensionEnum(Enum):



    lowercase_text = ".txt"
    python = ".py"
    batch = ".bat"
    csv = ".csv"
    c_sharp = ".cs"
    json = ".json"
    pem = ".pem"
    uppercase_text = ".TXT"
    doc =".docx"


    def __init__(self,suffix):
        self.suffix = suffix

class FileExtensionHandler:
    @property
    def return_enum_list(self):
        """Return a list of all file suffixes."""
        return [suffix.value for suffix in FileExtensionEnum]