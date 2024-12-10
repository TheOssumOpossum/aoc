import sys
import collections
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

directions = [(0,1),(-1,0),(0,-1),(1,0)] # right, up, left, down
m = {}
s = 0
ss = 0

# Grid Parser
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        m[(i,j)] = int(char)

for start in m:
    if m[start] != 0:
        continue
    for p2 in [False, True]:
        q = collections.deque([start])
        score = 0
        viz = set([start])
        while q:
            pos = q.popleft()
            if m[pos] == 9:
                score += 1
                continue
            for d in directions:
                new_pos = (pos[0] + d[0], pos[1] + d[1])
                if new_pos in m and m[new_pos] - m[pos] == 1 and (p2 or new_pos not in viz):
                    viz.add(new_pos)
                    q.append(new_pos)
        if p2:
            ss += score
        else:
            s += score
                 
print(s)
print(ss)
