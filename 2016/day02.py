import sys
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

#part 1
directions = [(0,1),(-1,0),(0,-1),(1,0)]
directions_map = {y:directions[x] for x,y in enumerate('RULD')}
m = {}
s = ''
x = y = 1
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        x += directions_map[char][0]
        y += directions_map[char][1]
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if x > 2:
            x = 2
        if y > 2:
            y = 2
    s += str(x*3+y+1)
print(s)

#part 2
m[(0, 2)] = '1'
for i, j in enumerate('234'):
    m[(1, i+1)] = j
for i, j in enumerate('56789'):
    m[(2, i)] = j
for i, j in enumerate('ABC'):
    m[(3, i+1)] = j
m[(4, 2)] = 'D'

x = 2
y = 0
s = ''
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        new_x = x + directions_map[char][0]
        new_y = y + directions_map[char][1]
        if (new_x, new_y) in m:
            x,y = new_x, new_y
    s += m[(x,y)]
print(s)
