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

# Primary Class, wheeee!
class Backups:

    def next_task(self, path):
        print '======================'
        print '=Basic Backup Options='
        print '======================'
        print ''
        print '1. Images'
        print '2. Videos'
        print '3. Music'
        print '4. Archives'
        print '5. Documents'
        print ''
        print '======================'
        print '  =Advanced Options=  '
        print '======================'
        print ''
        print '6. Back up Misc files'
        print ''
        print '======================'
        print '       =Exit=         '
        print '======================'
        print ''
        print '0. Exit'
        print ''
        print '======================'

        choice = input('Enter the numerical choice: ')
        if choice == 1:
            print 'Backing up images from ~/ ...'
            print 'Only .png is supported at this time.'
            self.image_bak(path)
        elif choice == 2:
            print 'Backing up videos from ~/ ...'
            print 'Feature not yet implemented.'
            #vid_bak(path)
            menuReturn = raw_input('Do you want to return to the main menu?(y/n): ')
            if menuReturn == 'y':
                self.next_task(path)
            elif menuReturn == 'n':
                print 'Okay...'
                exit('Clean exit from next vid_bak() placeholder.')
            else:
                print 'There was a problem with your input.'
                exit('Bad exit from vid_bak() placeholder.')
        elif choice == 3:
            print 'Backing up music from ~/ ...'
            print 'Feature not yet implemented.'
            #vid_bak(path)
            menuReturn = raw_input('Do you want to return to the main menu?(y/n): ')
            if menuReturn == 'y':
                self.next_task(path)
            elif menuReturn == 'n':
                print 'Okay...'
                exit('Clean exit from next music_bak() placeholder.')
            else:
                print 'There was a problem with your input.'
                exit('Bad exit from music_bak() placeholder.')
        elif choice == 4:
            print 'Backing up archives from ~/ ...'
            self.archive_bak(path)

    # Build a worker function like a good little script kiddie
    def archive_bak(self, path):
        archivePath = path + '/backups/archives'
        if os.path.exists(archivePath) == True:
            print 'Moving archives to ~/backups/archives now ...'
            for filename in glob.glob(os.path.join(path, '*.rar')):
                shutil.move(filename, archivePath)
                print 'Archive migration complete!'
                self.next_task()
        elif os.path.exists(archivePath) == False:
            print '~/backups/archives does not exist!'
            createArchPath = raw_input('Create the backup dir for archives?(y/n): ')
            if createArchPath == 'y':
                os.makedirs(archivePath)
                self.archive_bak(self, path)
            elif createArchPath == 'n':
                print "'skip' or 'exit'?"
                cont = raw_input('Which is it?: ')
                if cont == 'skip':
                    print 'Skipping archive backup...'
                    self.next_task()
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
        if os.path.exists(imagePath) == True:
            print 'Moving images to ~/backups/images now ...'
            for filename in glob.glob(os.path.join(path, '*.png')):
                shutil.move(filename, imagePath)
                print 'Image moving complete!'
                self.next_task(path)
        elif os.path.exists(imagePath) == False:
            print '~/backups/images does not exist!'
            createImagePath = raw_input('Create the backup dir for images?(y/n): ')
            if createImagePath == 'y':
                os.makedirs(imagePath)
                self.image_bak(self, path)
            elif createImagePath == 'n':
                print "'skip' or 'exit'?"
                cont = raw_input('Which is it?: ')
                if cont == 'skip':
                    print 'Skipping image backup...'
                    self.next_task()
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
def main():
    # Initialize problem children to avoid scope errors...
    user = os.getlogin()
    path = '/home/' + user

    # Create Backups object instance. Pointer?
    bk = Backups()

    # Call Backups class
    bk.next_task(path)

# Let's get rolling
if __name__ == '__main__':
    main()