import os
import sys
import re
import collections
from copy import deepcopy

f = open(f'{f"{os.path.dirname(os.path.realpath(__file__))}/../input/{os.path.dirname(os.path.realpath(__file__))[-4:]}/" if (len(sys.argv) >= 2 and sys.argv[1] == "1") else f"{os.path.dirname(os.path.realpath(__file__))}/"}{os.path.split(os.path.realpath(__file__))[1][3:5]}_{"data" if (len(sys.argv) >= 2 and sys.argv[1] == "1") else "sample" if len(sys.argv) < 2 or sys.argv[1] == "0" else "sample" + sys.argv[1]}.txt')
txt = f.read().strip()
lines = txt.split('\n')

s = 0
for i, line in enumerate(lines):
    name = re.match("[a-z-]+", line)[0][:-1]
    id = int(re.findall("\d+", line)[0])
    checksum = re.findall("\[[a-z]+", line)[0][1:]
    # print(name, id, checksum)
    name2 = name.replace('-','')
    c = collections.Counter(name2)
    letters = list(c.items())
    letters = sorted(letters, key=lambda x: (-x[1], x[0]))
    for i, j in enumerate(checksum):
        if j != letters[i][0]:
            break
    else:
        s += id
    name3 = ""
    for c in name:
        if c == '-':
            name3 += ' '
        else:
            x = ord(c)
            x -= ord('a')
            x += id
            x %= 26
            x += ord('a')
            name3 += chr(x)
    #print(name3)
    if 'north' in name3:
        print(name3, id)
print(s)