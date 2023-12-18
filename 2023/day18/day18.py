import sys
import re
import collections
import functools

day = '18'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 2 else 'sample'))
file = f.read().strip()
lines = file.splitlines()
groups = file.split('\n\n')

# part 1
m = collections.defaultdict(str)
row = col = 0
directions = [(0,1),(-1,0),(0,-1),(1,0)]
m[(0,0)] = '#'
depth = -1
for i, line in enumerate(lines):
    l = line.strip()
    direction, num, code = l.split(' ')
    num = int(num)
    match direction:
        case 'U':
            for i in range(1, num+1):
                m[(row-i,col)] = '#'
            row -= num
        case 'D':
            for i in range(1, num+1):
                m[(row+i, col)] = '#'
            row += num
        case 'R':
            for i in range(1, num+1):
                m[(row,col+i)] = '#'
            col += num
        case 'L':
            for i in range(1, num+1):
                m[(row, col-i)] = '#'
            col -= num
    depth += num
q = collections.deque()
viz = set()
q.append((1,1))
while q:
    node = q.popleft()
    depth += 1
    for n in directions:
        neighbor = (node[0] + n[0], node[1] + n[1])
        if neighbor not in viz and m[neighbor] != '#':
            viz.add(neighbor)
            q.append(neighbor)
print(depth)

# part 2
row = col = 0
edge_length = 0
vertices = [(0,0)]
depth = -1
for i, line in enumerate(lines):
    l = line.strip()
    direction, num, code = l.split(' ')
    code = re.search('[0-9a-f]+',code)[0]
    num = int(str('0x'+code[:-1]), 16)
    match int(code[-1]):
        case 0:
            col += num
        case 1:
            row += num
        case 2:
            col -= num
        case 3:
            row -= num
    vertices.append((row,col))
    edge_length += num

for i, v in enumerate(vertices[:-1]):
    vv = vertices[(i+1)]
    depth += 0.5 * (v[1] + vv[1])*(v[0]-vv[0])
print(int(abs(depth)+edge_length/2))
