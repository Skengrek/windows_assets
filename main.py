from os.path import isdir

from src.image import get_assets


def main():
    destination_folder = r'C:\Users\arman\Desktop\Assets'
    if not isdir(destination_folder):
        print('The directory you gave is not a valid one.')
        return None

    new_assets = get_assets(destination_folder)


if __name__ == "__main__":
    main()
