"""
    This project will collects windows assets and sort them into a specific
    directory.

    The default directory will be Desktop/Assets.
"""

from os import mkdir
from os.path import isdir, expandvars

from src.image import get_assets


def main(path=r'%userprofile%\Desktop\Assets'):
    dst_dir = expandvars(path)
    if not isdir(dst_dir):
        mkdir(dst_dir)

    new_assets = get_assets(dst_dir)

    print("New assets :")
    for element in new_assets:
        print(element)


if __name__ == "__main__":
    main()
