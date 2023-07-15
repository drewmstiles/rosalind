#!/usr/local/bin/python3
#
# Given: Positive integers n≤40 and k≤5.

# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

import os
import sys

def rabbits(n, k):

    if n <= 2:
        return 1
    else:
        return k * rabbits(n - 2, k) + rabbits(n - 1, k)
    

if __name__ == '__main__':

    ifile = os.path.join('data', sys.argv[0].replace('.py', '.txt'))

    n = -1
    k = -1

    with open(ifile, 'r') as f:
        data = f.read().strip().split(' ')
        n, k = data

    print(rabbits(int(n), int(k)))
