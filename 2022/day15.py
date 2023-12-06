import sys
import re

day = 15
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

lines = f.read().splitlines()

# #part 1
# m = set()
# b = set()
# y = 2000000 if not sample else 10

# for line in lines:
#     print(line)
#     l = line.strip()
#     x1, y1, x2, y2 = [int(x) for x in re.findall('\d+',l)]
#     b.add((x2,y2))
#     dist = abs(x1-x2) + abs(y1-y2)
#     for j in range(y1-dist,y1+dist+1):
#         if j != y:
#             continue
#         for i in range(x1-dist,x1+dist+1):
#             if abs(x1-i) + abs(y1-j) <= dist:
#                 if (i,j) not in b:
#                     m.add((i,j))

# s = 0
# for i in m:
#     # print(i)
#     if i[1] == y:
#         s += 1
# print(s)

# part 2
m = {}
b = set()
sss = set()

xx = -1
r = 20 if sample else 4000000
for line in lines:
    xx += 1
    l = line.strip()
    x1, y1, x2, y2 = [int(x) for x in re.findall('[-\d]+',l)]
    b.add((x2, y2))
    sss.add((x1, y1))
    
    print(line)

    dist = abs(x1-x2) + abs(y1-y2)

    start = x1-dist
    end = x1+dist
    
    for i in range(start,end+1):
        if i < 0 or i > r:
            continue
        ll = dist - abs(i-x1)
        if i not in m:
            m[i] = []
        m[i].append([max(0,y1-ll), min(y1 + ll, r)])

def mergeRanges(rs):
    i = -1
    while i < len(rs)-2:
        i += 1
        start = rs[i][0]
        end = rs[i][1]
        next_start = rs[i+1][0]
        next_end = rs[i+1][1]
        if end < next_start-1:
            continue
        elif next_start-1 <= end or end <= next_end+1:
            rs[i][0] = min(start, next_start)
            rs[i][1] = max(end, next_end)
            del rs[i+1]
            i -= 1
            continue
    return rs

print('merging')
mm={}
for i in m:
    mmm = mergeRanges(sorted(list(m[i])))
    if i < 0:
        continue
    if i > r:
        continue
    mm[i] = mmm
print('merged')

y = -1
x = -1
for i in range(r):
    if len(mm[i]) > 1:
        y = mm[i][0][1] + 1
        x = i
        break
print('x,y,',x,y)
print('result=', x*4000000+y)
