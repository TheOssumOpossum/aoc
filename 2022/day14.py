import sys
import re

day = 14
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('day{}_{}.txt'.format(day, 'sample' if sample else 'data'))

lines = f.read().strip().splitlines()

# part 1
# m = {}
# max_y = 0
# for line in lines:
#     l = line.strip()
#     nums = re.findall('\d+',l)
#     i = 0
#     while i < len(nums)-2:
#         x1 = int(nums[i])
#         y1 = int(nums[i+1])
#         x2 = int(nums[i+2])
#         y2 = int(nums[i+3])
#         if x1 == x2:
#             for j in range(min(y1,y2),max(y1,y2)+1):
#                 m[(x1,j)] = '#'
#                 max_y = max(max_y, j)
#         else:
#             for j in range(min(x1,x2),max(x1,x2)+1):
#                 m[(j,y1)] = '#'
#                 max_y = max(max_y, y1)
#         i += 2
# print(max_y)

# x = 500
# y = 0
# while True:
#     m[(x,y)] = 'o'
#     if (x, y+1) not in m:
#         del m[(x,y)]
#         y += 1
#         continue
#     elif (x-1, y+1) not in m:
#         del m[(x,y)]
#         y += 1
#         x -= 1
#         continue
#     elif (x+1, y+1) not in m:
#         del m[(x,y)]
#         y += 1
#         x += 1
#         continue
#     else:
#         if y == max_y:
#             del m[(x,y)]
#         x = 500
#         y = 0
#         s = 0
#         for i in m:
#             if m[i] == 'o':
#                 s += 1
#         print(s)
#         # break
#         continue

# part 2

m = {}
max_y = 0
for line in lines:
    l = line.strip()
    nums = re.findall('\d+', l)
    i = 0
    while i < len(nums)-2:
        x1 = int(nums[i])
        y1 = int(nums[i+1])
        x2 = int(nums[i+2])
        y2 = int(nums[i+3])
        if x1 == x2:
            for j in range(min(y1, y2), max(y1, y2)+1):
                m[(x1, j)] = '#'
                max_y = max(max_y, j)
        else:
            for j in range(min(x1, x2), max(x1, x2)+1):
                m[(j, y1)] = '#'
                max_y = max(max_y, y1)
        i += 2
print(max_y)

x = 500
y = 0
s = 0
max_y = max_y + 2
for i in range(-1000, 1000):
    m[(i, max_y)] = '#'
while True:
    if (x, y+1) not in m:
        y += 1
        continue
    elif (x-1, y+1) not in m:
        y += 1
        x -= 1
        continue
    elif (x+1, y+1) not in m:
        y += 1
        x += 1
        continue
    else:
        if y != max_y:
            m[(x, y)] = 'o'
        else:
            break
        if x == 500 and y == 0:
            break
        x = 500
        y = 0
        s += 1
        continue
print(s)
