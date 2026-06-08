from .organizer import Organizer 
from .utils import Utility
from .file_handler import Files

from rich.console import Console

def main():
    console = Console()
    path, args = Utility.setup(console)

    file_handler = Files(path)

    options = Utility.get_options(file_handler.question, args)
    if options is None:
        return
    
    known_types = file_handler.types_in_dir()
    new_opts = Utility.clean_options(options, known_types)

    organizer = Organizer(new_opts, file_handler.path, file_handler.files)
    organizer.make_dirs()

    new_files = organizer.organize()
    file_handler.display(new_files) 
    
    is_accept = Utility.acceptance(console)
    if is_accept:
        file_handler.move_files(new_files)
