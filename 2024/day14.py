import sys
import re
import collections
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

directions = [(0,1),(-1,0),(0,-1),(1,0)] # right, up, left, down
directions_map = {y:directions[x] for x,y in enumerate('RULD')}
m = {}
viz = set()
s = 0
ss = 0

# Line Parser
for i, line in enumerate(lines):
    px, py, vx, vy = [int(x) for x in re.findall('-?\d+', line)]
    m[i] = (px, py, vx, vy)
        
x_max = 101
y_max = 103
for step in range(20_000):
    mm = collections.defaultdict(int)
    for r in m:
        px, py, vx, vy = m[r]
        mm[(px, py)] += 1
    
    connection_score = 0
    for a in list(mm):
        px, py = a
        for d in [(1,0),(0,1),(-1,0),(0,-1)]:
            pos = (px + d[0], py + d[1])
            if mm[pos] > 0:
                connection_score +=1
    if connection_score > 400:
        print(step, connection_score)    
        for y in range(y_max):
            for x in range(x_max):
                pop = 0
                for r in m:
                    px, py, vx, vy = m[r]
                    if px == x and py == y:
                        pop += 1
                print(pop if pop > 0 else '.', end='')
            print('')
        print('')
        print(step)
        break
        
    if step == 100:
        q1 = q2 = q3 = q4 = 0
        for i in m:
            px, py, vx, vy = m[i]
            if px == (x_max-1)//2 or py == (y_max-1)//2:
                continue
            if px < x_max/2:
                if py < y_max//2:
                    q1 += 1
                elif py > y_max//2:
                    q2 += 1
            elif px > x_max//2:
                if py < y_max//2:
                    q3 += 1
                elif py > y_max//2:
                    q4 += 1
        print(q1 * q2 * q3 * q4)

    for r in m:
        px, py, vx, vy = m[r]
        px += vx
        py += vy
        if px < 0:
            px += x_max
        if px >= x_max:
            px -= x_max
        if py < 0:
            py += y_max
        if py >= y_max:
            py -= y_max
        m[r] = (px, py, vx, vy)
