#!/usr/bin/python

#Environment variables are often used for configuring command line tools and scripts. Write a script that does the following:
#Prints the first ten digits of Pi to the screen.
#Accepts an optional environment variable called DIGITS. If present, the script will print that many digits of Pi instead of 10.
#Note: You’ll want to import pi from the math package.
from os import getenv
from math import pi



digits = getenv("DIGITS", 10)

print("%.*f" % (digits, pi))
