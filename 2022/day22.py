import sys
import re

day = 22
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

lines = f.read().splitlines()

# part 1
# m = {}
# min_row = {}
# min_col = {}
# max_row = {}
# max_col = {}
# row = -1
# ins = None
# x = y = 0
# start = False
# for line in lines:
#     if 'L' in line:
#         ins = line
#         break
#     row += 1
#     col = -1
#     for c in line:
#         col += 1
#         if c == ' ':
#             continue
#         m[(row,col)] = c
#         if start is False:
#             y = row
#             x = col
#             start = True
#         if row not in min_col:
#             min_col[row] = col
#             max_col[row] = col
#         else:
#             min_col[row] = min(min_col[row], col)
#             max_col[row] = max(max_col[row], col)
#         if col not in min_row:
#             min_row[col] = row
#             max_row[col] = row
#         else:
#             min_row[col] = min(min_row[col], row)
#             max_row[col] = max(max_row[col], row)
# print(m)
# print(min_row)
# print(min_col)

# ins = re.findall('[A-Z]{1}|\d+', line)
# print(ins)

# dir = 0
# row = y
# col = x

# for i in ins:
#     # print(row, col)
#     if i.isnumeric():
#         i = int(i)
#         for i in range(i):
#             # print(' ', row, col)
#             match dir:
#                 case 0:
#                     prev_col = col
#                     col += 1
#                     if (row, col) not in m:
#                         col = min_col[row]
#                     if m[(row, col)] == '#':
#                         col = prev_col
#                         break
#                 case 2:
#                     prev_col = col
#                     col -= 1
#                     if (row, col) not in m:
#                         col = max_col[row]
#                     if m[(row, col)] == '#':
#                         col = prev_col
#                         break
#                 case 1:
#                     prev_row = row
#                     row += 1
#                     if (row, col) not in m:
#                         row = min_row[col]
#                     if m[(row, col)] == '#':
#                         row = prev_row
#                         break
#                 case 3:
#                     prev_row = row
#                     row -= 1
#                     if (row, col) not in m:
#                         row = max_row[col]
#                     if m[(row, col)] == '#':
#                         row = prev_row
#                         break
#     else:
#         match i:
#             case 'R':
#                 dir += 1
#                 dir = dir % 4
#             case 'L':
#                 dir -= 1
#                 dir = dir % 4

# print(row+1,col+1,dir)
                
# print((row+1)*1000+(col+1)*4+dir)

#part 2
m = {}
row = -1
ins = None
x = y = 0
start = False
for line in lines:
    if 'L' in line:
        ins = line
        break
    row += 1
    col = -1
    for c in line:
        col += 1
        if c == ' ':
            continue
        m[(row,col)] = c #if c == '.' else '█'
        if start is False:
            y = row
            x = col
            start = True

mm = {}
mmm = {}
s = 0
size = 50

for i in m:
    row = i[0]
    col = i[1]
    val = m[i]
    if 0 <= row < size:
        if size <= col < size*2:
            f = 6
        else:
            f = 5
    elif size <= row < size*2:
        f = 4
    elif size*2 <= row < size*3:
        if 0 <= col < size:
            f = 2
        else:
            f = 1
    else:
        f = 3
    mm[(row%size,col%size,f)] = val
    mmm[(row%size,col%size,f)] = (row, col)
    m[i] = (val, f)
    
# only works for this unfolding
#   65 
#   4
#  21
#  3

print(s)

ins = re.findall('[A-Z]{1}|\d+', line)
# print(ins)

dir = 0
row = 0
col = 0
f = 6

dirmap = {0: '>', 1: 'v', 2: '<', 3: '^'}
size -=1 
its = -1

for i in range(200):
    s = ''
    for j in range(150):
        if (i,j) not in m:
            s += '.'
        else:
            s += str(m[(i,j)][1])
    print(s)

idx = mmm[(row,col,f)]
m[idx] = dirmap[dir]

# print(ins)
for i in ins:
    its += 1
    if not i.isnumeric():
        match i:
            case 'R':
                dir += 1
                dir = dir % 4
            case 'L':
                dir -= 1
                dir = dir % 4
        idx = mmm[(row,col,f)]
        m[idx] = dirmap[dir]
        # print('turning to', dirmap[dir], 'at', row,col, f)
    else:
        i = int(i)
        # print('moving', i, dirmap[dir], 'from', row, col, f)
        for i in range(i):
            prev_row = row
            prev_col = col
            prev_f = f
            prev_dir = dir
            match dir:
                case 0:
                    col += 1
                    # print(col)
                    if (row, col, f) not in mm:
                        match f:
                            case 1:
                                f = 5
                                dir = 2
                                col = size
                                row = size - row
                            case 2:
                                f = 1
                                col = 0
                            case 3:
                                f = 1
                                dir = 3
                                col = row
                                row = size
                            case 4:
                                f = 5
                                dir = 3
                                col = row
                                row = size
                            case 5:
                                f = 1
                                dir = 2
                                row = size - row
                                col = size
                            case 6:
                                f = 5
                                col = 0
                case 1:
                    row += 1
                    if (row, col, f) not in mm:
                        match f:
                            case 1:
                                f = 3
                                dir = 2
                                row = col
                                col = size
                            case 2:
                                f = 3
                                row = 0
                            case 3:
                                f = 5
                                row = 0
                            case 4:
                                f = 1
                                row = 0
                            case 5:
                                f = 4
                                dir = 2
                                row = col
                                col = size
                            case 6:
                                f = 4
                                row = 0
                case 2:
                    col -= 1
                    if (row, col, f) not in mm:
                        match f:
                            case 1:
                                f = 2
                                col = size
                            case 2:
                                f = 6
                                dir = 0
                                col = 0
                                row = size - row
                            case 3:
                                f = 6
                                dir = 1
                                col = row
                                row = 0
                            case 4:
                                f = 2
                                dir = 1
                                col = row
                                row = 0
                            case 5:
                                f = 6
                                col = size
                            case 6:
                                f = 2
                                dir = 0
                                row = size - row
                                col = 0
                case 3:
                    row -= 1
                    if (row, col, f) not in mm:
                        match f:
                            case 1:
                                f = 4
                                row = size
                            case 2:
                                f = 4
                                dir = 0
                                row = col
                                col = 0
                            case 3:
                                f = 2
                                row = size
                            case 4:
                                f = 6
                                row = size
                            case 5:
                                f = 3
                                row = size
                            case 6:
                                f = 3
                                dir = 0
                                row = col
                                col = 0
            # print(row,col,f)
            if mm[(row, col, f)] == '#':
                row = prev_row
                col = prev_col
                f = prev_f
                dir = prev_dir
                break
            else:
                # print('updating idx',idx)
                idx = mmm[(row,col,f)]
                # print(idx)
                m[idx] = dirmap[dir]

for ii in range(200):
    s = ''
    for jj in range(150):
        if (ii,jj) not in m:
            s += ' '
        else:
            cha = m[(ii,jj)]
            s += cha if type(cha) == str else cha[0]
    print(s)

print(row,col, f, dir)
x = mmm[(row,col,f)]
print(x)
print((x[0]+1)*1000+(x[1]+1)*4+dir)
