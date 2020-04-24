#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

if len(sys.argv) == 0:
    sys.exit("Please include a program filename to run")

cpu = CPU()

try:
    cpu.load(sys.argv[1])
except:
    sys.exit("Error: the program was unable to load")

cpu.run()