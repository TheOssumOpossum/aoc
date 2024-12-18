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

m = {}
mm = {}
viz = set()

sample = True

if sample:
    sz = 6
    bytes = 12
else:
    sz = 70
    bytes = 1024

for i in range(sz+1):
    for j in range(sz+1):
        mm[(i,j)] = float('inf')

# Line Parser
for i, line in enumerate(lines):
    a,b = [int(x) for x in re.findall('\d+', line)]
    mm[(a,b)] = i

pos = (0,0)
q = collections.deque()
q.append((0, pos))
viz.add(pos)
while q:
    step, pos = q.popleft()
    if pos == (sz, sz):
        print(step)
        break
    for d in directions:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        if new_pos not in viz and new_pos in mm and mm[new_pos] >= bytes:
            viz.add(new_pos)
            q.append((step+1, new_pos))

i = bytes
while True:
    i += 1
    exit = False
    viz = set()
    q = collections.deque()
    q.append((0,0))
    while q:
        pos = q.popleft()
        if pos == (sz, sz):
            exit = True
            break
        for d in directions:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if new_pos not in viz and new_pos in mm and mm[new_pos] >= i:
                viz.add(new_pos)
                q.append(new_pos)
    if exit == False:
        # print(i)
        for x in mm:
            if mm[x] == i-1:
                print(x)
        break
