#!/usr/bin/env python

import numpy as np
import sys

from pathlib import Path

if len(sys.argv) != 2:
    print('Usage:')
    print('./convert.py file')
    print('\tfile - path to the file to convert')

f = Path(sys.argv[1])

if not f.is_file():
    exit('File does not exist')

f = f.open()

min_bin = np.inf
max_bin = -np.inf

print('Calculating number of elements...')
n_lines = sum(1 for i in f)

arr = np.zeros(n_lines)
print('Created an array with %s elements' % n_lines)

f.seek(0)

for i, l in enumerate(f):
    b, flux = l.strip().split()
    b = int(b)
    min_bin = min(min_bin, b)
    max_bin = max(max_bin, b)
    print(i, flux)
    arr[i] = float(flux)

f.close()
