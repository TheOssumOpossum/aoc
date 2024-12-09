import sys
import re
import collections
import functools
from copy import deepcopy
sys.path.append('../')
from lib.read import read
from lib.misc import transpose, rot90, rot270, flatten

lines, groups = read(__file__)

l = {}
# Line Parser
for i, line in enumerate(lines):
    id = 0
    space = False
    for c in line:
        if not space:
            for _ in range(int(c)):
                l[len(l)] = str(id)
            id += 1
            space = not space
        else:
            for _ in range(int(c)):
                l[len(l)] = '.'
            space = not space
l2 = deepcopy(l)

min_free = 0
for i in range(len(l)-1,0,-1):
    if l[i] != '.':
        for j in range(min_free, len(l)):
            if l[j] == '.':
                l[j] = l[i]
                l[i] = '.'
                min_free = j-1
                break

s = 0
for i, x in sorted(list(l.items())):
    if x == '.':
        continue
    s += int(x) * (i-1)
print('p1', s)

### p2

cur_length = 0
cur_start = 0
prev_char = None
l3 = {} # character, length
for i in range(len(l2)):
    if l2[i] != prev_char or i == len(l2)-1:
        if i == len(l2)-1:
            cur_length += 1
        if prev_char is not None:
            l3[cur_start] = (prev_char, cur_length)
        cur_start = i
        prev_char = l2[i]
        cur_length = 1
    else:
        cur_length += 1

processed = set()
restart = False
while len(processed) < id:
    for src in sorted(list(l3))[::-1]:
        if l3[src][0] == '.' or l3[src][0] in processed:
            continue
        processed.add(l3[src][0])
        for dest in sorted(list(l3)):
            if l3[dest][0] != '.':
                continue
            if dest >= src:
                break
            if l3[dest][1] >= l3[src][1]:
                remaining = l3[dest][1] - l3[src][1]
                l3[dest] = (l3[src][0], l3[src][1])
                if remaining > 0:
                    l3[dest+l3[src][1]] = ('.', remaining)
                    restart = True
                l3[src] = ('.', l3[src][1])
                break
        if restart:
            break

ss = 0
for i in sorted(list(l3)):
    for j in range(l3[i][1]):
        if l3[i][0] == '.':
            continue
        ss += int(l3[i][0]) * (i+j)
print('p2', ss)
