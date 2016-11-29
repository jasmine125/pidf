# -*- coding: utf-8 -*-
"""play.py

This module's name is 'play'.
Please use this module for playing image files.

"""
#from subprocess import call
import os

# main function
if __name__ == "__main__":
    # play the slideshow
    # fbi -a -T 2 -t 60 -noverbose `find ./images -iname "*.jpg"`
    #cmd = '''sudo fbi -a -T 2 -t 60 -noverbose /`find .//images -iname /"*.jpg/"/`'''
    #cmd_args = cmd.split()

    #call(cmd_args)
    os.system('sudo pkill fbi')
    os.system('sudo fbi -a -T 2 -t 30 -noverbose `find ./images -iname "*.jpg"`')


