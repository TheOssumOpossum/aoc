import sys
import re
import collections

day = '03'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample2' if sys.argv[1] == '2' else 'sample'))
lines = f.read().strip().splitlines()

# part 1
# s = 0
# for i, line in enumerate(lines):
#     l = line.strip()
#     n = 0
#     counts = False
#     for j, c in enumerate(l):
#         if c.isdigit():
#             n = n*10 + int(c)
#             for ii in [-1, 0, 1]:
#                 for jj in [-1, 0, 1]:
#                     if ii+i >= 0 and ii+i < len(lines) and jj+j >= 0 and jj+j < len(l):
#                         cc = lines[i+ii][j+jj]
#                         if cc != '.' and not cc.isdigit() and not counts:
#                             counts = True
#         if not c.isdigit():
#             if counts:
#                 s += n
#                 counts = False
#             n = 0
#     if counts:
#         s += n
#         counts = False
#         n = 0
# print(s)

# part 2
s = 0
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
                    if ii+i >= 0 and ii+i < len(lines) and jj+j >= 0 and jj+j < len(l):
                        cc = lines[i+ii][j+jj]
                        if cc != '.' and not cc.isdigit():
                            if cc == '*':
                                gear = (i+ii,j+jj)
                            counts = True
        if not c.isdigit():
            if counts and not gear:
                counts = False
            if gear:
                gears[gear].append(n)
                if len(gears[gear]) == 2:
                    s += n*gears[gear][0]
                gear = False
            n = 0
    if counts:
        if counts and not gear:
            counts = False
        if gear:
            gears[gear].append(n)
            if len(gears[gear]) == 2:
                s += n*gears[gear][0]
        n = 0

print(s)
        
    