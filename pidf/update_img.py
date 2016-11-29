# -*- coding: utf-8 -*-
"""update_img.py

This module's name is 'update_img'.

"""
import subprocess
from syncmanager import SyncMananger
import constant

# main function
if __name__ == "__main__":
    
    fm = SyncMananger(constant.CONST_TOKEN)
    fm.downloads(dropbox_path=constant.CONST_IMG_DIR_NAME, local_path=constant.CONST_IMG_DIR_NAME)
    subprocess.call(['python', 'play.py'])
