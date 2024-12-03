import sys
import re
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

inp = ''
for l in lines:
    inp += l
                    
s = 0
muls = re.findall('mul\(\d+,\d+\)', inp)
for mul in muls:
    a,b = re.findall('\d+', mul)
    s += int(a) * int(b)
print(s)

ss = 0
dos = re.split('do\(\)', inp)
for d in dos:
    muls = re.split('don\'t\(\)', d)
    muls = re.findall('mul\(\d+,\d+\)', muls[0])
    for mul in muls:
        a,b = re.findall('\d+', mul)
        ss += int(a) * int(b)
print(ss)
