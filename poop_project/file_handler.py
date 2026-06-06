from pathlib import Path

from .config import LEGAL_ARGS, EXTENSIONS, EXT_COLORS, COLORS

from rich.console import Console
from rich.tree import Tree
from rich.padding import Padding

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

        self.console.print(f"[{self.muted_color}]----------------------------------------------------")
        self.console.print(f"[{self.muted_color}]run [{self.subheader_color}]'poop -h'[/] for usage[/]\n")

        for arg in args:
            if arg not in LEGAL_ARGS:
                continue

            color = EXT_COLORS[arg]

            while options.get(arg) not in (False, True):
                e = "directory" if arg != "all" else "directories"

                answer = self.console.input(
                    f"[{self.prompt_color}]>[/] [{self.muted_color}]organize[/] "
                    f"[bold {color}]{arg}[/] "
                    f"[{self.muted_color}]files into their respective {e} (y/N):[/] "
                ).lower()

                options[arg] = False if answer == "" or answer == "n" else True if answer == "y" else answer

                if arg == "all" and options[arg] is True:
                    self.console.print()
                    return {opt: True for opt in EXTENSIONS.values()} 
        
        if all(value == False for value in options.values()):
            self.console.print(f"\n[{self.muted_color}]why don't you want to organize anything? -- exiting[/]", end="")
            return
 
        self.console.print()
        return options

    def display(self, preview) -> None:
        self.console.print(f"\n[{self.muted_color}]directory:[/] [{self.header_color}]{self.path}\n")

        for i, file in enumerate(preview):
            is_dir = isinstance(file, list)
            if is_dir:
                sub_files = file[1]
                file = file[0]
            else:
                sub_files = [] # needed for pleasing pyright
                
            file_name = file.stem
            file_ext = file.suffix

            category = EXTENSIONS.get(file_ext.lower(), "misc")
            color = EXT_COLORS.get(category)

            if is_dir:
                dir_tree = Tree(f"[{self.index_color}]{i+1}[/][{self.muted_color}].[/] "
                            f"[{self.text_color}]{file_name}[/]"
                            f"[{color}]{file_ext}[/]", style=self.index_color, guide_style=self.index_color)

                for j, sub_file in enumerate(sub_files):
                    sub_file_name = sub_file.stem
                    sub_file_ext = sub_file.suffix

                    sub_category = EXTENSIONS.get(sub_file_ext.lower(), "misc")
                    sub_color = EXT_COLORS.get(sub_category)

                    dir_tree.add(f"[{self.index_color}]{''}[/][{self.muted_color}].[/] "
                            f"[{self.text_color}]{sub_file_name}[/]"
                            f"[{sub_color}]{sub_file_ext}[/]")

                self.console.print(Padding.indent(dir_tree, 1))
                continue

            self.console.print(
                f"[{self.index_color}]{i+1:>3}[/][{self.muted_color}].[/] "
                f"[{self.text_color}]{file_name}[/]"
                f"[{color}]{file_ext}[/]"
            )

    def types_in_dir(self):
        types = set()

        for file in self.files:
            sfx = Path(file).suffix
            category = EXTENSIONS.get(sfx, "misc")

            types.add(category)

        return types

