# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:06:41 2012

@author: darthlukan
"""

odd = []

def odd_print():
    for i in odd:
        print i

def main():
    for i in range(1, 100):
        if i % 2 != 0:
            odd.append(i)
    odd_print()

if __name__ == '__main__':
    main()
