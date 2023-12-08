import sys
import re
import collections

day = '08'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if sys.argv[1].isdigit and int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip().splitlines()

# input parsing
s = 0
m = {}
for i, line in enumerate(lines):
    l = line.strip()
    if i == 0:
        directions = l
    elif i != 1:
        place, left, right = re.findall("\w+", l)
        m[place] = (left, right)

# part 1
steps = 0
place = 'AAA'
i = -1
while place != 'ZZZ':
    steps += 1
    i += 1
    if i == len(directions):
        i = 0
    move = directions[i]
    if move == 'L':
        place = m[place][0]
    else:
        place = m[place][1]
        
print(steps)

# part 2
steps_to_z = collections.defaultdict(list)
def calc_dist(p):
    orig_p = p
    viz = set()
    steps = 0
    i = -1
    while True:
        if p[-1] == 'Z':
            steps_to_z[orig_p].append(steps)
        steps += 1
        i += 1
        if i == len(directions):
            i = 0
        move = directions[i]
        if (p,i) in viz:
            break
        viz.add((p,i))
        if move == 'L':
            p = m[p][0]
        else:
            p = m[p][1]
  
for p in m:
    if p[-1] == 'A':
        calc_dist(p)
    
x = set()
for p in m:
    if p[-1] == 'A':
        x |= set([int(x) for x in steps_to_z[p]])

import math
print(math.lcm(*list(x)))
