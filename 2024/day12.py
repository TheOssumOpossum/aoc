import sys
import collections
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

directions = [(0,1),(-1,0),(0,-1),(1,0)] # right, up, left, down
m = {}
viz = set()
s = 0
ss = 0

# Grid Parser
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        m[(i,j)] = char

regions = {}
for start in m:
    if start in viz:
        continue
    letter = m[start]
    q = collections.deque([start])
    region = set([start])
    while q:
        pos = q.popleft()
        for d in directions:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if new_pos in m and new_pos not in region and m[new_pos] == letter:
                q.append(new_pos)
                viz.add(new_pos)
                region.add(new_pos)
    regions[(start)] = (letter, region)

for r in regions:
    letter, region = regions[r]
    area = len(region)
    perimeter = 0
    edges = collections.defaultdict(set)
    for cell in region:
        neighbors = 0
        for i, d in enumerate(directions):
            neighbor = (cell[0] + d[0], cell[1] + d[1])
            if neighbor in region:
                neighbors += 1
            else:
                edges[i].add(neighbor)
        perimeter += 4 - neighbors
    total_sides = 0
    for d in edges:
        sides = 0
        x_values = collections.defaultdict(set)
        y_values = collections.defaultdict(set)
        for x, y in edges[d]:
            if d == 1 or d == 3: # common x values
                y_values[x].add(y)
            else: #common y values
                x_values[y].add(x)
        if d == 1 or d == 3:
            for x in y_values:
                for y in y_values[x]:
                    if y+1 in y_values[x]:
                        continue
                    else:
                        sides += 1
        else:
            for y in x_values:
                for x in x_values[y]:
                    if x+1 in x_values[y]:
                        continue
                    else:
                        sides += 1
        total_sides += sides
    s += area*perimeter
    ss += area*total_sides

print(s)
print(ss)
