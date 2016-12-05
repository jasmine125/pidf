# -*- coding: utf-8 -*-
"""update_img.py

This module's name is 'update_img'.
This module will download images in a specific directory of Dropbox.

"""
import subprocess
from syncmanager import SyncMananger
import constant

# main function
if __name__ == "__main__":

    fm = SyncMananger(constant.CONST_TOKEN)
    isChanged = fm.downloads(dropbox_path=constant.CONST_IMG_DIR_NAME, local_path=constant.CONST_IMG_DIR_NAME)
    if isChanged:
        subprocess.call(['python', 'play.py'])
        print('*** play contents.')
