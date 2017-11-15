import os

from api_file import Computer
from api_phone import Phone
from api_time import Time
from api_windows import Windows


computer = Computer()
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
    print('[4] Reboot cellphone')
    print('\n')
    choice = windows.get_number('Enter your Choice: ')

    if choice == 1:
        various_info()
    elif choice == 2:
        phone.get_adblog()
    elif choice == 3:
        phone.go_bluetooth()
    elif choice == 4:
        phone.reboot()
    else:
        return
    main()

windows.update_python_modules()
main()
