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

#part 2
ss = 0
for line in lines:
    l = line.strip()
    a = 0
    b = 0
    for i in range(len(l)):
        c = l[i]
        x = re.findall("\d",c)
        if len(x) > 0:
            a = int(x[0])
            break
        if c == "o" and l[i:i+3] == "one":
            a = 1
            break
        if c == "t" and l[i:i+3] == "two":
            a = 2
            break
        if c == "s" and l[i:i+3] == "six":
            a = 6
            break
        if c == "f" and l[i:i+4] == "four":
            a = 4
            break
        if c == "n" and l[i:i+4] == "nine":
            a = 9
            break
        if c == "f" and l[i:i+4] == "five":
            a = 5
            break
        if c == "t" and l[i:i+5] == "three":
            a = 3
            break
        if c == "s" and l[i:i+5] == "seven":
            a = 7
            break
        if c == "e" and l[i:i+5] == "eight":
            a = 8
            break
    # print(a)
    for i in range(len(l[::-1])):
        c = l[::-1][i]
        x = re.findall("\d",c)
        if len(x) > 0:
            b = int(x[0])
            break
        if c == "e" and l[::-1][i:i+3] == "one"[::-1]:
            b = 1
            break
        if c == "o" and l[::-1][i:i+3] == "two"[::-1]:
            b = 2
            break
        if c == "x" and l[::-1][i:i+3] == "six"[::-1]:
            b = 6
            break
        if c == "r" and l[::-1][i:i+4] == "four"[::-1]:
            b = 4
            break
        # print(l[::-1][i:i+4], "nine"[::-1], c)
        if c == "e" and l[::-1][i:i+4] == "nine"[::-1]:
            b = 9
            break
        if c == "e" and l[::-1][i:i+4] == "five"[::-1]:
            b = 5
            break
        if c == "e" and l[::-1][i:i+5] == "three"[::-1]:
            b = 3
            break
        if c == "n" and l[::-1][i:i+5] == "seven"[::-1]:
            b = 7
            break
        if c == "t" and l[::-1][i:i+5] == "eight"[::-1]:
            b = 8
            break
    ss += a*10 + b
    
    
print(ss)
        