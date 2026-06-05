from pathlib import Path
from sys import exception
from types import new_class
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
        self.muted_color = COLORS.get("muted")

    def make_dirs(self):
        specs = self.options.get("spec")
        
        if specs is not None:
            self.dirs["specs"] = (self.path.joinpath(specs["name"]), specs["exts"])
            return

        name_choice = None
        if all(val is True for val in self.options.values()):
            while name_choice not in (False, True):
                name_choice = self.console.input(
                    f"[{self.prompt_color}]>[/] "
                    f"[{self.muted_color}]name directories after their category (y/N):[/] "
                )

                name_choice = True if name_choice == "y" else False if name_choice == "" or name_choice == "n" else name_choice

        for opt in self.options:
            val = self.options.get(opt)

            if val is True:
                color = EXT_COLORS.get(opt)
                if not name_choice:
                    name = None
                    has_same = self.path.joinpath(str(name)) in self.dirs.values()

                    while has_same or name is None: 
                        name = self.console.input(
                            f"[{self.prompt_color}]>[/] "
                            f"[{self.muted_color}]directory name for[/] "
                            f"[bold {color}]{opt.replace('_', ' ')}[/] "
                            f"[{self.muted_color}]files:[/] "
                        ).replace(" ", "_")
                    
                        has_same = self.path.joinpath(name) in self.dirs.values()

                    if name.isspace() or name == "":
                        name = f"{opt}s"
                else:
                    name = f"{opt}s"

                self.dirs[opt] = self.path.joinpath(name)
            else:
                self.dirs[opt] = self.path.joinpath(str(val))

    def organize(self):
        new_files = self.files.copy()
        specs = self.dirs.get("specs")

        if specs is None:      
            for file_type in self.dirs:
                new_files.append([self.dirs[file_type], list()])
        else:
            new_files.append([self.dirs["specs"][0], list()])

        for file in self.files:
            sfx = file.suffix.lower()
            file_type = EXTENSIONS.get(sfx, "misc")

            if specs is None:
                raw_path = self.dirs.get(file_type)
            else:
                if sfx in specs[1]:
                    raw_path = specs[0]
                else:
                    raw_path = None

            if raw_path is None:
                continue

            for item in new_files:
                if not isinstance(item, list) or not item[0] == raw_path:
                    continue

                item[1].append(file)
                new_files.remove(file)

        return new_files
