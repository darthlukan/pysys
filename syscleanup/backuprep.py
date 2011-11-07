#!/usr/bin/python2
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Filename: backuprep.py                                                      #
# Author: Brian Tomlinson <darthlukan@gmail.com>                              #
# URL: git@github.com:darthlukan/pysys.git                                    #
# Description: A simple backup prepper.  Sorts files based on extension into  #
# a predefined directory tree, overwriting older versions of files by default.#
# License: GPLv2, http://www.gnu.org/licenses/gpl-2.0.html                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os
import shutil # Somebody did the file work for you >.>
import glob   # Because Python isn't zsh

# Primary Class, wheeee!
class Backups:

    """ Backups class assumes that you have ~/backups directory populated with
    directories named 'images', 'videos', 'music', 'archives', and 'docs'. Will
    NOT overwrite files of the same name in those destination directories. """

    def next_task(self, path, dirlist):
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
            print 'Only .png files are supported at this time.'
            self.image_bak(path, dirlist)
        elif choice == 2:
            print 'Backing up videos from ~/ ...'
            print 'Only .avi files are supported at this time.'
            self.vid_bak(path, dirlist)
        elif choice == 3:
            print 'Backing up music from ~/ ...'
            print 'Only .mp3 files are supported at this time.'
            self.music_bak(path, dirlist)
        elif choice == 4:
            print 'Backing up archives from ~/ ...'
            print 'Only .rar files are supported at this time.'
            self.archive_bak(path, dirlist)
        elif choice == 5:
            print 'Backing up documents from ~/ ...'
            print 'Only .doc files are supported at this time.'
        elif choice == 6:
            print 'Routing you to advanced backup functions...'
            print 'Warning! There be dragons ahead!'
            print 'Feature not yet implemented.'
            self.misc_bak(path, dirlist)
        else:
            print 'Initiating clean exit.'
            exit(0)

    # TODO: Build a worker function, this is getting repetitive...
    def archive_bak(self, path, dirlist):
        archtypes = ['*.rar', '*.zip', '*.tar', '*.tar.gz', '*.tgz', 
                     '*.tar.bz2', '*.tbz2', '*.bz2', '*.7z', '*.s7z']
        archivePath = dirlist[0]
        if os.path.exists(archivePath) == True:
            print 'Moving archives to ~/backups/archives now ...'
            for filename in glob.glob(os.path.join(path, archtypes)):
                shutil.move(filename, archivePath)
                print 'Archive migration complete!'
            self.next_task(path, dirlist)
        elif os.path.exists(archivePath) == False:
            print '~/backups/archives does not exist!'
            createArchPath = raw_input('Create the backup dir for archives?(y/n): ')
            if createArchPath == 'y':
                os.makedirs(archivePath)
                self.archive_bak(self, path, dirlist)
            elif createArchPath == 'n':
                print "'skip' or 'exit'?"
                cont = raw_input('Which is it?: ')
                if cont == 'skip':
                    print 'Skipping archive backup...'
                    self.next_task(path, dirlist)
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

    def image_bak(self, path, dirlist):
        imagePath = dirlist[1]
        if os.path.exists(imagePath) == True:
            print 'Moving images to ~/backups/images now ...'
            for filename in glob.glob(os.path.join(path, '*.png')):
                shutil.move(filename, imagePath)
                print 'Image moving complete!'
            self.next_task(path, dirlist)
        elif os.path.exists(imagePath) == False:
            print imagePath
            print '~/backups/images does not exist!'
            createImagePath = raw_input('Create the backup dir for images?(y/n): ')
            if createImagePath == 'y':
                os.makedirs(imagePath)
                self.image_bak(self, path, dirlist)
            elif createImagePath == 'n':
                print "'skip' or 'exit'?"
                cont = raw_input('Which is it?: ')
                if cont == 'skip':
                    print 'Skipping image backup...'
                    self.next_task(path, dirlist)
                elif cont == 'exit':
                    print 'You\'re a douche for running me this far...'
                    exit('Make up your mind next time!')
                else:
                    print '''Something happened that shouldn't have, check if
                    PEBKAC is true...'''
                    exit('Something\'s b0rk3d here... >.>')
        else:
            print 'It\'s not you, it\'s me.  No, it\'s definitely you...'
            exit('Error in image_bak().  Fix me please!')

    def vid_bak(self, path, dirlist):
        vidPath = dirlist[2]
        if os.path.exists(vidPath) == True:
            print 'Moving videos to ~/backups/videos now ...'
            for filename in glob.glob(os.path.join(path, '*.avi')):
                shutil.move(filename, vidPath)
                print 'Video moving complete!'
            self.next_task(path, dirlist)
        elif os.path.exists(vidPath) == False:
            print '~/backups/vidoes does not exist!'
            createVidPath = raw_input('Create the backup dir for videos?(y/n): ')
            if createVidPath == 'y':
                os.makedirs(vidPath)
                self.vid_bak(self, path, dirlist)
            elif createVidPath == 'n':
                print "'skip' or 'exit'?"
                cont = raw_input('Which is it?: ')
                if cont == 'skip':
                    print 'Skipping video backup...'
                    self.next_task(path, dirlist)
                elif cont == 'exit':
                    print 'This is why we can\'t have nice things...'
                    exit('Goodbye!')
                else:
                    exit('No, really, there are only two options...')
            else:
                print 'There was an error in your input.'
                print 'Sending you back to the main menu...'
                self.next_task(path, dirlist)
        else:
            print 'Something went horribly wrong, raising exit()'
            exit('Error in vid_bak(), a little love would be nice...')

    def doc_bak(self, path, dirlist):
        docPath = dirlist[3]
        if os.path.exists(docPath) == True:
            print 'Moving docs to ~/backups/docs now ...'
            for filename in glob.glob(os.path.join(path, '*.doc')):
                shutil.move(filename, docPath)
                print 'Doc moving complete!'
            self.next_task(path, dirlist)
        elif os.path.exists(docPath) == False:
            print '~/backups/docs does not exist!'
            createDocPath = raw_input('Create the backup dir for docs?(y/n): ')
            if createDocPath == 'y':
                os.makedirs(docPath)
                self.doc_bak(self, path, dirlist)
            elif createDocPath == 'n':
                print "'skip' or 'exit'?"
                cont = raw_input('Which is it?: ')
                if cont == 'skip':
                    print 'Skipping doc backup...'
                    self.next_task(path, dirlist)
                elif cont == 'exit':
                    print 'This is why we can\'t have nice things...'
                    exit('Goodbye!')
                else:
                    exit('No, really, there are only two options...')
            else:
                print 'There was an error in your input.'
                print 'Sending you back to the main menu...'
                self.next_task(path, dirlist)
        else:
            print 'Something went horribly wrong, raising exit()'
            exit('Error in doc_bak(), a little love would be nice...')

    def music_bak(self, path, dirlist):
        musicPath = dirlist[4]
        if os.path.exists(musicPath) == True:
            print 'Moving music to ~/backups/music now ...'
            for filename in glob.glob(os.path.join(path, '*.mp3')):
                shutil.move(filename, musicPath)
                print 'Music moving complete!'
            self.next_task(path, dirlist)
        elif os.path.exists(musicPath) == False:
            print '~/backups/music does not exist!'
            createMusicPath = raw_input('Create the backup dir for music?(y/n): ')
            if createMusicPath == 'y':
                os.makedirs(musicPath)
                self.music_bak(self, path, dirlist)
            elif createMusicPath == 'n':
                print "'skip' or 'exit'?"
                cont = raw_input('Which is it?: ')
                if cont == 'skip':
                    print 'Skipping music backup...'
                    self.next_task(path)
                elif cont == 'exit':
                    print 'This is why we can\'t have nice things...'
                    exit('Goodbye!')
                else:
                    exit('No, really, there are only two options...')
            else:
                print 'There was an error in your input.'
                print 'Sending you back to the main menu...'
                self.next_task(path, dirlist)
        else:
            print 'Something went horribly wrong, raising exit()'
            exit('Error in music_bak(), a little love would be nice...')

    def misc_bak(self, path, dirlist):
        # TODO: Add advanced features for multiple file specifications and
        # alternate directories/file types.
        print 'TODO, sending you back to the main menu.'
        self.next_task(path, dirlist)

# Not the most elegant solution...
def main():
    # There has to be a better way...
    user = os.getlogin()
    path = '/home/' + user
    dirlist = [path + '/backups/archives', path + '/backups/images', 
               path + '/backups/videos', path + '/backups/docs', 
               path + '/backups/music', path + '/backups/misc']
    # Create Backups object instance. Pointer?
    bk = Backups()

    # Call Backups class
    bk.next_task(path, dirlist)

# Let's get rolling
if __name__ == '__main__':
    main()
