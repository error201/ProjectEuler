#!/usr/bin/python

import datetime
counter = 0

for year in range(1901,2001,1):
    for month in range(1,13,1):
        this_date = datetime.date(year, month, 1)
        my_time = this_date.timetuple()
        print my_time
        if my_time[6] == 6:
            counter += 1
print counter
