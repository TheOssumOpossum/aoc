import sys
from collections import Counter
import re
sys.path.append('../..')
lines, groups = read(__file__)
from lib.everybody_codes_read import read

#p1
c = Counter(lines[0])

s = 0
s += 1*c.get('B')
s += 3*c.get('C')
print(s)

#p2
combats = re.findall('(\w)(\w)', lines[0])

m = {'x': 0, 'A':0, 'B': 1, 'C':3, 'D':5}
s = 0
for a, b in combats:
    s += m[a]
    s += m[b]
    if a != 'x' and b != 'x':
        s += 2
print(s)

#p3
combats = re.findall('(\w)(\w)(\w)', lines[0])

m = {'x': 0, 'A':0, 'B': 1, 'C':3, 'D':5}
s = 0
for a, b, c in combats:
    s += m[a]
    s += m[b]
    s += m[c]
    xs = 0
    if a == 'x':
        xs += 1
    if b == 'x':
        xs += 1
    if c == 'x':
        xs += 1
    if xs == 1:
        s += 2
    if xs == 0:
        s += 6
print(s)
