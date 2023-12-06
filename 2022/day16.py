import sys
import re
import copy

day = 16
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

lines = f.read().splitlines()

#part 1
# x = {}
# start = 'AA'
# for line in lines:
#     l = line.strip()
#     f =  re.findall("\d+", l)[0]
#     f = int(f)
#     z = l.split("to valve")
#     n = []
#     v = l[6:8]
#     for i in z:
#         if len(i) > 30:
#             continue
#         n = re.findall("\w\w", i)
#     x[v] = (f, n)
# print(x)
# print('')
# def shortestPath(fromm, too):
#     global x
#     viz = {}
#     dist = 0
#     viz[fromm] = dist
#     q = [fromm]
#     a = fromm
#     while len(q) > 0:
#         a = q.pop(0)
#         dist = viz[a]
#         if a == too:
#             break
#         for j in x[a][1]:
#             if j == too:
#                 return dist + 1
#             if j not in viz:
#                 q.append(j)
#                 viz[j] = dist + 1
#     return dist

# g = {}
# valves = []
# for i in x:
#     if x[i][0] > 0:
#         valves.append(i)

# for i in valves + [start]:
#     n = []
#     for j in valves:
#         if i == j:
#             continue
#         n.append((j, shortestPath(i,j)))
#     g[i] = (x[i][0], n)

# for i in sorted(list(g)):
#     print(i, g[i])
# print('')

# memo = {}
# sys.setrecursionlimit(500000)
# def mx(v, mins=30, f=0, vs='', p=''):
#     global memo
#     global g
#     if vs in memo:
#         return memo[vs]
#     if mins <= 1:
#         return (f, p)
#     flow = (mins-1)*g[v][0]
#     res = []
#     if v not in vs and v != start:
#         vv = copy.deepcopy(vs)
#         vv += v
#         return mx(v, mins-1, f+flow, vv, p + 'min{} open {} for flow={} total={}, '.format(mins, v, flow, f+flow))
#     for i in g[v][1]:
#         if i[0] in vs or mins-i[1] < 1:
#             continue
#         vv = copy.deepcopy(vs)
#         res.append(mx(i[0], mins-i[1], f, vv, p + 'min{} goto {} costs={}min, '.format(mins, i[0],i[1])))
#     if len(res) == 0:
#         vv = copy.deepcopy(vs)
#         memo[vv] = (f, p)
#         return (f, p)
#     vv = copy.deepcopy(vs)
#     memo[vv] = max(res)
#     return max(res)
# print(mx(start))

#part 2
x = {}
start = 'AA'
for line in lines:
    l = line.strip()
    f = re.search("\d+", l).group(0)
    v, *n = re.findall("[A-Z]{2}", l)
    x[v] = (f, n)
print(x)
print('')
def shortestPath(fromm, too):
    global x
    viz = {}
    dist = 0
    viz[fromm] = dist
    q = [fromm]
    a = fromm
    while len(q) > 0:
        a = q.pop(0)
        dist = viz[a]
        if a == too:
            break
        for j in x[a][1]:
            if j == too:
                return dist + 1
            if j not in viz:
                q.append(j)
                viz[j] = dist + 1
    return dist

g = {}
valves = []
for i in x:
    if x[i][0] > 0:
        valves.append(i)

for i in valves + [start]:
    n = {}
    for j in valves:
        if i == j:
            continue
        n[j] = shortestPath(i,j)
    g[i] = (x[i][0], n)

for i in sorted(list(g)):
    print(i, g[i])
print('')

memo = set()
sys.setrecursionlimit(500000)

from collections import deque

mins = 26
q = deque([(start, mins, start, mins, set(), 0)])
max_total = 0
while q:
    me, memins, you, youmins, open, total = q.popleft()
    if (tuple(sorted(open)), total) in memo:
        continue
    memo.add((tuple(sorted(open)), total))

    move = False
    for i in g:
        if i in open or i == start:
            continue
        time_left = memins - g[me][1][i]
        if time_left >= 2:
            move = True
            flow = (time_left -1) * g[i][0]
            q.append((i, time_left - 1, you, youmins, open.union(set([i])), total + flow))
        time_left = youmins - g[you][1][i]
        if time_left >= 2:
            move = True
            flow = (time_left -1) * g[i][0]
            q.append((me, memins, i, time_left-1, open.union(set([i])), total + flow))

    if not move:
        max_total = max(total, max_total)
print(max_total)
