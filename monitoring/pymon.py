#!/usr/bin/env python2
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Filename: pymon.py                                                          #
# Author: Brian Tomlinson <darthlukan@gmail.com>                              #
# URL: git@github.com:darthlukan/pysys.git                                    #
# Description: System monitoring in Python.                                   #
# License: GPLv2, http://www.gnu.org/licenses/gpl-2.0.html                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from ConfigParser import SafeConfigParser


class Config(object):

    def __init__(self):
        self.config = ''
        self.sections = []
        self.options = []
        self.parser = SafeConfigParser()

    def get_config_file(self):
        self.config = self.parser.read('config.ini')
        return self.config

    def get_config_sections(self):
        # We have to call get_config_file() for tests.
        self.get_config_file()
        self.sections = self.parser.sections()
        return self.sections

    def get_config_options(self):
        self.get_config_file()
        self.get_config_sections()
        self.options = self.parser.options(self.sections[0])
        return self.options


def main():
    c = Config()

    print 'File:', c.get_config_file()
    print 'Sections:', c.get_config_sections()
    print 'Var Sections:', c.sections
    print 'Options:', c.get_config_options()
    print 'Var Options:', c.options

    return True


if __name__ == '__main__':
    main()