import sys
import collections

day = '16'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip().splitlines()

g = collections.defaultdict(list)
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        g[row].append((char, False))

direction = [(0,1),(-1,0),(0,-1),(1,0)] 

def move(pos, d):
    row, col = pos
    d %= 4
    return (row+direction[d][0], col+direction[d][1])

def config(g, pos=(0,0),d=0):
    
    def addToQueue(d):
        q.append((move(pos, d), d))

    viz = set()
    q = collections.deque()
    q.append((pos, d))
    while len(q):
        pos, d = q.popleft()
        d %=4
        row, col = pos
        if row<0 or row >= len(lines) or col < 0 or col >= len(lines[0]) or (row, col,d) in viz:
            continue
        viz.add((row, col, d))
        cell = g[row][col]
        char, _ = cell
        g[row][col] = (char, True)
        match char:
            case '.':
                addToQueue(d)
            case '-':
                if d%2 == 0:
                    addToQueue(d)
                else:
                    addToQueue(d+1)
                    addToQueue(d-1)
            case '|':
                if d%2:
                    addToQueue(d)
                else:
                    addToQueue(d+1)
                    addToQueue(d-1)
            case '\\':
                #2=>1 1=>2
                addToQueue(d + (1 if d%2 else -1))
            case '/':
                #0=>1 1=>0
                addToQueue(d - (1 if d%2 else -1))
                    
    s = 0
    for row in g:
         for col in g[row]:
              s += 1 if col[1] else 0
    return s
                    
from copy import deepcopy
print(config(deepcopy(g)))

config_max = 0
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if row == 0:
            config_max = max(config_max, config(deepcopy(g),(row,col), 3))
        if col == 0:
            config_max = max(config_max, config(deepcopy(g),(row, col), 0))
        if row == len(lines)-1:
            config_max = max(config_max, config(deepcopy(g),(row, col), 1))
        if col == len(lines[0])-1:
            config_max = max(config_max, config(deepcopy(g),(row, col), 2))
print(config_max) 
