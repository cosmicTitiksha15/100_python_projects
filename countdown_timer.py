# | **Beginner** | **Console/CLI** | **10. Countdown Timer** | `time` module, basic loops. |
# sys module is the partner to the time module. While time handles the clock, sys (short for System) allows your Python script to interact directly with the Python interpreter and the operating system environment.

import time
import sys

time_format = input("Enter the duration of timer [hh:mm:ss] : ")
split_time = time_format.split(':')
total_seconds = int(split_time[0])*3600 + int(split_time[1])*60 + int(split_time[2])
for timer in range(total_seconds,-1,-1):
    hour = timer // 3600
    rem_hr = timer % 3600
    min = rem_hr // 60
    sec = rem_hr % 60
    # ':02d' tells Python to format the integer as a decimal with a minimum width of 2, padding it with a leading zero if necessary.
    display = f"Your time : {hour:02d} : {min:02d} : {sec:02d}"
    # '\r' moves the cursorback to the start of the line
    print(display, end='\r')
    # pause the program for 1 second
    time.sleep(1)

print("\nTime's up!")
