"""

"""

from os import listdir, path, mkdir
from os.path import isfile, join, getsize, isdir
from shutil import copy2


def get_assets(dst_dir='TEMP'):
    """Get windows assets and copy them to a specific folder"""
    path_assets = path.expandvars(r'%LOCALAPPDATA%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets')
    tmp_assets = [f
                  for f in listdir(path_assets)
                  if isfile(join(path_assets, f))]
    new_assets = []
    for file in tmp_assets:
        if getsize(join(path_assets, file)) >= 10000:
            # ? In order to get rid of logos that are in the same folder
            new_assets.append(file)
            src = join(path_assets, file)
            dst = dst_dir + '/' + file + '.png'
            if not isfile(dst):
                # ? assets has not been collected yet
                copy2(src, dst)
    return new_assets
