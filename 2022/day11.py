import sys
import re

day = 11
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

lines = f.read().splitlines()

#part 1
# ms = {}
# class Monkey:
#     def __init__(self,id):
#         self.m = id
#         self.i = []
#         self.o = []
#         self.d = -1
#         self.t = -1
#         self.f = -1
#         self.n = 0

#     def __repr__(self):
#         return str(self.i)

# m = Monkey(-1)
# for line in lines:
#     l = line.strip()
#     if "Monkey" in l:
#         m_ = re.findall("\d+",l)[0]
#         m_ = int(m_)
#         m = Monkey(m_)
#         ms[m_] = m
#     elif "Starting" in l:
#         s = re.findall("\d+",l)
#         ss = []
#         for i in s:
#             ss.append(int(i))
#         m.i = ss
#     elif "Operation" in l:
#         o = re.findall("[+*\d]+", l)
#         # print(line)
#         if len(o) == 1:
#             o.append('old')
#         m.o = o
#     elif "Test" in l:
#         d = re.findall("\d+",l)[0]
#         m.d = int(d)
#     elif "true" in l:
#         t = re.findall("\d+",l)[0]
#         m.t = int(t)
#     elif "false" in l:
#         f = re.findall("\d+",l)[0]
#         m.f = int(f)
#     else:
#         #newline
#         continue

# round = 0
# viz = set()
# while round < 20:
#     round += 1
#     for m_ in range(len(ms)):
#         m = ms[m_]
#         while len(m.i) > 0:
#             item = m.i.pop(0)
#             m.n += 1
#             n = item if m.o[1] == 'old' else int(m.o[1])
#             if m.o[0] == '*':
#                 item = item * n
#             else:
#                 item = item + n
#             # item = item // 3
#             if item % m.d == 0:
#                 ms[m.t].i.append(item)
#             else:
#                 ms[m.f].i.append(item)

# x = []
# for i in ms:
#     x.append(ms[i].n)
# x = sorted(x)
# print(x[-1] * x[-2])

#part 2
ms = {}
p = 1
class Monkey:
    def __init__(self,id):
        self.m = id
        self.i = []
        self.o = []
        self.d = -1
        self.t = -1
        self.f = -1
        self.n = 0

    def __repr__(self):
        return str(self.i)

for line in lines:
    l = line.strip()
    if "Monkey" in l:
        m_ = re.findall("\d+",l)[0]
        m_ = int(m_)
        m = Monkey(m_)
        ms[m_] = m
    elif "Starting" in l:
        s = re.findall("\d+",l)
        ss = []
        for i in s:
            ss.append(int(i))
        m.i = ss
    elif "Operation" in l:
        o = re.findall("[+*\d]+", l)
        # print(line)
        if len(o) == 1:
            o.append('old')
        # elif o[0] == '*':
        #     p *= int(o[1])
        m.o = o
    elif "Test" in l:
        d = re.findall("\d+",l)[0]
        m.d = int(d)
        p *= int(d)
    elif "true" in l:
        t = re.findall("\d+",l)[0]
        m.t = int(t)
    elif "false" in l:
        f = re.findall("\d+",l)[0]
        m.f = int(f)
    else:
        #newline
        continue

round = 0
viz = set()
while round < 10000:
    round += 1
    print(round)
    for m_ in range(len(ms)):
        m = ms[m_]
        while len(m.i) > 0:
            item = m.i.pop(0)
            m.n += 1
            n = item if m.o[1] == 'old' else int(m.o[1])
            if m.o[0] == '*':
                item = item * n
            else:
                item = item + n
            item = item % p
            if item % m.d == 0:
                ms[m.t].i.append(item)
            else:
                ms[m.f].i.append(item)

x = []
for i in ms:
    x.append(ms[i].n)
x = sorted(x)
print(x[-1] * x[-2])
