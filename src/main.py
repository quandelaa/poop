from parse import parse
from organizer import Organizer 
from pathlib import Path
from config import LEGAL_ARGS, EXTENSIONS, EXT_COLORS, COLORS, TERMS
from rich.console import Console
from rich.layout import Layout

class Files:
    def __init__(self, path) -> None:
        self.console = Console()

        self.index_color = COLORS["index"]
        self.header_color = COLORS["header"]
        self.subheader_color = COLORS["subheader"]
        self.muted_color = COLORS["muted"]
        self.error_color = COLORS["error"]
        self.success_color = COLORS["success"]
        self.text_color = COLORS["text"]
        self.prompt_color = COLORS["prompt"] 

        self.startup_error = None

        try:
            self.files = [f for f in path.iterdir() if f.is_file()]
        except PermissionError as e:
            self.startup_error = e

        self.path = str(path)
        
    def question(self, args):
        options = dict()

        self.console.print(f"do [bold {self.prompt_color}]'poop -h'[/] for more help\n")

        for arg in args:
            term = TERMS.get(arg)

            if not term:
                continue

            if term not in LEGAL_ARGS:
                continue

            color = EXT_COLORS.get(term)

            while options.get(term) not in (False, True):
                e = "directory" if term != "all" else "directories"
                answer = self.console.input(f"organize [bold {color}]{term}[/] files in to their respective {e} (y for yes, blank for no): ").lower() 

                options[term] = False if answer == "" else True if answer == "y" else answer

                if term == "all" and options[term]:
                    return options #gonna js return a dictionary with all flags: true

        if all(value == False for value in options.values()):
            self.console.print(f"\n[bold {self.error_color}]why didn't you pick anything?", end="")
            return

        return options

    def display(self) -> None:
        self.console.print(f"\ndirectory: [bold {self.subheader_color}]{self.path}\n")

        for i, file in enumerate(self.files):
            file_name = file.stem
            file_ext = file.suffix

            category = EXTENSIONS.get(file_ext, "misc")
            color = EXT_COLORS.get(category)

            self.console.print(f"[{self.index_color}]{i+1}.[/] [{self.text_color}]{file_name}[/][bold {color}]{file_ext}")

def setup(console):
    args = parse()

    if args.path:
        path = Path(args.path).resolve()
    else:
        path = Path(console.input(f"[{COLORS.get("prompt")}]?[/] path to folder: ").strip()).resolve()

    if not path.is_dir():
        while not path.is_dir():
            console.print(f"[{COLORS.get('error')}]{path}[/], is not a path to a directory")
            path = Path(console.input(f"[{COLORS.get("prompt")}]?[/] path to folder: ").strip()).resolve()

    args_ = {arg: val for arg, val in vars(args).items() if arg != "path"}

    return path, args_

def main():
    console = Console()
    path, args = setup(console)

    file_store = Files(path)

    if file_store.startup_error is not None:
        return file_store.startup_error

    if sum(1 for value in args.values() if value == False or value == None) == 14:
        options = file_store.question(list(args))
        
        if options is None:
            return
    else:
        options = args
    
    print(options)
    organizer = Organizer(options, file_store.path)

    organizer.mkdirs()

    file_store.display()






