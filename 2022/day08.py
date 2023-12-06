import sys
import re

day = '08'
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

lines = f.read().splitlines()

#part 1
# m = {}
# r = -1
# for line in lines:
#     l = line.strip()
#     r += 1
#     c = 0
#     for a in l:
#         if r not in m:
#             m[r] = []
#         m[r].append(a)
# print(m)
# s = 0
# for i in range(len(m)):
#     for j in range(len(m[0])):
#         height = m[i][j]
#         visible = False
#         v1 = v2 = v3 = v4 = True
#         if i == 0 or j == 0 or i == len(m)-1 or j == len(m[0])-1:
#             s +=  1
#             continue
#         for a in range(0,i):
#             if m[a][j] >= height:
#                 v1 = False
#                 break
#         for a in range(i+1,len(m)):
#             if m[a][j] >= height:
#                 v2 = False
#                 break
#         for a in range(0,j):
#             if m[i][a] >= height:
#                 v3 = False
#                 break
#         for a in range(j+1, len(m[0])):
#             if m[i][a] >= height:
#                 v4 = False
#         if v1 or v2 or v3 or v4:
#             s += 1
#         print(v1 or v2 or v3 or v4, i,j)
# print(s)

#part 2
m = {}
r = -1
for line in lines:
    l = line.strip()
    r += 1
    c = 0
    for a in l:
        if r not in m:
            m[r] = []
        m[r].append(a)

s = 0
for i in range(1,len(m)-1):
    for j in range(1,len(m[0])-1):
        height = m[i][j]
        v1 = v2 = v3 = v4 = 0
        # if i == 0 or j == 0 or i == len(m)-1 or j == len(m[0])-1:
        #     s +=  1
        #     continue
        for a in range(i-1,-1,-1):
            v1 += 1
            if m[a][j] >= height:
                break
        for a in range(i+1,len(m)):
            v2 += 1
            if m[a][j] >= height:
                break
        for a in range(j-1,-1,-1):
            v3 += 1
            if m[i][a] >= height:
                break
        for a in range(j+1, len(m[0])):
            v4 += 1
            if m[i][a] >= height:
                break
        ss = v1 * v2 * v3 * v4
        s = max(ss, s)
print(s)
