#!/usr/bin/python3.5

#   Environment variables are often used for configuring command line tools and scripts. Write a script that does the following:

#   Prints the first ten digits of Pi to the screen.
#   Accepts an optional environment variable called DIGITS. If present, the script will print that many digits of Pi instead of 10.
#   Note: You’ll want to import pi from the math package.

#   This task will require some more advanced string formatting. You can read the documentation here, but here’s an example of how you could print a float to ten digits: print("%.*f" % (10, my_float))


from os import getenv
from math import pi

digits = getenv("DIGITS") or 10

print("\n")
print("%.*f" % (digits, pi))
