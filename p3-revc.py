#!/usr/local/bin/python3
#
# Given: A DNA string s of length at most 1000 bp.
#
# Return: The reverse complement sc of s.

import os
import sys

nt_compls = { 'A' : 'T', 'C' : 'G' }
nt_compls = nt_compls | { v: k for k, v in nt_compls.items() }

ifile = os.path.join('data', sys.argv[0].replace('.py', '.txt'))

seq = ''
with open(ifile, 'r') as f:
    seq = f.read().strip()

complement = []
for nt in seq[::-1]:
    complement.append(nt_compls[nt])

print(''.join(complement))
