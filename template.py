import sys
import re
import collections
import functools
from copy import deepcopy
sys.path.append('../')
from lib.read import read
from lib.misc import transpose, rot90, rot270, flatten

lines, groups = read(__file__)

directions = [(0,1),(-1,0),(0,-1),(1,0)] # right, up, left, down
directions_map = {y:directions[x] for x,y in enumerate('RULD')}
m = {}
viz = set()
s = 0
ss = 0

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
print(ss)
