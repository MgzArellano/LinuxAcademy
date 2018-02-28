#!/usr/bin/python

import glob
import os
import shutil
import json
import re
import math


try:
    os.mkdir("./new/processed")
except OSError:
    print("'processed' directory already exists")

receipts = [f for f in glob.iglob('./new/receipt-[0-9]*.json')
            if re.match('./new/receipt-[0-9]*[02468].json', f)]

subtotal = 0.0


for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    destination = path.replace('new', 'new/processed')
    shutil.move(path, destination)
    print("moved '%s' to '%s'" % (path,destination))

# Iterate over the receipts
print("Receipt subtotal: $%.2f" % round(subtotal, 2))

    # read content and tally subtotal
    # mv the file to processed directory
    # print that we processed the file

# Print the subtotal of all processed receipts