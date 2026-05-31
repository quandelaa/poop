import argparse

def parse():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--path", help="the path to the folder you wanna organize")

    parser.add_argument("--all", help="all file types organized into seperate folders based on their category", action="store_true")
    parser.add_argument("--spec", help="specify file types to be organized into one seperate folder", nargs="+", metavar="TYPE")

    parser.add_argument("--img", help="organize image files into a seperate folder", action="store_true")
    parser.add_argument("--vid", help="organize video files into a seperate folder", action="store_true")
    parser.add_argument("--audio", help="organize audio files into a seperate folder", action="store_true")
    parser.add_argument("--doc", help="organize documents into a seperate folder", action="store_true")
    parser.add_argument("--sheet", help="organize spreadsheets into a seperate folder", action="store_true")
    parser.add_argument("--zip", help="organize archive files into a seperate folder", action="store_true")
    parser.add_argument("--exe", help="organize executable files into a seperate folder", action="store_true")
    parser.add_argument("--ebook", help="organize ebook files into a seperate folder", action="store_true")
    parser.add_argument("--font", help="organize font files into a seperate folder", action="store_true")
    parser.add_argument("--sub", help="organize subtitle files into a seperate folder", action="store_true")
    parser.add_argument("--3d", help="organize 3d files into a seperate folder", action="store_true")
    parser.add_argument("--map", help="organize map/gis files into a seperate folder", action="store_true") 

    args = parser.parse_args()

    return args
