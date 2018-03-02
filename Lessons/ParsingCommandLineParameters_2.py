#!/usr/bin/python

# Parsing command line parameters

import argparse

print("\nParsing Command Line Parameters 2\n")

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='help to read')
parser.add_argument('--limit', '-l', type=int, help='The number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 2.0')

#"%(prog)s 2.0" % {'prog': 'reverse-file'}

args=parser.parse_args()

try:
    f = open(args.filename)
except IOError as err:
    print("Error: file not found")
else:

    with f:
        limit = args.limit
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:args.limit]

        for line in lines:
            print(line.strip()[::-1])

finally:
    print("\nWe're finished\n")