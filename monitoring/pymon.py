#!/usr/bin/env python2
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Filename: pymon.py                                                          #
# Author: Brian Tomlinson <darthlukan@gmail.com>                              #
# URL: git@github.com:darthlukan/pysys.git                                    #
# Description: System monitoring in Python.                                   #
# License: GPLv2, http://www.gnu.org/licenses/gpl-2.0.html                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os
import pwd

from ConfigParser import SafeConfigParser


class Config(object):

    def __init__(self):
        self.parser = SafeConfigParser()
        self.config = self.parser.read('config.ini')
        self.sections = self.parser.sections()
        self.options = self.parser.options(self.sections)

    def get_config_file(self):
        return self.config

    def get_config_sections(self):
        return self.sections

    def get_config_options(self):
        return self.options


class User(object):

    def __init__(self, name=False, user_id=False, path=False):

        if name:
            self.name = self.set_user_by_name(name)
        else:
            self.name = self.set_user_by_name()

        if user_id:
            self.user_id = self.set_user_by_id(user_id)
        else:
            self.user_id = self.set_user_by_id()

        if path:
            self.path = self.set_user_path(path)
        else:
            self.path = self.set_user_path()

    def get_user_name(self):
        return self.name

    def get_user_id(self):
        return self.user_id

    def get_user_path(self):
        return self.path

    def set_user_by_name(self, name=False):
        """
            Sets the user's name by the provided name (str) variable,
            sets users's name to return value of os.getlogin() otherwise.

            :param name: (optional)
            :returns self.name (string):
        """
        if name:
            self.name = name
        else:
            self.name = os.getlogin()

        return self.name

    def set_user_by_id(self, user_id=False):
        """
            Sets the user's id by the provided user_id (int) variable,
            sets user's id to return value of os.getuid() otherwise.

            :param user_id: (optional)
            :returns self.user_id: (int)
        """
        if user_id:
            self.user_id = user_id
        else:
            self.user_id = os.getuid()

        return self.user_id

    def set_user_path(self, path=False):
        """
            Sets the user's path by the provided path (str) variable,
            sets user's path to return value of pwd.getpwuid(os.getuid())[5] otherwise.
            :param path: (optional)
            :returns self.path: (str)
        """
        if path:
            self.path = path
        else:
            self.path = pwd.getpwuid(os.getuid())[5]

        return self.path


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