from parse import parse
from pathlib import Path
from config import EXTENSIONS, EXT_COLORS, COLORS
from rich.console import Console  # pyright: ignore[reportMissingImports]

class Organizer:
    def __init__(self, files: list) -> None:
       self.files = files.copy()

    def display(self, console):
        for i, file in enumerate(self.files):
            file_name = file.name.replace(file.suffix, "")
            file_ext = file.suffix

            category = EXTENSIONS.get(file_ext, "misc")
            color = EXT_COLORS.get(category)

            console.print(f"[{COLORS.get("subheader")}]{i+1}.[/] {file_name}[{color}]{file_ext}[/]")

def setup(console):
    args = parse()

    if args.path:
        path = Path(args.path)
    else:
        path = Path(console.input("[grey66]?[/] path to folder: ").strip())
 
    if not path.is_dir():
        while not path.is_dir():
            console.print(f"[red]{path}[/], is not a path to a directory")
            path = Path(console.input("[grey66]?[/] path to folder: ").strip())   

    return path, args

def main():
    console = Console()
    path, args = setup(console)

    files = [f for f in path.iterdir() if f.is_file()]

    organizer = Organizer(files)

    organizer.display(console)
