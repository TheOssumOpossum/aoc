import sys
import re
import collections
import functools

day = ''' + '\'{}\''.format(day) + '''
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample2' if sys.argv[1] == '2' else 'sample'))
lines = f.read().strip().splitlines()

s = 0
m = {}
for i, line in enumerate(lines):
    l = line.strip()
