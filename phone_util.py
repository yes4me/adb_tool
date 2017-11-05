import os

from api_file import Computer

computer = Computer(os.name)


print("Hello")
# os.system("adb devices")
print("==>" + computer.get_current_directory())
# print("1==>" + str( computer.check_file_exist("D:\\save\\thomas\\job\\computer\\Python\\api_file.py") ))
# print("2==>" + str( computer.check_file_exist("api_file.py") ))
# print("3==>" + str( computer.rename_file("test.txt", "test2.txt") ))
