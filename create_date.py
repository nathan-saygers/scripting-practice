# This function consumes a date from the google API and
# returns a more human readable date object

from datetime import date
from datetime import time
from datetime import datetime

test_date = date(2002, 12, 4).ctime()

def readable_date( start ):
    date_list = start.split("-")
    date_list[2] = date_list[2].split("T")

    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2][0])

    time_list = date_list[2][1].split(":")

    hour = int(time_list[0])
    minute = int(time_list[1])
    second = int(time_list[2])

    result = datetime(year, month, day, hour, minute, second).ctime()

    return result
