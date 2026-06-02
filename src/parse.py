import argparse

def parse():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--path", help="the path to the directory you want to organize")

    parser.add_argument("--all", help="all file types organized into seperate directories based on their category", action="store_true")
    parser.add_argument("--spec", help="specify file types to be organized into one seperate directory", nargs="+", metavar="TYPE")

    parser.add_argument("--image", help="organize image files into a seperate directory", metavar="NAME")
    parser.add_argument("--video", help="organize video files into a seperate directory", metavar="NAME")
    parser.add_argument("--audio", help="organize audio files into a seperate directory", metavar="NAME")
    parser.add_argument("--document", help="organize documents into a seperate directory", metavar="NAME")
    parser.add_argument("--spreadsheet", help="organize spreadsheets into a seperate directory", metavar="NAME")
    parser.add_argument("--archive", help="organize archive files into a seperate directory", metavar="NAME")
    parser.add_argument("--exe", help="organize executable files into a seperate directory", metavar="NAME")
    parser.add_argument("--ebook", help="organize ebook files into a seperate directory", metavar="NAME")
    parser.add_argument("--font", help="organize font files into a seperate directory", metavar="NAME")
    parser.add_argument("--subtitle", help="organize subtitle files into a seperate directory", metavar="NAME")
    parser.add_argument("--3d", help="organize 3d files into a seperate directory", metavar="NAME")
    parser.add_argument("--map", help="organize map/gis files into a seperate directory", metavar="NAME") 

    args = parser.parse_args()

    return args
