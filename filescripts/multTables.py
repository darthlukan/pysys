# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:53:20 2012

@author: darthlukan
"""
def main():
    i = 1
    while i <= 12:
        n = 1
        while n <= 12:
            print "%4d".rjust(4) % (i * n),
            n += 1
        print
        i += 1

main()