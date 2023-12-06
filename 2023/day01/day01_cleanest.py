import sys

day = '01'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample2' if sys.argv[1] == '2' else 'sample'))
lines = f.read().strip().splitlines()

import re
#part 1
# s = 0
# for line in lines:
#     l = line.strip()
#     n = re.findall("\d",l)
#     s += int(n[0]) * 10 + int(n[-1])
# print(s)

#part 2
ss = 0
nums = ["one","two","three","four","five","six","seven","eight","nine"]
for line in lines:
    l = line.strip()
    x = re.findall("\d|one|two|three|four|five|six|seven|eight|nine",l)
    y = re.findall("d\|one|two|three|four|five|six|seven|eight|nine"[::-1],l[::-1])
    a = x[0]
    b = y[0]
    if a in "123456789":
        a = int(a)
    else:
        a = nums.index(a) + 1
    if b in "123456789":
        b = int(b)
    else:
        b = nums.index(b[::-1]) + 1
    ss += a*10 + int(b)
    
print(ss)
        