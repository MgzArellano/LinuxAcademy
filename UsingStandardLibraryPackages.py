#!/bin/python

from time import localtime, strftime, mktime

start_time = localtime()
print("\nThis timer start at %s" % strftime("%X",start_time))


input("Please hit enter.....")

stop_time = localtime()
difference = mktime(stop_time)- mktime(start_time)

print("\nThe timer stopped at %s" % strftime("%X", stop_time))
print("Total time the program run : %s seconds)"% difference)