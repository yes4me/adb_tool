#!/usr/bin/python
import calendar
import time

class Time:
    @staticmethod
    def get_date():
        localtime = time.localtime()
        return time.strftime("%Y%m%d", localtime)

    @staticmethod
    def get_time():
        localtime = time.localtime()
        return time.strftime("%H%M%S", localtime)

    @staticmethod
    def display_calendar(*argv):
        localtime = time.localtime()
        try:
            year = int(argv[0])
        except:
            year = int(time.strftime("%Y", localtime))

        try:
            month = int(argv[1])
        except:
            month = int(time.strftime("%m", localtime))

        cal = calendar.month(year, month)
        print(cal)
