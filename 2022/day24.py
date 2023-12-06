import sys

day = 24
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

#part 1
# lines = f.read().strip().splitlines()

# m = {}
# row = -1
# exit_row = 0
# exit_col = 0
# rows = len(lines) - 2
# cols = len(lines[0]) - 2
# print(rows, cols)
# for line in lines:
#     row += 1
#     l = line.strip()
#     for col in range(1,len(l)-1):
#         if l[col] in ['>','v','<','^']:
#             m[(0, row,col-1)] = l[col]
#         if l[col] == '.':
#             exit_row = row
#             exit_col = col-1
# print(exit_row, exit_col)

# dirs = {'>':(0,1), '<':(0,-1), 'v':(1,0), '^':(-1,0)}
# states = rows*cols
# prev_m = {}
# for x in m:
#     prev_m[(x[1],x[2])] = m[x]

# #calculate m
# for i in range(10000):
#     new_m = {}
#     for x in prev_m:
#         chars = prev_m[x]
#         row = x[0]
#         col = x[1]
#         for char in chars:
#             row_inc = col_inc = 0
#             if char in ['>','v','<','^']:
#                 row_inc, col_inc = dirs[char]
#             new_row =  row + row_inc
#             if new_row == rows+1:
#                 new_row = 1
#             elif new_row == 0:
#                 new_row = rows
#             new_col =  col + col_inc
#             new_col %= cols
#             if (new_row,new_col) not in new_m:
#                 new_m[(new_row,new_col)] = char
#             else:
#                 new_m[(new_row,new_col)] += char
#     prev_m = new_m
#     for x in new_m:
#         row = x[0]
#         col = x[1]
#         m[(i+1, row, col)] = new_m[(row,col)]
#     done = True
#     for x in new_m:
#         if (0,x[0],x[1]) not in m or new_m[x] != m[(0,x[0],x[1])]:
#             done = False
#             break
#     if done:
#         break
#     else:
#         if i %10 == 0:
#             print('calculated state:', i)
# # for x in sorted(list(m)):
# #     print(x, m[x])

# states = i+1
# print('number of states before cycle:', i)
# from collections import deque
# q = deque()
# q.append((0,0,0))
# viz = {}
# viz[(0,0,0)] = (0, [])
# while len(q) != 0:
#     x = q.popleft()
#     row = x[1]
#     col = x[2]
#     s = x[0]
#     dist = viz[x]
#     next_state = (s+1)%states
#     if row == exit_row and col == exit_col:
#         print('mins:', dist)
#         break
#     dirs = [(1,0),(-1,0),(0,1),(0,-1),(0,0)]
#     for i in dirs:
#         row_inc, col_inc = i
#         new_row = row + row_inc
#         new_col = col + col_inc
#         if new_row < 0 or new_row == 0 and new_col != 0:
#             continue
#         if new_row == exit_row and new_col != exit_col:
#             continue
#         if new_col < 0 or new_col > exit_col:
#             continue
#         if (next_state, new_row, new_col) not in m and (next_state, new_row, new_col) not in viz:
#             q.append((next_state, new_row, new_col))
#             viz[(next_state, new_row, new_col)] = dist + 1
                
# part 2
lines = f.read().strip().splitlines()

m = {}
row = -1
exit_row = 0
exit_col = 0
rows = len(lines) - 2
cols = len(lines[0]) - 2
print(rows, cols)
for line in lines:
    row += 1
    l = line.strip()
    for col in range(1,len(l)-1):
        if l[col] in ['>','v','<','^']:
            m[(0, row,col-1)] = l[col]
        if l[col] == '.':
            exit_row = row
            exit_col = col-1
print(exit_row, exit_col)

dirs = {'>':(0,1), '<':(0,-1), 'v':(1,0), '^':(-1,0)}
states = rows*cols
prev_m = {}
for x in m:
    prev_m[(x[1],x[2])] = m[x]

#calculate m
for i in range(10000):
    new_m = {}
    for x in prev_m:
        chars = prev_m[x]
        row = x[0]
        col = x[1]
        for char in chars:
            row_inc = col_inc = 0
            if char in ['>','v','<','^']:
                row_inc, col_inc = dirs[char]
            new_row =  row + row_inc
            if new_row == rows+1:
                new_row = 1
            elif new_row == 0:
                new_row = rows
            new_col =  col + col_inc
            new_col %= cols
            if (new_row,new_col) not in new_m:
                new_m[(new_row,new_col)] = char
            else:
                new_m[(new_row,new_col)] += char
    prev_m = new_m
    for x in new_m:
        row = x[0]
        col = x[1]
        m[(i+1, row, col)] = new_m[(row,col)]
    done = True
    for x in new_m:
        if (0,x[0],x[1]) not in m or new_m[x] != m[(0,x[0],x[1])]:
            done = False
            break
    if done:
        break
    else:
        if i %10 == 0:
            print('calculated state:', i)

states = i+1
print('number of states before cycle:', i)
from collections import deque

def calcFromTo(row_start=0, col_start=0, row_end=exit_row, col_end=exit_col, state=0):
    global m
    global exit_row
    global exit_col
    viz = {}
    viz[(state, row_start, col_start)] = 0
    q = deque()
    q.append((state, row_start, col_start))
    while len(q) > 0:
        x = q.popleft()
        row = x[1]
        col = x[2]
        s = x[0]
        dist = viz[x]
        next_state = (s+1)%states
        if row == row_end and col == col_end:
            # print('mins:', dist)
            break
        dirs = [(1,0),(-1,0),(0,1),(0,-1),(0,0)]
        for i in dirs:
            row_inc, col_inc = i
            new_row = row + row_inc
            new_col = col + col_inc
            if new_row < 0 or new_row == 0 and new_col != 0:
                continue
            if new_row > exit_row or new_row == exit_row and new_col != exit_col:
                continue
            if new_col < 0 or new_col > exit_col:
                continue
            if (next_state, new_row, new_col) not in m and (next_state, new_row, new_col) not in viz:
                q.append((next_state, new_row, new_col))
                viz[(next_state, new_row, new_col)] = dist + 1
    return dist

x1 = calcFromTo()
print('calc to:', x1)
x2 = calcFromTo(exit_row, exit_col, 0, 0, x1)
print('calc back:', x1, x1+x2)
x3 = calcFromTo(state=x1+x2)
print('calc to again', x3)
print(x1+x2+x3)
