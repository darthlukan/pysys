#!/usr/bin/getenv python2
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
import time
import shutil # Somebody did the file work for you >.>
import glob   # Because Python isn't zsh

def next_task():
    # Because I'm lazy...
    print 'TODO'

class Backups:
    # Build a worker function like a good little script kiddie
    def archive_bak(self, path):
        archivePath = path + '/backups/archives'
        if os.path.exists(archivePath) == 'True':
            print 'Moving archives to ~/backups/archives now ...'
            for filename in glob.glob(os.path.join(path, '*.rar')):
                shutil.move(filename, archivePath)
                print 'Archive migration complete!'
                next_task()
        elif os.path.exists(archivePath) == 'False':
            print '~/backups/archives does not exist!'
            createArchPath = raw_input('Create the backup dir for archives?(y/n): ')
            if createArchPath == 'y':
                os.execute('mkdir -r ~/backups/archives')
                archive_bak(self, path)
            elif createArchPath == 'n':
                print "'skip' or 'exit'?"
                cont = raw_input('Which is it?: ')
                if cont == 'skip':
                    print 'Skipping archive backup...'
                    next_task()
                elif cont == 'exit':
                    print 'You must be a Windows user... Ass...'
                    exit('All work and no play makes me throw holy hand grenades.')
                else:
                    exit('You suck.')
            else:
                print 'There was a problem, probably PEBKAC again...'
                exit('L2TYPE')
        else:
            print 'Bad voodoo follows you, goodbye.'
            exit('Something in archive_bak() is B0RK3D!')

    def image_bak(self, path):
        imagePath = path + '/backups/images'
        if os.path.exists(imagePath) == 'True':
            print 'Moving images to ~/backups/images now ...'
            for filename in glob.glob(os.path.join(path, '*.png')):
                shutil.move(filename, imagePath)
                print 'Image moving complete!'
                next_task()
        elif os.path.exists(imagePath) == 'False':
            print '~/backups/images does not exist!'
            createImagePath = raw_input('Create the backup dir for images?(y/n): ')
            if createImagePath == 'y':
                os.execute('mkdir -r ~/backups/images')
                image_bak(self, path)
            elif createImagePath == 'n':
                print "'skip' or 'exit'?"
                cont = raw_input('Which is it?: ')
                if cont == 'skip':
                    print 'Skipping image backup...'
                    next_task()
                elif cont == 'exit':
                    print 'You\'re a douche for running me this far...'
                    exit('Make up your mind next time!')
                else:
                    print '''Something happened that shouldn't have, check if
                    PEBKAC is true.'''
                    exit('Something\'s b0rk3d here... >.>')
        else:
            print 'It\'s not you, it\'s me.  No, it\'s definitely you...'
            exit('Error in image_bak().  Fix me please!')

# Get rid of this awful mess please...
def get_username(username):
    username = raw_input('what is your username?: ')
    return username

def get_path(path):
    path = raw_input('Enter your path (/home/username): ')
    return path

def get_permission(consent):
    consent = raw_input('Ready to begin? (y/n): ')
    if consent == 'y':
        print 'Okay then!'
        print 'Next function not yet defined.'

def main():
    # Some cheezy functions until I put something better there
    get_username(username)
    get_path(path)
    get_permission(consent)

# Let's get rolling
if __name__ == '__main__':
    main()