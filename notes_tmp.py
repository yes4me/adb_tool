from api_file import Computer
from api_phone import Phone
from api_time import Time
from api_windows import Windows


computer = Computer()
phone = Phone()
time = Time()
windows = Windows(os.name)

# If the phone crashes, look at /proc/last_kmsg on reboot.
# os.system('adb shell pm list packages')
# return Phone.get_adb('shell pm list packages')

# Testing api_file
# print("0==>" + computer.get_current_directory())
# print("1==>" + str( computer.check_file_exist("D:\\save\\thomas\\job\\computer\\Python\\api_file.py") ))
# print("2==>" + str( computer.check_file_exist("api_file.py") ))
# print("3==>" + str( computer.rename_file("test.txt", "test2.txt") ))


# TO DO:
# Logcat
# Upload any apk files in the same folder to cellphone
    # subprocess.Popen("echo %s " % user_input, stdout=PIPE).stdout.read(
    # from subprocess import call, Popen, CREATE_NEW_CONSOLE
    # Popen(
    #     [executable, 'pidcat.py', '%s' % PACKAGE_NAME, '--always-display-tags', '--timestamp',
    #      '--autosave', '-i', PIDCAT_FILTER_NT],
    #     creationflags=CREATE_NEW_CONSOLE)

computer = Computer()
phone = Phone()
time = Time()
windows = Windows(os.name)

log_file = "log_" + time.get_date() + "_" + time.get_time() + ".txt"
print("log_file=" + log_file)
from subprocess import Popen, CREATE_NEW_CONSOLE
Popen('adb logcat -d > test.txt')
# Popen('adb logcat -d > ' + log_file, creationflags=CREATE_NEW_CONSOLE)
