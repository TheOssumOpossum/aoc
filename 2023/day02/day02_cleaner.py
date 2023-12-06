import sys
import re
import collections

day = '02'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample2' if sys.argv[1] == '2' else 'sample'))
lines = f.read().strip().splitlines()

#part 1
games = 0
s = 0
for g, line in enumerate(lines):
    g += 1
    games += g
    l = line.strip()
    x = re.findall("\d+|\w+|;",l)[2:]
    m = collections.defaultdict(int)
    for i, a in enumerate(x):
        if a == ';':
            m = collections.defaultdict(int)
        else:
            if a.isnumeric():
                color = x[i+1]
                m[color] = int(a) + m[color]
            if m['red'] > 12 or m['green'] > 13 or m['blue'] > 14:
                s += g
                break
print(games-s) 

#part 2
s = 0
for line in lines:
    l = line.strip()
    x = re.findall("\d+|\w+|;",l)[2:]
    m = collections.defaultdict(int)
    mx = collections.defaultdict(int)
    for i, a in enumerate(x):
        if a == ';':
            m = collections.defaultdict(int)
        else:
            if a.isnumeric():
                color = x[i+1]
                m[color] = int(a) + m[color]
            mx[color] = max(m[color],mx[color])
    xx = list(mx.values())
    s += xx[0] * xx[1] * xx[2]
print(s) 
