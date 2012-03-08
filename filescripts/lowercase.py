# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:18:31 2012

@author: darthlukan
"""

import sys
import fileinput

file = sys.argv[1]

def main(file):

    for line in fileinput.input(file):
        line.rstrip('\r\n')
        print(str.lower(line))

if __name__ == '__main__':
    main(file)
