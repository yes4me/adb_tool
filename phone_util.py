import os
import shutil


class Computer:
    __os = ""

    def __init__(self, os):
        self.__os = os

    @staticmethod
    def get_current_directory():
        # full path to the directory a Python file is contained in
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # get the current working directory
        # dir_path = os.getcwd()
        return dir_path

    """
    @staticmethod
    def get_full_path_file(path_source, file_name):
        return path_source + '/' + file_name

    @staticmethod
    def check_file_exist(file_fullname):
        return os.path.isfile(file_fullname)

    @staticmethod
    def move_file(path_source, path_target, file_name):
        file_source = Computer.get_full_path_file(path_source, file_name)
        file_target = Computer.get_full_path_file(path_target, file_name)

        if not Computer.check_file_exist(file_source):
            return False
        Computer.delete_file(file_target)
        shutil.move(file_source, path_target)
        return True

    @staticmethod
    def delete_file(file_fullname):
        if Computer.check_file_exist(file_fullname):
            try:
                os.remove(file_fullname)
                return True
            except:
                return False
        return False

    @staticmethod
    def find_adb_devices():
        try:
            adb_output = check_output(["adb", "devices"])
            print(adb_output)

            nlines = adb_output.count('\n')
            if nlines > 2:
                return True
        except CalledProcessError as e:
            print(e.returncode)
        return False

    @staticmethod
    def update_python_modules():
        for dist in pip.get_installed_distributions():
            call("pip install --upgrade " + dist.project_name, shell=True)

    def clear_screen(self):
        if self.__os == "nt":
            os.system("cls")
        elif self.__os == "posix":
            from subprocess import call
            call("clear", shell=True)

    @staticmethod
    def get_number(input_text, default_number):
        sys.stdout.flush()
        choice = raw_input(input_text)
        if choice.isdigit():
            return int(choice)
        else:
            return default_number

    @staticmethod
    def get_string(input_text):
        sys.stdout.flush()
        choice = raw_input(input_text)
        return choice

    @staticmethod
    def pause():
        return Computer.get_string('Press ENTER key to continue')

    @staticmethod
    def wait():
        while True:
            device_found = Computer.find_adb_devices()
            if device_found:
                break
            time.sleep(0.5)
    """


computer = Computer(os.name)


print("Hello")
# os.system("adb devices")
print("==>" + computer.get_current_directory())