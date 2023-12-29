import sys
import hashlib
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

# part 1
id = lines[0].strip()
s = ''
i = 0
while len(s) < 8:
    i += 1
    test = f'{id}{i}'
    r = hashlib.md5(test.encode('utf-8')).hexdigest()
    if r.startswith('00000'):
        print(r)
        s += r[5]
print(s)

# part 2
id = lines[0].strip()
d = {}
i = 0
while len(d.keys()) != 8:
    i += 1
    test = f'{id}{i}'
    r = hashlib.md5(test.encode('utf-8')).hexdigest()
    if r.startswith('00000'):
        pos = r[5]
        char = r[6]
        if pos.isnumeric() and 0 <= int(pos) <= 7 and int(pos) not in d:
            print(r)
            d[int(pos)] = char
            
s = ''
for i in '01234567':
    s += d[int(i)]
print(s)
            
    
