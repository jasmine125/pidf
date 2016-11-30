# -*- coding: utf-8 -*-
"""play.py

This module's name is 'play'.
Please use this module for playing image files.
You must install the fbi(framebuffer imageviewer).
 - how to install fbi: apt-get install fbi

"""

import os

# main function
if __name__ == "__main__":

    # kill a previous fbi process.
    os.system('sudo pkill fbi')

    # execute the fbi.
    os.system('sudo fbi -a -T 2 -t 30 -noverbose `find ./images -iname "*.jpg"`')