#!/usr/bin/python2
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Filename: dirtests-curses.py                                              #
# Author: Brian Tomlinson <darthlukan@gmail.com>                            #
# License: GPLv2                                                            #
# Description: Some simple directory tests using Python's curses module.    #
# Note: Experimental! Not meant to be anything other than a learning tool.  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os
import sys
import glob
import curses
import shutil
import fileinput
import subprocess

def main():
    screen = curses.initscr()
    curses.start_color()
    screen.border(0)

    screen.addstr(2, 2, "We will now attempt to display '/' data with df -h...")
    screen.refresh()
    screen.addstr(2, 2, subprocess.check_output(["df", "-h", "/"]))
    screen.refresh()
    screen.addstr(8, 6, "Do you see the output?")
    screen.addstr(12, 2, "1. Yes")
    screen.addstr(13, 2, "2. No")
    screen.refresh()

    x = screen.getch()

    if x == ord('1'):
        screen.addstr("Cool! It worked :)")
        screen.refresh()
        curses.endwin()
    else:
        screen.addstr("That's too bad, time to refactor.")
        screen.refresh()
        curses.endwin()

main()