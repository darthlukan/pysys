# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:18:31 2012

@author: darthlukan
"""

import os
import sys

file = sys.argv[1]

def main(file):
    print(os.path.getsize(file))
    file.close()

if __name__ == '__main__':
    main(file)
