import sys
import re
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

inp = ''
for l in lines:
    inp += l
                    
s = 0
muls = re.findall('mul\((\d+),(\d+)\)', inp)
for a, b in muls:
    s += int(a) * int(b)
print(s)

ss = 0
dos = re.split('do\(\)', inp)
for d in dos:
    do = re.split('don\'t\(\)', d)[0]
    muls = re.findall('mul\((\d+),(\d+)\)', do)
    for a, b in muls:
        ss += int(a) * int(b)
print(ss)
