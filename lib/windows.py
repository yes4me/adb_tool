import os
import subprocess
import sys

import pip

from lib.convert import Convert


class Windows:
    __os = ""

    def __init__(self, operating_system):
        self.__os = operating_system

    @staticmethod
    def get_string(input_text):
        sys.stdout.flush()
        try:
            text = input(input_text)
        except KeyboardInterrupt:
            return ""
        return text

    @staticmethod
    def get_number(input_text):
        text = Windows.get_string(input_text)
        return Convert.get_number(text)

    def clear(self):
        if self.__os == "nt":
            os.system("cls")
        elif self.__os == "posix":
            from subprocess import call
            call(["clear"], shell=True)

    @staticmethod
    def pause():
        return Windows.get_string('Press ENTER key to continue')

    @staticmethod
    def update_python_modules():
        for dist in pip.get_installed_distributions():
            subprocess.call(["pip install --upgrade " + dist.project_name], shell=True)
