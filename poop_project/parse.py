import argparse

def parse():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("-p", "--path", help="path to the directory to organize")

    parser.add_argument("-a", "--all", help="organize all supported file types into separate directories named by category", action="store_true")
    parser.add_argument("-s", "--spec", help="move specific file extensions into a directory named DIR in PATH", nargs="+", metavar=("DIR", ".EXT"))

    parser.add_argument("--image", help="organize supported image files into a directory named DIR in PATH", metavar="DIR")
    parser.add_argument("--video", help="organize supported video files into a directory named DIR in PATH", metavar="DIR")
    parser.add_argument("--audio", help="organize supported audio files into a directory named DIR in PATH", metavar="DIR")

    parser.add_argument("--document", help="organize supported document files into a directory named DIR in PATH", metavar="DIR")
    parser.add_argument("--spreadsheet", help="organize supported spreadsheet files into a directory named DIR in PATH", metavar="DIR")
    
    parser.add_argument("--archive", help="organize supported archive files into a directory named DIR in PATH", metavar="DIR")
    parser.add_argument("--executable", help="organize supported executable files into a directory named DIR in PATH", metavar="DIR")
    
    parser.add_argument("--ebook", help="organize supported ebook files into a directory named DIR in PATH", metavar="DIR")
    parser.add_argument("--font", help="organize supported font files into a directory named DIR in PATH", metavar="DIR")
    parser.add_argument("--subtitle", help="organize supported image files into a directory named DIR in PATH", metavar="DIR")
    
    parser.add_argument("--3d", help="organize supported 3d model files into a directory named DIR in PATH", metavar="DIR")
    parser.add_argument("--disk_image", help="organize supported disk image files into a directory named DIR in PATH", metavar="DIR") 
    
    parser.add_argument("--code", help="organize supported code files into a directory named DIR in PATH", metavar="DIR") 
    parser.add_argument("--backup", help="organize supported backup files into a directory named DIR in PATH", metavar="DIR") 
    parser.add_argument("--data", help="organize supported data files into a directory named DIR in PATH", metavar="DIR") 

    parser.add_argument("--misc", help="organize supported miscellaneous files into a directory named DIR in PATH", metavar="DIR") 

    args = parser.parse_args()

    return args
