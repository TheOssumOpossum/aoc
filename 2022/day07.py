import sys
import re

day = '07'
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

lines = f.read().splitlines()

# #part 1
# m = {}
# root=True
# dirstack = []
# for line in lines:
#     l = line.strip()
#     if '$ cd' in l:
#         if '/' in l:
#             # dir = '/'
#             dirstack = ['/']
#             m[dirstack[-1]] = ([],0,'')
#         elif '..' in l:
#             # dir = m[dir][2]
#             dirstack.pop()
#             # print(dir)
#         else:
#             _, dir = re.findall("\w+",l)

#             ddd = ''
#             for dddd in dirstack:
#                 ddd += dddd
#             dirstack.append(dir)
#             # print(dir)
#             m[ddd+dir] = ([],0,ddd)
#     elif 'dir ' in l:
#         _, child = re.findall("\w+",l)
#         ddd = ''
#         for dddd in dirstack:
#             ddd += dddd
#         m[ddd][0].append(ddd+child)
#     elif l[0].isnumeric():
#         size = re.findall("\d+",l)
#         file = re.findall("[\w.]+",l)
#         ddd = ''
#         for dddd in dirstack:
#             ddd += dddd
#         m[ddd] = (m[ddd][0], m[ddd][1] + int(size[0]), m[ddd][2])

# print(m)
# ss = 0
# for d in m:
#     s = 0
#     s += m[d][1]
#     q = m[d][0]
#     while len(q) > 0:
#         dd = q.pop(0)
#         s += m[dd][1]
#         q += m[dd][0]
#     # print(d,s)
#     if s <= 100000:
#         ss += s
# print(ss)

#part 2
m = {}
root=True
dirstack = []
for line in lines:
    l = line.strip()
    if '$ cd' in l:
        if '/' in l:
            # dir = '/'
            dirstack = ['/']
            m[dirstack[-1]] = ([],0,'')
        elif '..' in l:
            # dir = m[dir][2]
            dirstack.pop()
            # print(dir)
        else:
            _, dir = re.findall("\w+",l)

            ddd = ''
            for dddd in dirstack:
                ddd += dddd
            dirstack.append(dir)
            # print(dir)
            m[ddd+dir] = ([],0,ddd)
    elif 'dir ' in l:
        _, child = re.findall("\w+",l)
        ddd = ''
        for dddd in dirstack:
            ddd += dddd
        m[ddd][0].append(ddd+child)
    elif l[0].isnumeric():
        size = re.findall("\d+",l)
        file = re.findall("[\w.]+",l)
        ddd = ''
        for dddd in dirstack:
            ddd += dddd
        m[ddd] = (m[ddd][0], m[ddd][1] + int(size[0]), m[ddd][2])

ss = 0
mm = {}
for d in m:
    s = 0
    s += m[d][1]
    q = m[d][0]
    while len(q) > 0:
        dd = q.pop(0)
        s += m[dd][1]
        q += m[dd][0]
    # print(d,s)
    if s <= 100000:
        ss += s
    mm[d] = s

total  = 70000000
need = 30000000
print(mm['/'])
unused = total - mm['/']
print(unused)
deleteneed = 30000000-unused
print(deleteneed)
minny=float('inf')
for ddddd in mm:
    if mm[ddddd] > deleteneed and mm[ddddd] < minny:
        minny = mm[ddddd]
print(minny)
