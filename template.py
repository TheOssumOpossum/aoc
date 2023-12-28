import os
import sys
import re
import collections
import functools
from copy import deepcopy

f = open(f'{f"../input/{os.path.dirname(os.path.realpath(__file__))[-4:]}/" if (len(sys.argv) >= 2 and sys.argv[1] == "1") else ""}{os.path.split(os.path.realpath(__file__))[1][3:5]}_{"data" if (len(sys.argv) >= 2 and sys.argv[1] == "1") else "sample" if len(sys.argv) < 2 or sys.argv[1] == "0" else "sample" + sys.argv[1]}.txt')
txt = f.read().strip()
lines = txt.split('\n')
groups = txt.split('\n\n')

directions = [(0,1),(-1,0),(0,-1),(1,0)]
m = {}
s = 0
for i, line in enumerate(lines):
    pass

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        m[(i,j)] = char

for i, group in enumerate(groups):
    for j, line in enumerate(group.splitlines()):
        pass

print(s)