from pathlib import Path
from config import TERMS, EXT_COLORS 
from rich.console import Console

class Organizer:
    def __init__(self, options: dict, path) -> None:
        self.options = options.copy()
        self.console = Console()
        self.path = Path(path)

    def mkdirs(self):
        paths = []

        for opt in self.options:
            if not self.options[opt]:
                continue
            
            print(opt)
            term = TERMS.get(opt)
            color = EXT_COLORS.get(term)
            name = self.console.input(f"name for the new [bold {color}]{term}[/] directory: ")

            if name.isspace():
                name = opt

            path = Path(self.path.joinpath(name))
            print(path)
            # path.mkdir(exist_ok=True)

            print(name)

            paths.append(path)
