#!/usr/bin/python
import os
import sys

from lib.convert import Convert


class CmdWindows:
    __os = ""

    def __init__(self, operating_system):
        self.__os = operating_system

    @staticmethod
    def get_string(*args):
        if len(args) == 0:
            input_text = ""
        else:
            input_text = args[0]

        sys.stdout.flush()
        try:
            text = input(input_text)
        except KeyboardInterrupt:
            return ""
        return text

    @staticmethod
    def get_number(*args):
        if len(args) == 0:
            input_text = ""
        else:
            input_text = args[0]
        text = CmdWindows.get_string(input_text)
        return Convert.get_number(text)

    def clear(self):
        if self.__os == "nt":
            os.system("cls")
        elif self.__os == "posix":
            from subprocess import call
            call(["clear"], shell=True)

    @staticmethod
    def pause():
        return CmdWindows.get_string('Press ENTER key to continue')
