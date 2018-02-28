#!/usr/bin/python

# Learn to search files by name using (glob) patterns and find replacements
# in the standard library for common UNIX tools like mv, mkdir, cp, and rm.

# this script will process recepts

import glob
import os
import shutil
import json

try:
    os.mkdir("./new/processed")
except OSError:
    print("'processed' directory already exists")

# Get a list of receipts
receipts = glob.glob('./new/receipt-[0-9]*.json')

subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split('/')[-1]
    destination = "./new/processed/%s" % name
    shutil.move(path, destination)
    print("moved '%s' to '%s'" % (path,destination))
# Iterate over the receipts
print("Receipt subtotal: $%.2f" % subtotal)

    # read content and tally subtotal
    # mv the file to processed directory
    # print that we processed the file

# Print the subtotal of all processed receipts
