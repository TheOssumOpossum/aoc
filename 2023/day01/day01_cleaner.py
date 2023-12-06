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
for line in lines:
    l = line.strip()
    x = re.findall("\d|one|two|three|four|five|six|seven|eight|nine",l)
    y = re.findall("d\|one|two|three|four|five|six|seven|eight|nine"[::-1],l[::-1])
    a = x[0]
    b = y[0]
    if a in "123456789":
        a = int(a)
    if b in "123456789":
        b = int(b)
    if a == "one":
        a = 1
    if a == "two":
        a = 2
    if a == "three":
        a = 3
    if a == "four":
        a = 4
    if a == "five":
        a = 5
    if a == "six":
        a = 6
    if a == "seven":
        a = 7
    if a == "eight":
        a = 8
    if a == "nine":
        a = 9
    if b == "one"[::-1]:
        b = 1
    if b == "two"[::-1]:
        b = 2
    if b == "three"[::-1]:
        b = 3
    if b == "four"[::-1]:
        b = 4
    if b == "five"[::-1]:
        b = 5
    if b == "six"[::-1]:
        b = 6
    if b == "seven"[::-1]:
        b = 7
    if b == "eight"[::-1]:
        b = 8
    if b == "nine"[::-1]:
        b = 9
    ss += a*10 + int(b)

print(ss)
