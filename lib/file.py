#!/usr/bin/python
import os
import re
import sys

from lib.string import String


class File:
    @staticmethod
    def get_current_directory():
        # full path to the directory where the original file is run
        dir_path = os.path.abspath(os.path.dirname(sys.argv[0]))

        # full path to the directory where the executable Python file is contained
        # dir_path = os.path.dirname(os.path.realpath(__file__))

        # get the current working directory
        # dir_path = os.getcwd()
        return dir_path

    @staticmethod
    def is_file(file_name):
        return os.path.isfile(file_name)

    @staticmethod
    def is_directory(folder_name):
        return os.path.isdir(folder_name)

    @staticmethod
    def get_full_path_file(file_name):
        search_obj = re.search(r'\\', file_name, re.M | re.I)
        if not search_obj:
            file_name = File.get_current_directory() + '/' + file_name
        return file_name

    @staticmethod
    def get_files_by_ext(extention_name, *argv):
        # Keep only the text after the dot
        if String.left(extention_name, 1) == '.':
            extention_name = re.sub(".([a-zA-Z0-9]+)$", "\\1", extention_name)

        try:
            path_name = argv[0]
        except:
            path_name = File.get_current_directory()

        results = []
        for file in os.listdir(path_name):
            if file.endswith("." + extention_name):
                results.append(file)
        return results

    @staticmethod
    def move_file(source_name, target_name):
        source_name = File.get_full_path_file(source_name)
        target_name = File.get_full_path_file(target_name)

        if not File.check_file_exist(source_name):
            print("Cannot rename file. Source file cannot be found")
            return False
        if File.check_file_exist(target_name):
            print("Target file is overwriten")
            File.delete_file(target_name)
        return File.rename_file(source_name, target_name)

    @staticmethod
    def rename_file(source_name, target_name):
        source_name = File.get_full_path_file(source_name)
        target_name = File.get_full_path_file(target_name)
        if not File.check_file_exist(source_name):
            print("Cannot rename file. Source file cannot be found")
            return False
        if File.check_file_exist(target_name):
            print("Cannot rename file. Target file exists")
            return False
        return os.rename(source_name, target_name)

    @staticmethod
    def delete_file(file_name):
        file_name = File.get_full_path_file(file_name)
        if File.check_file_exist(file_name):
            try:
                os.remove(file_name)
                return True
            except:
                return False
        return False


if __name__ == '__main__':
    print(File.get_current_directory())

    # Testing: is_file
    # print( File.is_file("phone.py") )
    # print( File.is_file( File.get_current_directory() + "\\phone.py") )
    # print( File.is_file("abc") )
    # print( File.is_file( File.get_current_directory() + "\\abc") )
    # print( File.is_file("xxx") )

    # Testing: is_directory
    # print( File.is_directory("phone.py") )
    # print( File.is_directory( File.get_current_directory() + "\\phone.py") )
    # print( File.is_directory("abc") )
    # print( File.is_directory( File.get_current_directory() + "\\abc") )
    # print( File.is_directory("xxx") )

    # print(File.get_files_by_ext("py"))
