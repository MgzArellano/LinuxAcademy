#!/bin/python

import os

stage = (os.getenv("STAGE") or "development").upper()

output = "We're running in %s" % stage

if stage.startswith("PROD"):
    print("DANGER!!! %s"% output)
else:
    print(output)
