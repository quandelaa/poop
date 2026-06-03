from .parse import parse
from .organizer import Organizer 
from pathlib import Path
from .config import LEGAL_ARGS, EXTENSIONS, EXT_COLORS, COLORS
from rich.console import Console
from rich.layout import Layout

class Files:
    def __init__(self, path) -> None:
        self.files = []

        for f in path.iterdir():
            try:
                if f.is_file():
                    self.files.append(f)
            except PermissionError:
                continue

        self.console = Console()

        self.header_color = COLORS["header"]
        self.subheader_color = COLORS["subheader"]
        
        self.index_color = COLORS["index"]
        self.muted_color = COLORS["muted"]

        self.error_color = COLORS["error"]
        self.success_color = COLORS["success"]
        
        self.text_color = COLORS["text"]
        self.prompt_color = COLORS["prompt"] 

        self.path = str(path)
        
    def question(self, args: list):
        options = dict()

        self.console.print(f"do [bold {self.prompt_color}]'poop -h'[/] for usage\n")

        for arg in args:
            if arg not in LEGAL_ARGS:
                continue

            color = EXT_COLORS.get(arg)

            while options.get(arg) not in (False, True):
                e = "directory" if arg != "all" else "directories"
                answer = self.console.input(f"organize [bold {color}]{arg}[/] files into their respective {e} (y/N): ").lower() 

                options[arg] = False if answer == "" else True if answer == "y" else answer

                if arg == "all" and options[arg] is True:
                    return {opt: True for opt in EXTENSIONS.values()} 
        
        if all(value == False for value in options.values()):
            self.console.print(f"\n[bold {self.error_color}]why don't you want to organize anything?", end="")
            return

        print()
        return options

    def display(self, preview):
        self.console.print(f"\ndirectory: [bold {self.subheader_color}]{self.path}\n")

        for i, file in enumerate(self.files):
            file_name = file.stem
            file_ext = file.suffix

            category = EXTENSIONS.get(file_ext.lower(), "misc")
            color = EXT_COLORS.get(category)

            self.console.print(f"[{self.index_color}]{i+1}.[/] [{self.text_color}]{file_name}[/][bold {color}]{file_ext}")

    @classmethod
    def clean_options(cls, options: dict):
        all_ = options.get("all")
        specs = options.get("spec")

        if all_ is not None and all_ is True:
            return {opt: True for opt in set(EXTENSIONS.values())}

        if specs is not None:
            return {"spec": [(spec if spec[0] == "." else f".{spec}")for spec in specs]}

        return {opt: val for opt, val in options.items() if val not in (False, None)}

def setup(console):
    args = parse()
    args_ = {arg: val for arg, val in vars(args).items() if arg != "path"}

    if args.path:
        if len(args.path) == 2 and args.path[1] == ":":
            path = Path(args.path)

        path = Path(args.path).resolve()
    else:
        raw_path = console.input(f"[{COLORS.get('prompt')}]?[/] path to directory: ").strip()
        if len(raw_path) == 2 and raw_path[1] == ":":
            path = Path(raw_path)

        path = Path(raw_path).resolve()

    if not path.is_dir():
        while not path.is_dir():
            console.print(f"[{COLORS.get('error')}]{path}[/], is not the path to a known directory")
            raw_path = console.input(f"[{COLORS.get('prompt')}]?[/] path to directory: ").strip()
            
            if len(raw_path) == 2 and raw_path[1] == ":":
                path = Path(raw_path)

            path = Path(raw_path).resolve()

    return path, args_

def main():
    console = Console()
    path, args = setup(console)

    file_store = Files(path)

    if not any(val for val in args.values()):
        options = file_store.question(list(args))
        
        if options is None:
            return
    else:
        options = args
    
    new_opts = file_store.clean_options(options)

    organizer = Organizer(new_opts, file_store.path, file_store.files)
    new_dir_paths = organizer.directory_paths()

    for path in new_dir_paths:
        print(path, new_dir_paths.get(path))

    file_store.display(0)
