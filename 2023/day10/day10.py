import sys
import re
import collections
import functools

day = '10'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if int(sys.argv[1]) >= int(2) else 'sample'))
lines = f.read().strip().splitlines()


#part 1
m = {}
for row, line in enumerate(lines):
    l = line.strip()
    for col, c in enumerate(l):
        m[(col,row)] = c
        if c == 'S':
            start = (col,row)

q = collections.deque()
neighbors = [(0,-1), (0, 1), (-1, 0), (1, 0)]
start_neighbors = []
#up, down, left, right

max_dist = 0
pos = start
dist = 0
for i, n in enumerate(neighbors):
    neighbor_pos = (pos[0] + n[0], pos[1] + n[1])
    if neighbor_pos not in m:
        continue
    if i == 0 and m[neighbor_pos] in ['|','F','7']:
        q.append((neighbor_pos, dist+1))
        start_neighbors.append(neighbor_pos)
    elif i == 1 and m[neighbor_pos] in ['|', 'L', 'J']:
        q.append((neighbor_pos, dist+1))
        start_neighbors.append(neighbor_pos)
    elif i == 2 and m[neighbor_pos] in ['-','F','L']:
        q.append((neighbor_pos, dist+1))
        start_neighbors.append(neighbor_pos)
    elif i == 3 and m[neighbor_pos] in ['-','J','7']:
        q.append((neighbor_pos, dist+1))
        start_neighbors.append(neighbor_pos)

viz = set()
viz.add(start)
prev = start
while len(q):
    node = q.popleft()
    dist = node[1]
    pos = node[0]
    pipe = m[pos]
    if pos in viz:
        continue
    viz.add(pos)
    for i, n in enumerate(neighbors):
        neighbor_pos = (pos[0] + n[0], pos[1] + n[1])
        if neighbor_pos not in m:
            continue
        if i == 0 and m[pos] in ['|', 'L', 'J'] and m[neighbor_pos] in ['|','F','7']:
            max_dist = max(max_dist, dist+1)
            q.append((neighbor_pos, dist+1))
        elif i == 1 and m[pos] in ['|','F','7'] and m[neighbor_pos] in ['|', 'L', 'J']:
            max_dist = max(max_dist, dist+1)
            q.append((neighbor_pos, dist+1))
        elif i == 2 and m[pos] in ['-','J','7'] and m[neighbor_pos] in ['-','F','L']:
            max_dist = max(max_dist, dist+1)
            q.append((neighbor_pos, dist+1))
        elif i == 3 and m[pos] in ['-','F','L'] and m[neighbor_pos] in ['-','J','7']:
            max_dist = max(max_dist, dist+1)
            q.append((neighbor_pos, dist+1))

print('max_dist', max_dist-1)

#part 2
viz = set()
viz.add(start)
q = collections.deque()
pos = start
q.append(start_neighbors[0])

prev = start
viz = set()
loop = set()
while len(q):
    cur = q.popleft()
    loop.add(cur)
    if cur in viz:
        continue
    viz.add(cur)
    avg = ((prev[0] + cur[0])/2, (prev[1] + cur[1])/2)
    m[avg] = '#'
    for i, n in enumerate(neighbors):
        neighbor_pos = (cur[0] + n[0], cur[1] + n[1])
        if i == 0 and m[cur] in ['|', 'L', 'J'] and m[neighbor_pos] in ['|','F','7']:
            q.append(neighbor_pos)
        elif i == 1 and m[cur] in ['|','F','7'] and m[neighbor_pos] in ['|', 'L', 'J']:
            q.append(neighbor_pos)
        elif i == 2 and m[cur] in ['-','J','7'] and m[neighbor_pos] in ['-','F','L']:
            q.append(neighbor_pos)
        elif i == 3 and m[cur] in ['-','F','L'] and m[neighbor_pos] in ['-','J','7']:
            q.append(neighbor_pos)
    prev = cur
    
n = start_neighbors[1]
avg = ((n[0] + start[0])/2, (n[1] + start[1])/2)
m[avg] = '#'

inside_candidates = set()
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if (col, row) not in loop:
            inside_candidates.add((col, row))

neighbors2 = [(0, -0.5), (0, 0.5), (0.5, 0), (-0.5,0)]
s = 0
outside_set = set()
inside_set = set()
for c in inside_candidates:
    viz = set()
    q = collections.deque()
    q.append(c)
    outside = False
    while len(q):
        pos = q.popleft()
        for n in neighbors2:
            neighbor_pos = (pos[0] + n[0], pos[1] + n[1])
            if neighbor_pos[0] < 0 or neighbor_pos[1] < 0 or neighbor_pos[0] > len(lines[0]) or neighbor_pos[1] > len(lines) or neighbor_pos in outside_set:
                outside = True
                break
            if neighbor_pos in inside_set:
                break
            if neighbor_pos not in m:
                m[neighbor_pos] = '.'
            if m[neighbor_pos] not in ['#','-','|','L','F','J','7','S']:
                if neighbor_pos not in viz:
                    q.append(neighbor_pos)
                    viz.add(neighbor_pos)
        if neighbor_pos in inside_set:
            break
        if outside == True:
            outside_set |= viz
            break
    if outside == False:
        inside_set |= viz
        s += 1
print(s)
