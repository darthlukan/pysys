#!/usr/bin/env python2
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Filename: backuprep.py                                                      #
# Author: Brian Tomlinson <darthlukan@gmail.com>                              #
# URL: git@github.com:darthlukan/pysys.git                                    #
# Description: A simple backup prepper.  Sorts files based on extension into  #
# a predefined directory tree, overwriting older versions of files by default.#
# License: GPLv2, http://www.gnu.org/licenses/gpl-2.0.html                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# -*- coding: utf-8 -*-

import os
import glob
import shutil

# File Type Lists, audio, video, images, documents, archives
audlst = ['*.mp3', '*.ogg', '*.wav']

vidlst = ['*.mpg', '*.mp4', '*.mkv',
          '*.avi', '*.mpeg', '*.mpg', '*.flv']

imglst = ['*.png', '*.jpg', '*.jpeg',
          '*.gif', '*.raw', '*.svg']

doclst = ['*.doc', '*.docx', '*.txt',
          '*.log', '*.odt', '*.org',
          '*.xls', '*.xlsx', '*.ods']

archlst = ['*.rar', '*.zip', '*.tar',
            '*.gz', '*.tgz', '*.bz2',
            '*.tbz2', '*.7z', '*.s7z']

typeslist = [audlst, vidlst, imglst, doclst, archlst]

# Get the user and their $HOME
userhome = '/home/' + os.getlogin()

# Hard-coding the expected backup paths, user interaction based pathing
# will happen later.
dirlist = [userhome + '/backups/archives', userhome + '/backups/images',
           userhome + '/backups/videos', userhome + '/backups/docs',
           userhome + '/backups/music', userhome + '/backups/misc']

# General backup function, WIP
def backup_copy():
    print "TODO"