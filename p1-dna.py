#!/usr/local/bin/python3
#
# Given:
#    A DNA string s of length at most 1000 nt.
#
# Return:
#    Four integers (separated by spaces) counting the
#    respective number of times that the symbols
#    'A', 'C', 'G', and 'T' occur in s.

import os
import sys

seq = ''
ifile = os.path.join('data', sys.argv[0].replace('.py', '.txt'))

with open(ifile, 'r') as f:
    seq = f.read().strip()

nts = [ 'A', 'C', 'G', 'T' ]
counts = dict.fromkeys(nts, 0)

for nt in seq:
    counts[nt] = counts.get(nt, 0) + 1

for nt in nts:
    print(str(counts[nt]), end=' ')
