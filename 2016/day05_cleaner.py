import sys
import hashlib
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

# part 1 and 2
id = lines[0].strip()
d = {}
i = 0
s = ''
while len(d) != 8:
    i += 1
    test = f'{id}{i}'
    r = hashlib.md5(test.encode('utf-8')).hexdigest()
    if r.startswith('00000'):
        pos, char = r[5], r[6]
        if len(s) < 8:
            s += pos
        if not pos.isnumeric():
            continue
        pos = int(pos)
        if 0 <= pos <= 7 and pos not in d:
            d[pos] = char

print(s)
s = ''
for i in range(8):
    s += d[i]
print(s)
            
    
