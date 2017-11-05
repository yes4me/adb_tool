import os
import re


class Computer:
    __os = ""

    def __init__(self, operating_system):
        self.__os = operating_system

    @staticmethod
    def get_current_directory():
        # full path to the directory a Python file is contained in
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # get the current working directory
        # dir_path = os.getcwd()
        return dir_path

    @staticmethod
    def get_full_path_file(file_name):
        search_obj = re.search(r'\\', file_name, re.M | re.I)
        if not search_obj:
            file_name = Computer.get_current_directory() + '/' + file_name
        return file_name

    @staticmethod
    def check_file_exist(file_name):
        file_name = Computer.get_full_path_file(file_name)
        return os.path.isfile(file_name)

    @staticmethod
    def move_file(source_name, target_name):
        source_name = Computer.get_full_path_file(source_name)
        target_name = Computer.get_full_path_file(target_name)

        if not Computer.check_file_exist(source_name):
            print("Cannot rename file. Source file cannot be found")
            return False
        if Computer.check_file_exist(target_name):
            print("Target file is overwriten")
            Computer.delete_file(target_name)
        return Computer.rename_file(source_name, target_name)

    @staticmethod
    def rename_file(source_name, target_name):
        source_name = Computer.get_full_path_file(source_name)
        target_name = Computer.get_full_path_file(target_name)
        if not Computer.check_file_exist(source_name):
            print("Cannot rename file. Source file cannot be found")
            return False
        if Computer.check_file_exist(target_name):
            print("Cannot rename file. Target file exists")
            return False
        return os.rename(source_name, target_name)

    @staticmethod
    def delete_file(file_name):
        file_name = Computer.get_full_path_file(file_name)
        if Computer.check_file_exist(file_name):
            try:
                os.remove(file_name)
                return True
            except:
                return False
        return False
