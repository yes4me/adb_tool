import importlib
import os

from lib.file import File
from lib.phone import Phone
from lib.time import Time
from lib.windows import Windows


file = File()
phone = Phone()
time = Time()
windows = Windows(os.name)

def various_info():
    print("Number of devices connected = " + str(phone.get_count_devices()))
    print("Memory percentage = " + str(phone.get_memory_pct()))
    print("Current battery = " + phone.get_battery_pct())


def main():
    print('\n')
    print('[1] Information')
    print('[2] Get adb log')
    print('[3] Go to setting > Bluetooth')
    print('[4] Install apk')
    print('[5] Reboot cellphone')
    print('\n')
    choice = windows.get_number('Enter your Choice: ')

    if choice == 1:
        various_info()
    elif choice == 2:
        phone.get_adblog()
    elif choice == 3:
        phone.go_bluetooth()
    elif choice == 4:
        phone.install_apk()
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
    # windows.update_python_modules()
    main()


def install_apk():
    # Get all apk
    results = file.get_file_extension(".apk")

    counter = 1
    for result in results:
        print("[" + str(counter) + "] " + result)
        counter = counter + 1
    print()

    choice = windows.get_number("Pick a APK file: ")
    if choice > 0 and choice <= len(results):
        choice = choice - 1
    print(choice)

install_apk()
