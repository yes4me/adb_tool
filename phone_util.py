import os

from api_file import Computer
from api_phone import Phone

computer = Computer()
phone = Phone()


# Testing api_file
# print("0==>" + computer.get_current_directory())
# print("1==>" + str( computer.check_file_exist("D:\\save\\thomas\\job\\computer\\Python\\api_file.py") ))
# print("2==>" + str( computer.check_file_exist("api_file.py") ))
# print("3==>" + str( computer.rename_file("test.txt", "test2.txt") ))

print("BEGIN")
# print("Phone counter = "+ str(phone.count_devices()))
print(phone.get_memory())
# phone.get_freememory()
# phone.get_battery()
print("END")


# To watch the memory: cat /proc/meminfo
# If the phone crashes, look at /proc/last_kmsg on reboot.
# os.system('adb shell pm list packages')
# return Phone.get_adb('shell pm list packages')
