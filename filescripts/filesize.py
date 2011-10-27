#!/usr/bin/python2
# Filename: filesize.py
# Author: Brian Tomlinson <darthlukan@gmail.com>
# Description: Run this program, give it a path to your file, recieve the file
# size in bytes.

import os, sys # os for os.path.getsize(), sys for exit()

# Define and get our variables
fget = raw_input('Please provide the absolute path and name of your file: ')
fsize = os.path.getsize(fget)
# Do work if fsize is an integer, die otherwise
if fsize > 0:
    print 'Your file is', fsize, 'bytes in size.'
    exit(0)
else:
    print('There was an error with your file input, please try again.')
    exit('File read error: Filesize is not greater than zero.')
