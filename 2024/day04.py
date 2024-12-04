import sys
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

directions = [(0,1),(-1,0),(0,-1),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
directions2 = [(1,1),(-1,-1),(-1,1),(1,-1)]
m = {}
s = 0
ss = 0

# Grid Parser
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        m[(i,j)] = char

for start in m:
    if m[start] == 'X':
        for d in directions:
            pos = start
            for i in range(3):
                pos = (pos[0] + d[0], pos[1] + d[1])
                if pos not in m:
                    break
                if i == 0 and m[pos] != 'M':
                    break
                elif i == 1 and m[pos] != 'A':
                    break
                elif i == 2 and m[pos] == 'S':
                    s += 1

for start in m:
    m_count = 0
    s_count = 0
    if m[start] == 'A':
        tl = None
        br = None
        for d in directions2:
            pos = (start[0] + d[0], start[1] + d[1])
            if pos not in m:
                break
            if m[pos] == 'M':
                m_count += 1
            elif m[pos] == 'S':
                s_count += 1
            if d == (1,1):
                tl = m[pos]
            if d == (-1,-1):
                br = m[pos]
        if m_count == 2 and s_count == 2 and tl != br:
            ss += 1        

print(s)
print(ss)
