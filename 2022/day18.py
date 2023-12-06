import sys
import re 
day = 18
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

lines = f.read().splitlines()

max_x = max_y = max_z = 0
cubes = set()
for line in lines:
    l = line.strip()
    x,y,z = [int(i) for i in re.findall('\d+', l)]
    cubes.add((x,y,z))
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    max_z = max(z, max_z)
max_x += 1
max_y += 1
max_z += 1

s = 0
m = {}
for a in cubes:
    for j in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
        x = (a[0]+j[0], a[1]+j[1], a[2]+j[2])
        if x not in cubes:
            s += 1
            if x not in m:
                m[x] = 0
            m[x] += 1
print('part1', s)

def get_neighbors(a):
    x = []
    for j in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
        x.append((a[0]+j[0], a[1]+j[1], a[2]+j[2]))
    return x

import collections
vviz = {}
for i in m:
    viz = set()
    qq = get_neighbors(i)
    q = collections.deque([])
    for aa in qq:
        if aa not in cubes:
            q.append(aa)
    air = False
    while len(q) > 0:
        a = q.popleft()
        if a in vviz:
            air = True if vviz[a] == 1 else False
            break
        viz.add(a)
        if a not in cubes:
            qq = get_neighbors(a)
            for aa in qq:
                if aa not in viz and aa not in cubes:
                    viz.add(aa)
                    q.append(aa)
        if a[0] == 0 or a[1] == 0 or a[2] == 0 or a[0] == max_x or a[1] == max_y or a[2] == max_z:
            air =True
            break
    if not air:
        s -= m[i]
        for i in viz:
            vviz[i] = -1
    else:
        for i in viz:
            vviz[i] = 1

print('part2', s)
