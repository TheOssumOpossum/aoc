import sys

day = 12
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

lines = f.read().splitlines()

#part 1
# grid = {}
# h = 0
# for i in range(len(lines)):
#     l = lines[i].strip()
#     if l == '':
#         continue
#     h += 1
#     for j in range(len(l)):
#         if lines[i][j] == 'S':
#             start = (i,j)
#             grid[(i,j)] = 'a'
#         elif lines[i][j] == 'E':
#             end = (i,j)
#             grid[(i,j)] = 'z'
#         else:
#             grid[(i,j)] = lines[i][j]

# w = len(lines[0])
# q = [start]
# viz = {}
# viz[start] = 0
# while len(q) > 0:
#     a = q.pop(0)
#     a1 = (a[0] + 1, a[1])
#     a2 = (a[0] - 1, a[1])
#     a3 = (a[0], a[1] + 1)
#     a4 = (a[0], a[1] - 1)
#     dist = viz[a]
#     for i in [a1, a2, a3, a4]:
#         if i[0] < 0 or i[0] >= h or i[1] < 0 or i[1] >= w or i in viz:
#             continue
#         if ord(grid[i]) - ord(grid[a]) <= 1:
#             viz[i] = dist + 1
#             q.append(i)
# print(viz)
# print(viz[end])

#part 2
grid = {}
h = 0
starts = set()
for i in range(len(lines)):
    l = lines[i].strip()
    if l == '':
        continue
    h += 1
    for j in range(len(l)):
        if lines[i][j] == 'S':
            start = (i,j)
            grid[(i,j)] = 'a'
        elif lines[i][j] == 'E':
            end = (i,j)
            grid[(i,j)] = 'z'
        else:
            if lines[i][j] == 'a':
                starts.add((i,j))
            grid[(i,j)] = lines[i][j]

m = 9999999
for s in starts:
    w = len(lines[0])
    q = [s]
    viz = {}
    viz[s] = 0
    while len(q) > 0:
        a = q.pop(0)
        a1 = (a[0] + 1, a[1])
        a2 = (a[0] - 1, a[1])
        a3 = (a[0], a[1] + 1)
        a4 = (a[0], a[1] - 1)
        dist = viz[a]
        for i in [a1, a2, a3, a4]:
            if i[0] < 0 or i[0] >= h or i[1] < 0 or i[1] >= w or i in viz:
                continue
            if ord(grid[i]) - ord(grid[a]) <= 1:
                viz[i] = dist + 1
                q.append(i)
        if end in viz:
            m = min(viz[end],m)
print(m)
