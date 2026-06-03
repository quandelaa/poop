from pathlib import Path
from .config import COLORS, EXT_COLORS 
from rich.console import Console

class Organizer:
    def __init__(self, options: dict, path: str, files: list) -> None:
        self.options = options.copy()
        self.console = Console()

        self.path = Path(path)
        self.files = files.copy() 
  
        self.prompt_color = COLORS.get("prompt")

    def directory_paths(self):
        dir_paths = {}
        specs = self.options.get("spec")
        
        if specs is not None:
            name = self.console.input(f"name of the new directory to store [bold {self.prompt_color}]{", ".join(specs)}[/] files: ")
            if name.isspace() or name == "":
                name = "directory_made_by_poop"

            dir_paths["spec"] = self.path.joinpath(name)
            return dir_paths

        name_choice = None
        while name_choice not in (False, True):
            name_choice = self.console.input(f"name new directories after their own respective category name (y/N): ")
            name_choice = True if name_choice == "y" else False if name_choice == "" else name_choice

        if not name_choice:
            print()

        for opt in self.options:
            val = self.options.get(opt)

            if val is True:
                color = EXT_COLORS.get(opt)
                if not name_choice:
                    name = self.console.input(f"name of the new directory to store [bold {color}]{opt.replace("_", " ")}[/] files: ").replace(" ", "_")
                
                    if name.isspace() or name == "":
                        name = opt
                else:
                    name = f"{opt}s"

                dir_paths[opt] = (self.path.joinpath(name))

        return dir_paths

    def mkdirs(self):
        pass
