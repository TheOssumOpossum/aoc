import sys
import os

# print(os.path.split(os.path.realpath(__file__))[1][3:5])
f = open(f'{f"../input/{os.path.dirname(os.path.realpath(__file__))[-4:]}/" if (len(sys.argv) >= 2 and sys.argv[1] == "1") else ""}{os.path.split(os.path.realpath(__file__))[1][3:5]}_{"data" if (len(sys.argv) >= 2 and sys.argv[1] == "1") else "sample" if len(sys.argv) < 2 or sys.argv[1] == "0" else "sample" + sys.argv[1]}.txt')
txt = f.read().strip()
lines = txt.split('\n')

#part 1 and 2
directions = [(0,1),(-1,0),(0,-1),(1,0)]
directions_map = {y:directions[x] for x,y in enumerate('RULD')}
def solve(x,y,m):
    s = ''
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            new_x = x + directions_map[char][0]
            new_y = y + directions_map[char][1]
            if (new_x, new_y) in m:
                x,y = new_x, new_y
        s += m[(x,y)]
    print(s)

m = {}
m2 = {}
for i, j in enumerate('123456789'):
    m[(i//3, i%3)] = j
for i, j in enumerate('xx1xxx234x56789xABCxxxDxx'):
    m2[(i//5, i%5)] = j
for key, val in list(m2.items()):
    if val == 'x':
        del m2[key]

solve(1,1,m)
solve(2,0,m2)