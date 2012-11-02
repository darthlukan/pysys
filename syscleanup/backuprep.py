#!/usr/bin/env python2
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Filename: backuprep.py                                                      #
# Author: Brian Tomlinson <darthlukan@gmail.com>                              #
# URL: git@github.com:darthlukan/pysys.git                                    #
# Description: A simple backup prepper.  Sorts files based on extension into  #
# a predefined directory tree, overwriting older versions of files by default.#
# License: GPLv2, http://www.gnu.org/licenses/gpl-2.0.html                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os
import sys
import glob
import shutil

class Backups:

    """ Backups class assumes that you have ~/backups directory populated with
    directories named 'images', 'videos', 'music', 'archives', and 'docs'. Will
    NOT overwrite files of the same name in those destination directories. """

    def __init__(self, path, dirlist):
        '''Initializes default file extensions to iterate over and provides
        commands for function calls.'''

        self.homedir = os.path.expanduser('~')

        self.data = {'movies': ['*.mpg', '*.avi', '*.mkv'],
                     'music': ['*.mp3', '*.wav', '*.ogg'],
                     'docs': ['*.odt', '*.doc', '*.ods', '*.xls'],
                     'archives': ['*.rar', '*.zip', '*.7z', '*.gz', '*.bz2']}

        self.commands = {'ALL': self.all,
                         'QUIT': self.quitter,
                         'PICTURES': self.pics,
                         'VIDEOS': self.vids,
                         'MUSIC': self.snds,
                         'DOCUMENTS': self.docs,
                         'ARCHIVES': self.archs
                         }

    def quitter(self):
        sys.exit(0)

    def worker(self, todo):
        backpath = self.homedir + '/backups'
        types = self.data[todo]

        for i in types:
            for filename in glob.glob(os.path.join(self.homedir, type)):
                    shutil.move(filename, backpath)
        print 'Archive migration complete!'
