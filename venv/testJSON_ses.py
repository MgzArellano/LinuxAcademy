#!/usr/bin/python

import os
import json

item = json.loads(open('1item.json').read())
print(item["payload"])
