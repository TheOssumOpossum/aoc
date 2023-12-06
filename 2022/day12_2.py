import sys
sys.path.append('../')
from lib.grid import grid

day = 12
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

#part 1
# lines = f.read().splitlines()

# z = grid(lines)
# start = (0,0)
# end = (0,0)
# for i in range(z.height):
#     for j in range(z.width):
#         if z[i][j] == 'S':
#             z[i][j] = 'a'
#             start = (i,j)
#         elif z[i][j] == 'E':
#             z[i][j] = 'z'
#             end = (i,j)

# viz = {}
# viz[start] = 0
# q = [start]
# while len(q) > 0:
#     a = q.pop(0)
#     dist = viz[a]
#     y = a[0]
#     x = a[1]
#     a1 = z.transit('l',x,y,include=False,idx=True)
#     a2 = z.transit('r',x,y,include=False,idx=True)
#     a3 = z.transit('u',x,y,include=False,idx=True)
#     a4 = z.transit('d',x,y,include=False,idx=True)
#     for i in [a1, a2, a3, a4]:
#         if len(i) > 0:
#             aa = tuple(i[0])
#             if aa not in viz and ord(z[aa[0]][aa[1]]) - ord(z[y][x]) <= 1:
#                 viz[aa] = dist + 1
#                 q.append(aa)
# print(viz[end])

#part 2
lines = f.read().splitlines()

z = grid(lines)
starts = []
end = (0,0)
for i in range(z.height):
    for j in range(z.width):
        if z[i][j] == 'S' or z[i][j] == 'a':
            z[i][j] = 'a'
            starts.append((i,j))
        elif z[i][j] == 'E':
            z[i][j] = 'z'
            end = (i,j)

viz = {}
for i in starts:
    viz[i] = 0

q = starts
while len(q) > 0:
    a = q.pop(0)
    dist = viz[a]
    y = a[0]
    x = a[1]
    a1 = z.transit('l',x,y,include=False,idx=True)
    a2 = z.transit('r',x,y,include=False,idx=True)
    a3 = z.transit('u',x,y,include=False,idx=True)
    a4 = z.transit('d',x,y,include=False,idx=True)
    for i in [a1, a2, a3, a4]:
        if len(i) > 0:
            aa = tuple(i[0])
            if aa not in viz and ord(z[aa[0]][aa[1]]) - ord(z[y][x]) <= 1:
                viz[aa] = dist + 1
                q.append(aa)
print(viz[end])
