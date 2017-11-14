import os
import re
import subprocess

from api_convert import Convert


class Phone:
    # __os = ""
    #
    # def __init__(self, operating_system):
    #     self.__os = operating_system

    @staticmethod
    def get_adb(command):
        try:
            # result_str = str(check_output(["adb", command]))
            # print("result_str=" + result_str)

            p = subprocess.Popen('adb ' + command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            result_str = str(stdout)

            # Clean up the result
            result_str = re.sub('^b\'', '', result_str)
            result_str = re.sub('\'$', '', result_str)
            result_str = re.sub("(\s)+", " ", result_str)
            result_str = re.sub('(\\\\r|\\\\n)+$', '', result_str)
            result_str = re.sub(r'(\\r)+', "\\\\r", result_str)
            result_str = re.sub(r'(\\n)+', "\\\\n", result_str)
            result_str = re.sub(r'(\\r\\n)+', "\\\\r\\\\n", result_str)
            return result_str.strip()
        except subprocess.CalledProcessError as e:
            print(e)
            return ""

    def get_adb_dictionary(command):
        text = Phone.get_adb(command)
        return Convert.get_dictionary(text)

    @staticmethod
    def get_count_devices():
        return len(Phone.get_devices_list())

    @staticmethod
    def get_devices_list():
        try:
            result_str = Phone.get_adb("devices")
            # ==> List of devices attached\r\nLG-MS870-96e975b\tdevice
            result_str = result_str.replace("\\tdevice", "")
            # ==> List of devices attached\r\nLG-MS870-96e975b
            result_list = result_str.split("\\r\\n")
            result_list = result_list[1:]
            # ==> result_list[0] = LG-MS870-96e975b
            return result_list
        except subprocess.CalledProcessError:
            return None

    @staticmethod
    def get_memory_pct():
        # 3 ways to get different type of memory
        # os.system("adb shell vmstat")
        # os.system("adb shell top")  # memory for each application
        result_dictionary = Phone.get_adb_dictionary('shell "cat /proc/meminfo"')
        mem_total = Convert.get_number( result_dictionary['MemTotal'] )
        if mem_total is None or mem_total == 0:
            return -1
        mem_free = Convert.get_number( result_dictionary['MemFree'] )
        if mem_free is None:
            return -1
        return int(mem_free)*100 / int(mem_total)

    @staticmethod
    def get_battery_pct():
        result_dictionary = Phone.get_adb_dictionary("shell cat /sys/class/power_supply/battery/*")
        if result_dictionary is None:
            return -1
        return result_dictionary["POWER_SUPPLY_CAPACITY"]

    @staticmethod
    def go_bluetooth():
        os.system("adb shell am start -a android.settings.BLUETOOTH_SETTINGS")

    @staticmethod
    def reboot():
        os.system("adb reboot")
