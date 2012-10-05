#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: darthlukan
"""
# Modules whose methods we'll need
import os
import sys

# This is how to define a function
def main():
    # This is how we define variables in Python, in this case, we're gathering
    # information about the system using the modules that we imported above.
    uname = os.uname()
    # This is "list notation" (for lack of a better term)
    # We are setting opsys to the item in the list uname that is
    # in the "zero-th" position.
    opsys = uname[0]
    # Same as with opsys, but with the item in the number 1 position.
    hostname = uname[1]
    kernel = uname[2]
    arch = uname[4]
    cwd = os.getcwd()

    # Grabs the Python interpreter version as a list of values, see next comment.
    version = sys.version_info

    # This is a "simple" yet non-elegant way of taking values from a list
    # and converting them to strings.  str(i) is casting numeric values as
    # strings so that Python doesn't get confused when we use '+' and try to
    # perform math.  Instead, it concatenates the 'strings'.
    pyversion = str(version[0]) + '.' + str(version[1]) + '.' + str(version[2])

    # This is a way of creating a dictionary.  Dictionaries are maps that use
    # 'key, value' pairs.  The keys can be almost anything, strings, numbers, etc.
    infodict = {'OS': opsys,
                'Hostname': hostname,
                'Kernel Version': kernel,
                'Architecture': arch,
                'Python Version': pyversion,
                'Current Directory': cwd
                }

    # This is a way of iterating over a dictionary in order to print the keys
    # and values. Note the comma, this adds a space between the keys and values.
    for key, value in infodict.items():
        print key + ':', value

    # Here we define alist and populate it with some
    # default values.  Lists are like dictionaries, but without
    # explicity 'keys'.  Instead, their keys are implied by position.
    # Check above where we set uname and opsys to see how we use
    # list (position) keys.
    example_list = ['Foo', 'Bar', 'Baz', 'Bazinga'
		    'lists', 'can', 'hold', 'numbers',
		    'like', 1, 2, 3, 4, 'as well.']

    # A simple for loop.  We call an "imaginary" 'i' into being,
    # this 'i' is an 'iterator'.  It moves over each item inside of
    # our example_list and 'becomes' that item until it is moved
    # to the next item in the list.
    for i in example_list:
	print i

    # Exits the program/script and prints a message to stdout (terminal).
    sys.exit('Output printed. Bye.')

# A very "pythonic" way of starting things off.  This checks if we are importing
# this script for use as a module, or if we are running it as a script/program.
# If a script/program, this check is TRUE and the call to our main() function
# is executed.  If we import this file as a module (like we did with os and sys)
# then main() will not be executed.  This is useful if your script has useful
# methods in it that you want to use in another program without having to re-write
# all of the same stuff in that program, just import and call your methods.
if __name__ == '__main__':
    main()
