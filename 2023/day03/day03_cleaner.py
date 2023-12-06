import sys
import re
import collections

day = '03'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample2' if sys.argv[1] == '2' else 'sample'))
lines = f.read().strip().splitlines()

# part 1 and 2
s = 0
ss = 0
gears = collections.defaultdict(list)
for i, line in enumerate(lines):
    l = line.strip()
    n = 0
    counts = False
    gear = False
    for j, c in enumerate(l):
        if c.isdigit():
            n = n*10 + int(c)
            for ii in [-1, 0, 1]:
                for jj in [-1, 0, 1]:
                    try:
                        cc = lines[i+ii][j+jj]
                        if cc != '.' and not cc.isdigit():
                            counts = True
                            if cc == '*':
                                gear = (i+ii,j+jj)
                    except IndexError:
                        continue
        if not c.isdigit() or j == len(l)-1:
            if counts:
                s += n
                counts = False
            if gear:
                gears[gear].append(n)
                if len(gears[gear]) == 2:
                    ss += n*gears[gear][0]
                gear = False
            n = 0

print(s)
print(ss)
        
    