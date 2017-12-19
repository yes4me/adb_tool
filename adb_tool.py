#!/usr/bin/python
import os

import lib


cmd = lib.CmdWindows(os.name)
file = lib.File()
import_lib = lib.MyImport()
phone = lib.Phone()
time = lib.Time()


def various_info():
    print("Number of devices connected = " + str(phone.get_count_devices()))
    print("Memory percentage = " + str(phone.get_memory_pct()))
    print("Current battery = " + phone.get_battery_pct())


def get_apk_list(*files_apk):
    files_install = []

    # Get the list of apk files to install
    if len(files_apk) == 0:
        file_list = file.get_files_by_ext("apk")
        if len(file_list) > 0:
            print("===== apk found =====")
            for index, file_name in enumerate(file_list):
                counter = index + 1
                print("[" + str(counter) + "] " + file_name)
            print("")

            choice = cmd.get_number("Which apk would you like to install? (0 to exit) ")
            if choice == 0:
                return
            try:
                files_install.append(file_list[choice-1])
            except:
                print("Invalid choice")
                return
    else:
        files_install = files_apk
    return files_install


def install_apk():
    # Get all apk
    results = file.get_files_by_ext(".apk")

    counter = 1
    for result in results:
        print("[" + str(counter) + "] " + result)
        counter = counter + 1
    print()

    choice = cmd.get_number("Pick a APK file: ")
    if 0 < choice <= len(results):
        return phone.install_apk(results[choice - 1])
    return False


def main():
    print(colorama.Fore.CYAN)
    print('\n')
    print('[1] Information')
    print('[2] Get adb log')
    print('[3] Go to setting > Bluetooth')
    print('[4] Install apk')
    print('[5] Reboot cellphone')
    print('\n')
    print(colorama.Style.RESET_ALL)
    choice = cmd.get_number('Enter your Choice: ')

    if choice == 1:
        various_info()
    elif choice == 2:
        print("XXX: To do")
        phone.get_adblog()
    elif choice == 3:
        phone.go_bluetooth()
    elif choice == 4:
        install_apk()
    elif choice == 5:
        phone.reboot()
    else:
        return
    main()


'''
Before executing the code, it will define a few special variables.
For example, if the python interpreter is running that module (the source file) as the main program,
it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module,
__name__ will be set to the module's name.
In short, __main__ will be called only if adb_tool.py is executed. If it is imported, this will not be executed
'''


if __name__ == '__main__':
    import_lib.update_python_modules()
    colorama = import_lib.import_module('colorama')
    colorama.init(convert=True)
    main()
