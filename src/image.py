"""

"""

from os import listdir, path, sep, mkdir, remove
from os.path import isfile, join, getsize, isdir
from shutil import copy2, move

from PIL import Image


def get_assets(dst_dir):
    """Get windows assets and copy them to a specific folder"""
    path_assets = path.expandvars(
        r'%LOCALAPPDATA%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets')

    # ? get all files from the assets folder
    tmp_assets = [f
                  for f in listdir(path_assets)
                  if isfile(join(path_assets, f))
                  ]

    new_assets = []

    # ? check which assets have already been collected
    log_file = dst_dir + sep + 'log.txt'
    old_list = []

    if isfile(log_file):
        old_list = get_collected_assets(log_file)

    else:
        # ? create the file
        f = open(log_file, "w+")
        f.close()

    for asset in tmp_assets:
        if asset not in old_list:
            # ? In order to get rid of logos that are in the same folder
            new_assets.append(asset)
            src = join(path_assets, asset)
            dst = dst_dir + '/' + asset + '.png'
            if not isfile(dst):
                # ? assets has not been collected yet
                copy2(src, dst)

    fill_log_file(log_file, new_assets)
    sort_assets(dst_dir)
    return new_assets


def get_collected_assets(file_name):
    """
        This function read the log file telling which one it already have
        collected
    """
    f = open(file_name, "r")
    old_assets = []
    for element in f:
        old_assets.append(element.strip('\n'))

    return old_assets


def fill_log_file(file_name, new_assets):
    """
        Fill the log file with assets collected
    :param file_name: the name of the log file
    :param new_assets: A list of assets collected
    :return: None
    """
    f = open(file_name, "a")

    for asset in new_assets:
        tmp_str = str(asset)
        f.write(tmp_str)

        # ? change line
        f.write('\n')


def sort_assets(path_dir='TEMP'):
    """
        Sort the image by their size :
            1920*1080 => wallpaper
            300*300 => logo
            Other => others

    :param path_dir: the path to the dir where assets will be saved.
    :return:
    """

    if not isdir(join(path_dir, 'wallpaper')):
        # ? Create the wallpaper directory of it does not exist
        mkdir(join(path_dir, 'wallpaper'))

    if not isdir(join(path_dir, 'wallpaper_vert')):
        # ? Create the wallpaper_vert directory of it does not exist
        mkdir(join(path_dir, 'wallpaper_vert'))

    if not isdir(join(path_dir, 'logo')):
        # ? Create the logo directory of it does not exist
        mkdir(join(path_dir, 'logo'))

    if not isdir(join(path_dir, 'others')):
        # ? Create the others directory of it does not exist
        mkdir(join(path_dir, 'others'))

    # ? get all png file
    tmp_assets = [f
                  for f in listdir(path_dir)
                  if f.split('.')[-1] == 'png'
                  ]

    for file in tmp_assets:
        # ? list all assets in the directory
        path_im = join(path_dir, file)

        # ? get the image size
        try:
            im = Image.open(path_im)
            width, height = im.size
            im.close()

            # ? Sort all image by their size
            if width == 1920:
                dst = path_dir + sep + 'wallpaper' + sep + file
                move(path_im, join(path_im, dst))

            elif width == 1080:
                dst = path_dir + sep + 'wallpaper_vert' + sep + file
                move(path_im, join(path_im, dst))

            elif width == height:
                dst = path_dir + sep + 'logo' + sep + file
                move(path_im, join(path_im, dst))

            else:
                dst = path_dir + sep + 'others' + sep + file
                move(path_im, join(path_im, dst))

        except IOError:
            remove(path_im)
