import sys
import re
import collections
import functools
from copy import deepcopy
sys.path.append('../')
from lib.read import read
from lib.misc import transpose, rot90, rot270, flatten

lines, groups = read(__file__)

directions = [(-1,0),(0,1),(1,0),(0,-1)]
m = {}
start = None

# Grid Parser
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        m[(i,j)] = char
        if char == '^':
            start = (i,j)
            m[(i,j)] = '.'

viz = set()
pos = start
d = directions[0]
d_i = 0
while True:
    viz.add(pos)
    new_pos = (pos[0] + d[0], pos[1] + d[1])
    if new_pos not in m:
        print('p1', len(viz))
        break
    if m[new_pos] == '#':
        d_i += 1
        d_i %= 4
        d = directions[d_i]
    else:
        pos = new_pos

sols = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if (i,j) == start:
            continue
        if m[(i,j)] == '#':
            continue
        
        viz = set()
        pos = start
        d = directions[0]
        d_i = 0
        
        while True:
            if (pos, d_i) in viz:
                sols += 1
                break
            viz.add((pos, d_i))
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if new_pos not in m:
                break
            if m[new_pos] == '#' or new_pos == (i,j):
                d_i += 1
                d_i %= 4
                d = directions[d_i]
            else:
                pos = new_pos
print('p2', sols)
