#!/usr/local/bin/python3
#
# Given: A DNA string t having length at most 1000 nt.
#
# Return: The transcribed RNA string of t.

import os
import sys

ifile = os.path.join('data', sys.argv[0].replace('.py', '.txt'))

with open(ifile, 'r') as f:
    print(f.read().strip().replace('T', 'U'))
