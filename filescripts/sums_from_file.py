#!/usr/bin/env python2

import os
import sys

file = sys.argv[1]

nums = []
1nums = []
2nums = []

a = 0
b = 0
c = 0
d = 0
e = []

def loops(file):
    for line in file:
        for i in line:
            if line = file[0]:
                1nums.append(i)
            else:
                2nums.append(i)
    maths(1nums, 2nums)

def maths(1nums, 2nums):
    for i in 1nums:
        if a == 0:
            a = i
        else:
            b = i

    if c == 0:
        c = a + b
        e.append(c)
    else:
        d = a + b
        e.append(d)
    for i in e:
        print i

def main(file):
    loops(file)

main()