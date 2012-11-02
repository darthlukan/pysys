# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 18:57:04 2012

@author: darthlukan
"""

import sys

file = sys.argv[1]

def main(file):
    for line in open(file):
        for number in line.split():
            if int(number) % 3 == 0:
                if int(number) % 5 == 0:
                    print "FB",
                else:
                    print "F",
            elif int(number) % 5 == 0 and int(number) % 3 != 0:
                print "B",
            else:
                print number,
        print

if __name__ == '__main__':
    main(file)