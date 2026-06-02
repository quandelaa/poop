from pathlib import Path
from config import EXT_COLORS 
from rich.console import Console

class Organizer:
    def __init__(self, options: dict, path, files: list) -> None:
        self.options = options.copy()
        self.console = Console()
        self.path = Path(path)
        self.files = files.copy() 

    def mkdirs(self):
        paths = []
