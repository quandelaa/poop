from pathlib import Path
import shutil

from .parse import parse
from .config import EXTENSIONS, COLORS

class Utility():
    @classmethod
    def clean_options(cls, options: dict, known_types) -> dict:
        all_ = options.get("all")
        specs = options.get("spec")

        if all_ is not None and all_ is True:
            return {opt: True for opt in set(EXTENSIONS.values()) if opt in known_types}

        if specs is not None:
            return {"spec": {"name": specs[0], "exts": [(spec if spec[0] == "." else f".{spec}") for spec in specs[1:]]}}

        return {opt: val for opt, val in options.items() if val not in (False, None) and opt in known_types}

    @classmethod
    def setup(cls, console):
        args = parse()
        args_ = {arg: val for arg, val in vars(args).items() if arg != "path"}

        if args.path:
            path = Path(args.path).resolve()
        else:
            raw_path = console.input(
                f"[bold {COLORS.get('prompt')}]?[/] [{COLORS.get('muted')}]path to directory:[/] "
            ).strip()

            path = Path(raw_path).resolve()
            console.print()

        if not path.is_dir():
            while not path.is_dir():
                console.print(
                    f"[{COLORS.get('error')}]![/] "
                    f"[bold {COLORS.get('text')}]{path}[/] "
                    f"[{COLORS.get('error')}]is not a valid directory[/]"
                )

                raw_path = console.input(
                    f"[bold {COLORS.get('prompt')}]?[/] [{COLORS.get('muted')}]path to directory:[/] "
                ).strip()
                
                path = Path(raw_path).resolve()
                console.print()

        return path, args_

    @classmethod
    def get_options(cls, question, args):
        if not any(val for val in args.values()):
            options = question(list(args))
        else:
            options = args

        return options

    @classmethod
    def acceptance(cls, console):
        accept = None

        console.print()
        while accept is not False and accept is not True:
            accept = console.input(
                    f"[bold {COLORS.get('prompt')}]?[/] [{COLORS.get('muted')}]would you like to accept the changes [bold](y/N to abort): "
            ).strip().lower()

            accept = True if accept == "y" else False if accept == "n" or accept.isspace() or accept == "" else accept

        return accept
