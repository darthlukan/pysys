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

# Get the user and their $HOME
userhome = '/home/' + os.getlogin()

# Set our supported formats.
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

# Set the directories that we expect
dirs = {
    'home': userhome,
    'audio': userhome + '/backups/music',
    'video': userhome + '/backups/videos',
    'image': userhome + '/backups/images',
    'docs': userhome + '/backups/docs',
    'archives': userhome + '/backups/archives',
    'misc': userhome + '/backups/misc'
    }

# General backup function, WIP
def backup_copy(op):
    # Placeholder
    print('Backing up')
    
def check_dirs(op):
    for key, val in dirs.items():
        if key == op:
            if os.path.isdir(val):
                backup_copy(op)
            else:
                print("That directory does not exist, would you like to create it?")
                answer = input("Y/n: ")
                if answer.lower() == 'y':
                    create_path(op)
                elif answer.lower() == 'n':
                    quitter()
                else:
                    sys.exit('Invalid input entered, exiting.')
        else:
            print('Somthing bad happened, exiting.')
            sys.exit('Logic error encountered.')

# Callers    
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