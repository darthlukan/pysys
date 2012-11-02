#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Filename: BetterBackup.py                                                   #
# Author: Brian Tomlinson <darthlukan@gmail.com>                              #
# URL: git@github.com:darthlukan/pysys.git                                    #
# Description: Backup program that can create archives and disc images.       #
# License: GPLv2, http://www.gnu.org/licenses/gpl-2.0.html                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# -*- coding: utf-8 -*-

import os
import sys
import glob
import shutil

''' Contains the formats that we care to work with. '''
formats = {
    'audio': ['*.mp3', '*.ogg', '*.wav'],
    'video': ['*.mpg', '*.mp4', '*.mkv',
              '*.avi', '*.mpeg', '*.mpg',
              '*.flv'],
    'image': ['*.png', '*.jpg', '*.jpeg',
              '*.gif', '*.raw', '*.svg'],
    'docs': ['*.doc', '*.docx', '*.txt',
             '*.log', '*.odt', '*.org',
             '*.xls', '*.xlsx', '*.ods'],
    'archives': ['*.rar', '*.zip', '*.tar',
                 '*.gz', '*.tgz', '*.bz2',
                 '*.tbz2', '*.7z', '*.s7z']
    }

# Get the user and their $HOME
userhome = '/home/' + os.getlogin()

''' Directories that we plan to work with. '''
dirs = {
    'home': userhome,
    'audio': userhome + '/backups/music',
    'video': userhome + '/backups/videos',
    'image': userhome + '/backups/images',
    'docs': userhome + '/backups/docs',
    'archives': userhome + '/backups/archives',
    'misc': [dirs['audio'], dirs['video'],
             dirs['image'], dirs['docs'],
             dirs['archives']]
    }

def backup_copy(op):
    '''
        This function does all of the moving.
    
        Takes a string "op" (operation) as an argument
        which is also a key in the dirs and formats dicts.
    '''
    backpath = dirs.get(op)
    backformats = formats.get(op)
    
    downloads = dirs.get('home') + '/Downloads'
    
    for type in backformats:
                for filename in glob.glob(os.path.join(downloads, type)):
                    shutil.move(filename, backpath)
    print('Backup of %s files complete!' % (op))
    return true            

def check_dirs(op):
    '''
        Verifies that the "op" (string) argument is actually a key
        in the dirs dict and checks if the value
        is an existing directory.
    
        @TODO: Offer to create the path if it does not exist.
    '''
    for key, val in dirs.items():
        if key == op and op != 'misc':
            if os.path.isdir(val):
                backup_copy(op)
            # TODO: handle creating all needed paths here.
            elif key == op and op == 'misc':
                raise NotImplementedError
            else:
                print("That directory does not exist, would you like to create it?")
                answer = input("Y/n: ")
                if answer.lower() == 'y':
                    return create_path(op)
                elif answer.lower() == 'n':
                    quitter()
                else:
                    sys.exit('Invalid input entered, exiting.')
        else:
            print('Somthing bad happened, exiting.')
            sys.exit('Logic error encountered.')
    return true

def create_path(op):
    print("Creating path to %s." % (dirs.get(op)))
    
    try:
        os.makedirs(dirs.get(op))
        check_dirs(op)
    except:
        print('An unexpected error occurred while trying to make the directory.')
        raise

# Callers. Set "op" argument
# TODO: This appears too repetitive to be the "right way".
def every():
    check_dirs('misc')
    
def pics():
    check_dirs('image')
    
def vids():
    check_dirs('video')
    
def audio():
    check_dirs('audio')
    
def docs():
    check_dirs('docs')

def archs():
    check_dirs('archives')

def quitter():
    sys.exit('Exited because of user input.')


def main():
    '''
        Sets our commands dict with references to functions.
        Provides "direction" logic.
        Exits on error.
    '''
    commands = {
            'ALL': every,
            'QUIT': quitter,
            'PICTURES': pics,
            'VIDEOS': vids,
            'MUSIC': audio,
            'DOCUMENTS': docs,
            'ARCHIVES': archs
            }
        
    while true:
        for key in commands:
            print(key)
        user_input = input('What would you like to do?: ')
        
        arg = user_input.lower()
        
        if arg in commands.keys():
            commands[arg]()
        else:
            print("%s not a recognized command." % (arg))
            sys.exit('Exiting')                

if __name__ == '__main__':
    main()