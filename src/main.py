from pydoc import text
from parse import parse
from pathlib import Path
from config import EXTENSIONS, EXT_COLORS, COLORS, TERMS
from rich.console import Console  # pyright: ignore[reportMissingImports]
from rich.panel import Panel
from rich.layout import Layout

class Files:
    def __init__(self, path) -> None:
        self.files = [f for f in path.iterdir() if f.is_file()]
        self.path = str(path)

        self.index_color = COLORS["index"]
        self.header_color = COLORS["header"]
        self.subheader_color = COLORS["subheader"]
        self.muted_color = COLORS["muted"]
        self.error_color = COLORS["error"]
        self.success_color = COLORS["success"]
        self.text_color = COLORS["text"]
        self.prompt_color = COLORS["prompt"] 
        
    def question(self, console, args):
        options = dict()

        for arg in args:
            term = TERMS.get(arg)
            
            if not term:
                continue

            color = EXT_COLORS.get(term)

            while options.get(term) != "y" and options.get(term) != "":
                options[term] = console.input(f"[{self.text_color}]organize [{color}]{term}[/] files in a seperate directory (y for yes, blank for no): ").lower()

        console.print()

    def display(self, console):
        console.print(f"directory: [bold {self.subheader_color}]{self.path}\n")

        for i, file in enumerate(self.files):
            file_name = file.stem
            file_ext = file.suffix

            category = EXTENSIONS.get(file_ext, "misc")
            color = EXT_COLORS.get(category)

            console.print(f"[{self.index_color}]{i+1}.[/] [{self.text_color}]{file_name}[/][{color}]{file_ext}[/]")

def setup(console):
    args = parse()

    if args.path:
        path = Path(args.path).resolve()
    else:
        path = Path(console.input(f"[{COLORS.get("prompt")}]?[/] path to folder: ").strip()).resolve()

    if not path.is_dir():
        while not path.is_dir():
            console.print(f"[{COLORS.get("error")}]{path}[/], is not a path to a directory")
            path = Path(console.input(f"[{COLORS.get("prompt")}]?[/] path to folder: ").strip()).resolve()

    args_ = {arg: val for arg, val in vars(args).items() if arg != "path"}

    return path, args_

def main():
    console = Console()
    path, args = setup(console)

    file_store = Files(path)

    if sum(1 for value in args.values() if value == False or value == None) == 14:
        file_store.question(console, list(args))

    file_store.display(console)
