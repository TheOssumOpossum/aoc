import sys
import collections
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

directions = [(0,1),(-1,0),(0,-1),(1,0)] # right, up, left, down
directions_map = {int(y):directions[x] for x,y in enumerate('0123')}
m = {}

# Grid Parser
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        m[(i,j)] = char
        if char == 'S':
            start = (i,j)
        if char == 'E':
            end = (i,j)
            
dir = 0

q = collections.deque()
q.append((start, 0, 0)) # position, direction, score
min_score = collections.defaultdict(lambda: float('inf'))

while q:
    pos, dir, score = q.popleft()
    cur = (pos, dir)
    if min_score[cur] <= score:
        continue
    min_score[cur] = score
    new_pos = (pos[0] + directions_map[dir][0], pos[1] + directions_map[dir][1])
    if m[new_pos] != '#':
        q.append((new_pos, dir, score + 1))
    q.append((pos, (dir+1)%4, score + 1000))
    q.append((pos, (dir-1)%4, score + 1000))

x = [min_score[(end, d)] for d in range(4)]
p1 = min(x)
min_d = x.index(p1)
print('p1', p1)

# the example input thankfully has less than 1000 steps, otherwise just increase the multiplication factor
steps = p1 % 1000
turns = p1 // 1000
# print(steps, turns)
seat = set()

import copy
def dfs(pos, steps, turns, dir=0, viz=set()):
    viz.add(pos)
    if pos == start:
        for v in viz:
            seat.add(v)
        return
    elif steps == 0:
        return
    new_pos = (pos[0] + directions_map[dir][0], pos[1] + directions_map[dir][1])
    score_diff = min_score[(pos, (dir+2)%4)] - min_score[(new_pos, (dir+2)%4)]
    if m[new_pos] != '#' and new_pos not in viz and score_diff == 1:
        dfs(new_pos, steps-1, turns, dir, copy.deepcopy(viz))

    if turns == 0:
        return
    
    rot1 = (dir+1)%4
    new_pos1 = (pos[0] + directions_map[rot1][0], pos[1] + directions_map[rot1][1])
    score_diff = min_score[(pos, (dir+2)%4)] - min_score[(new_pos1, (rot1+2)%4)]
    if m[new_pos1] != '#' and new_pos1 not in viz and score_diff == 1001:
        dfs(new_pos1, steps-1, turns-1, rot1, copy.deepcopy(viz))
    
    rot2 = (dir-1)%4
    new_pos2 = (pos[0] + directions_map[rot2][0], pos[1] + directions_map[rot2][1])
    score_diff = min_score[(pos, (dir+2)%4)] - min_score[(new_pos2, (rot2+2)%4)]
    
    if m[new_pos2] != '#' and new_pos2 not in viz and score_diff == 1001:
        dfs(new_pos2, steps-1, turns-1, rot2, copy.deepcopy(viz))
    
dfs(end, steps, turns, (min_d+2)%4)
print('p2', len(seat))
