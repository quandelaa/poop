from pathlib import Path
from .config import COLORS, EXT_COLORS, EXTENSIONS 
from rich.console import Console

class Organizer:
    def __init__(self, options: dict, path: str, files: list) -> None:
        self.options = options.copy()
        self.console = Console()

        self.path = Path(path)
        self.files = files.copy()
        
        self.dirs = dict()
        
        self.prompt_color = COLORS.get("prompt")

    def make_dirs(self):
        specs = self.options.get("spec")
        
        if specs is not None:
            self.dirs["spec"] = self.path.joinpath(specs["name"])
            return

        name_choice = None
        if all(val is True for val in self.options.values()):
            while name_choice not in (False, True):
                name_choice = self.console.input(f"name new directories after their own respective category name (y/N): ")
                name_choice = True if name_choice == "y" else False if name_choice == "" else name_choice

        if name_choice is True:
            print()

        for opt in self.options:
            val = self.options.get(opt)

            if val is True:
                color = EXT_COLORS.get(opt)
                if not name_choice:
                    name = self.console.input(f"name of the new directory to store [bold {color}]{opt.replace("_", " ")}[/] files: ").replace(" ", "_")
                
                    if name.isspace() or name == "":
                        name = f"{opt}s"
                else:
                    name = f"{opt}s"

                self.dirs[opt] = self.path.joinpath(name)
            else:
                self.dirs[opt] = self.path.joinpath(str(val))

    def organize(self):
        for file in self.files:
            ext = Path(file).suffix

            print(file)
            print(EXTENSIONS.get(ext.lower(), "misc"))
            


