import sys
import collections
from copy import deepcopy

day = '14'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip().splitlines()

s = 0
m = collections.defaultdict(int)
for i, line in enumerate(lines):
    l = line.strip()
    for j, c in enumerate(l):
        m[(i,j)] = c
        
def calc(m, cycles=1000000000):
    states = {}
    vals = {}
    cycle_length = 0
    def move(i,j,vertical=-1,horizontal=0):
        if m[(i+vertical,j+horizontal)] == '.':
            m[(i,j)] = '.'
            m[(i+vertical,j+horizontal)] = 'O'
            move(i+vertical,j+horizontal, vertical, horizontal)
    for ii in range(cycles):
        for j in range(len(lines[0])):
            for i in range(len(lines)):
                if m[(i,j)] == 'O':
                    move(i,j)
        if cycles != 1:
            for i in range(len(lines)):
                for j in range(len(lines[0])):
                    if m[(i,j)] == 'O':
                        move(i,j,0,-1)
            for j in range(len(lines[0])):
                for i in range(len(lines)-1,-1,-1):
                    if m[(i,j)] == 'O':
                        move(i,j,1)
            for i in range(len(lines)):
                for j in range(len(lines[0])-1,-1,-1):
                    if m[(i,j)] == 'O':
                        move(i,j,0,1)
        s = 0
        state = ''
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if m[(i,j)] == 'O':
                    s += len(lines) - i
                state += m[(i,j)]
        
        if state in states:
            cycle_length = ii - states[state]
            offset = states[state] - 1
            return vals[((1000000000-offset)%cycle_length)+offset-1]
        else:
            states[state] = ii
            vals[ii] = s
    return s

from copy import deepcopy
print(calc(deepcopy(m),1))
print(calc(deepcopy(m)))
