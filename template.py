import os
import sys
import re
import collections
import functools
from copy import deepcopy

f = open(f'{f"{os.path.dirname(os.path.realpath(__file__))}/../input/{os.path.dirname(os.path.realpath(__file__))[-4:]}/" if (len(sys.argv) >= 2 and sys.argv[1] == "1") else f"{os.path.dirname(os.path.realpath(__file__))}/"}{os.path.split(os.path.realpath(__file__))[1][3:5]}_{"data" if (len(sys.argv) >= 2 and sys.argv[1] == "1") else "sample" if len(sys.argv) < 2 or sys.argv[1] == "0" else "sample" + sys.argv[1]}.txt')
txt = f.read().strip()
lines = txt.split('\n')
groups = txt.split('\n\n')

directions = [(0,1),(-1,0),(0,-1),(1,0)]
directions_map = {y:directions[x] for x,y in enumerate('RULD')}
m = {}
viz = set()
s = 0
# Line Parser
for i, line in enumerate(lines):
    pass

# Character Parser
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        pass

# Grid Parser
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        m[(i,j)] = char

# Group Parser
for i, group in enumerate(groups):
    for j, line in enumerate(group.splitlines()):
        pass

print(s)