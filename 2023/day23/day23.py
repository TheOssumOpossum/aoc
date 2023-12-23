import sys
import collections
from copy import deepcopy

day = '23'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip().splitlines()

source = None
m = collections.defaultdict(str)
for row, line in enumerate(lines):
    l = line.strip()
    for col, char in enumerate(l):
        m[(row, col)] = char
        if char == '.':
            destination = (row, col)
        if source is None and char == '.':
            source = (row, col)

neighbors = [(0, 1), (-1, 0), (0, -1), (1, 0)]

# part 1
def find_max_dist(pos, viz):
    count = 0
    q = collections.deque()
    q.append(pos)
    while q:
        pos = q.popleft()
        if pos == destination:
            return count
        viz.add(pos)
        for i, n in enumerate(neighbors):
            new_pos = (pos[0] + n[0], pos[1] + n[1])
            if new_pos not in m or new_pos in viz:
                continue
            if m[new_pos] == '#':
                continue
            if m[pos] == '>' and i != 0:
                continue
            if m[pos] == '^' and i != 1:
                continue
            if m[pos] == '<' and i != 2:
                continue
            if m[pos] == 'v' and i != 3:
                continue
            q.append(new_pos)
        if len(q) == 0:
            return None
        if len(q) != 1:
            res1 = find_max_dist(q[0], deepcopy(viz))
            res2 = find_max_dist(q[1], deepcopy(viz))
            if res1 is None:
                res1 = -999
            if res2 is None:
                res2 = -999
            return 1 + max(count + res1, count + res2)
        else:
            count += 1

print(find_max_dist(source, set()))


# part 2
decision_points = []
for pos in m:
    if m[pos] == '#':
        continue
    count = 0
    for n in neighbors:
        new_pos = (pos[0] + n[0], pos[1] + n[1])
        if new_pos not in m:
            continue
        if m[new_pos] != '#':
            count += 1
    if count > 2:
        decision_points.append(pos)
decision_points.append(source)
decision_points.append(destination)

def find_dist(start, destination):
    pos = start
    q = collections.deque()
    viz = set()
    q.append((start, 0))
    while q:
        pos, dist = q.popleft()
        viz.add(pos)
        if pos == destination:
            return dist
        for n in neighbors:
            new_pos = (pos[0] + n[0], pos[1] + n[1])
            if new_pos not in m or new_pos in viz or m[new_pos] == '#' or new_pos in decision_points and new_pos != destination:
                continue
            q.append((new_pos, dist + 1))

network = {}
for s in decision_points:
    for d in decision_points:
        if s == d:
            continue
        x = find_dist(s,d) 
        if x is not None:
            network[(s,d)] = x 

distance_between_decisions = collections.defaultdict(list)
for n in network:
    start, end = n
    dist = network[n]
    if (end, dist) not in distance_between_decisions[start]:
        distance_between_decisions[start].append((end, dist))
    if (start, dist) not in distance_between_decisions[end]:
        distance_between_decisions[end].append((start, dist))

viz = set()

count = 0
ans = 0

def dfs(v, d):
    global ans
    if v in viz:
        return
    viz.add(v)
    if v == destination:
        ans = max(ans, d)
    for (y, yd) in distance_between_decisions[v]:
        dfs(y, d+yd)
    viz.remove(v)

dfs(source, 0)
print(ans)
