import os

from api_file import Computer
from api_phone import Phone
from api_windows import Windows


computer = Computer()
phone = Phone()
windows = Windows(os.name)

def various_info():
    print("Number of devices connected = " + str(phone.get_count_devices()))
    print("Memory percentage = " + str(phone.get_memory_pct()))
    print("Current battery = " + phone.get_battery_pct())


def main():
    print('\n')
    print('[1] Information')
    print('[2] Go to setting > Bluetooth')
    print('[3] Reboot cellphone')
    print('\n')
    choice = windows.get_number('Enter your Choice: ')

    if choice == 1:
        various_info()
    elif choice == 2:
        phone.go_bluetooth()
    elif choice == 3:
        phone.reboot()
    else:
        return
    main()


# windows.update_python_modules()
main()

# If the phone crashes, look at /proc/last_kmsg on reboot.
# os.system('adb shell pm list packages')
# return Phone.get_adb('shell pm list packages')

# Testing api_file
# print("0==>" + computer.get_current_directory())
# print("1==>" + str( computer.check_file_exist("D:\\save\\thomas\\job\\computer\\Python\\api_file.py") ))
# print("2==>" + str( computer.check_file_exist("api_file.py") ))
# print("3==>" + str( computer.rename_file("test.txt", "test2.txt") ))
