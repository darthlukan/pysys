#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Filename: logreader.py
# Author: Brian Tomlinson
# Contact: <brian.tomlinson@mcnhealthcare.com>
# Description: A simple program that reads log output from CodeIgniter apps
# and allows you to display and write the output to another file for reporting.
# Note: requires Python 2.7.x
# Usage: python2 logreader.py </path/to/CI/log

import os
import sys

everyLine = []
debug = []
error = []
info = []
# Errors specific to PDF Conversion, NYI
pdfConvErrs = []

def check_lines(logObj):
    for line in logObj:
        line.rstrip('\r\n')
        everyLine.append(line)
    logObj.close()
    return everyLine

def sort_lines():
    for i in everyLine:
        if i.startswith('ERROR'):
            error.append(i)
        elif i.startswith('INFO'):
            info.append(i)
        elif i.startswith('DEBUG'):
            debug.append(i)
        else:
            continue

    print 'Populated lists:'
    print ''
    if len(debug) > 0:
        print 'Debug'

    if len(error) > 0:
        print 'Error'

    if len(info) > 0:
        print 'Info'
    print ''

def display_info():
    for i in info:
        print i
    get_tasks()

def display_error():
    for i in error:
        print i
    get_tasks()

def display_debug():
    for i in debug:
        print i
    get_tasks()

def display_all():
    for i in everyLine:
        print i
    get_tasks()

def output_to_file_write(copyList):
    task = copyList
    if os.path.exists('/tmp/logreader_out.log') == False:
        outputFile = open('/tmp/logreader_out.log', 'w')
    else:
        outputFile = open('/tmp/logreader_out.log', 'a')
    print 'Outputting requested information to /tmp/logreader.log'
    if task == 1:
        for i in debug:
            outputFile.writelines(i + '\n')
    elif task == 2:
        for i in error:
            outputFile.writelines(i + '\n')
    elif task == 3:
        for i in info:
            outputFile.writelines(i + '\n')
    elif task == 4:
        for i in everyLine:
            outputFile.writelines(i + '\n')
    else:
        print 'Input was invalid, returning you to the previous menu.'
        output_to_file_select()
    outputFile.flush()
    outputFile.close()
    print 'Requested operation completed successfully.'
    output_to_file_select()

def output_to_file_select():
    print 'Please select the information to copy to a file:'
    print ''
    print '1: Debug messages'
    print '2: Error messages'
    print '3: Info messages'
    print '4: All'
    print '0: Return to main menu'
    copyList = input('Enter your choice: ')
    if copyList != 0:
        output_to_file_write(copyList)
    else:
        print 'Returning you to the main menu.'
        get_tasks()

def get_tasks():
    print 'What would you like to display?'
    print '1: Debug messages'
    print '2: Error messages'
    print '3: Info messages'
    print '4: All (Messy)'
    print '5: Output to file'
    print '0: Exit'
    task = input('Enter your choice: ')

    if task == 1:
        display_debug()
    elif task == 2:
        display_error()
    elif task == 3:
        display_info()
    elif task == 4:
        display_all()
    elif task == 5:
        output_to_file_select()
    elif task == 0:
        sys.exit('User initiated exit code 0.')
    else:
        sys.exit('Invalid input, please try again using only 1, 2, 3, 4, or 0.')

def main(logObj):
    check_lines(logObj)
    sort_lines()
    get_tasks()

if __name__ == '__main__':
    logObj = open(sys.argv[1], 'r')
    main(logObj)