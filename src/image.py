"""

"""

from os import listdir, path
from os.path import isfile, join, getsize
from shutil import copy2


def get_assets():
    """Get windows assets and copy them to TEMP/ directory"""
    path_assets = path.expandvars(r'%LOCALAPPDATA%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets')
    tmp_assets = [f
                  for f in listdir(path_assets)
                  if isfile(join(path_assets, f))]
    assets = []
    for file in tmp_assets:
        if getsize(join(path_assets, file)) >= 10000:
            assets.append(file)
            src = join(path_assets, file)
            dst = 'TEMP/' + file + '.png'
            copy2(src, dst)
    return assets
