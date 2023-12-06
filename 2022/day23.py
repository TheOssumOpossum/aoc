import sys

day = 23
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('day{}_{}.txt'.format(day, 'sample' if sample else 'data'))

# # part 1
# lines = f.read().strip().splitlines()

# row = -1
# pos = set()
# for l in lines:
#     line = l.strip()
#     row += 1
#     col = -1
#     for c in line:
#         col += 1
#         if c == '#':
#             pos.add((row, col))

# dir = -1  # north, south, west east


# rounds = 10
# for i in range(rounds):
#     dir += 1
#     dir = dir % 4
#     considered = {}
#     for e in pos:
#         surrounding_elves = 0
#         for ii in range(-1, 2):
#             for jj in range(-1, 2):
#                 if (e[0]+ii, e[1]+jj) in pos:
#                     surrounding_elves += 1
#         if surrounding_elves == 1:
#             continue
#         my_dir = dir
#         for d in range(4):
#             if my_dir == 0:
#                 row = [-1 for x in range(3)]
#                 col = [x for x in range(-1, 2)]
#             elif my_dir == 1:
#                 row = [1 for x in range(3)]
#                 col = [x for x in range(-1, 2)]
#             elif my_dir == 2:
#                 row = [x for x in range(-1, 2)]
#                 col = [-1 for x in range(3)]
#             else:
#                 row = [x for x in range(-1, 2)]
#                 col = [1 for x in range(3)]
#             move = None
#             for j in range(3):
#                 pp = (e[0]+row[j], e[1]+col[j])
#                 if pp in pos:
#                     move = None
#                     break
#                 if j == 1:
#                     move = pp
#             if move is not None:
#                 if move in considered:
#                     considered[move] = None
#                 else:
#                     considered[move] = e
#                 break
#             my_dir += 1
#             my_dir = my_dir % 4

#     # print('  abcdefgijklmnop')
#     # for i in range(-5,10):
#     #   s= '{:02d}'.format(i)
#     #   for j in range(-5,10):
#     #     s += '#' if (i,j) in pos else '.'
#     #   print(s)
#     # print(considered)
#     newpos = set()

#     for c in considered:
#         if considered[c] is None:
#             continue
#         newpos.add(c)
#         pos.remove(considered[c])
#     for e in newpos:
#         pos.add(e)

#     # print('  abcdefgijklmnop')
#     # for i in range(-5,10):
#     #   s= '{:02d}'.format(i)
#     #   for j in range(-5,10):
#     #     s += '#' if (i,j) in pos else '.'
#     #   print(s)
#     # break

# min_row = min_col = 999999
# max_row = max_col = -999999

# for p in pos:
#     min_row = min(p[0], min_row)
#     min_col = min(p[1], min_col)
#     max_row = max(p[0], max_row)
#     max_col = max(p[1], max_col)
# print(min_row, min_col, max_row, max_col)
# print((max_row-min_row + 1)*(max_col - min_col + 1) - len(pos))

# part 2
lines = f.read().strip().splitlines()

row = -1
pos = set()
for l in lines:
    line = l.strip()
    row += 1
    col = -1
    for c in line:
        col += 1
        if c == '#':
            pos.add((row, col))

dir = -1  # north, south, west east


rounds = 10
round = 0
while True:
    round += 1
    dir += 1
    dir = dir % 4
    considered = {}
    for e in pos:
        surrounding_elves = 0
        for ii in range(-1, 2):
            for jj in range(-1, 2):
                if (e[0]+ii, e[1]+jj) in pos:
                    surrounding_elves += 1
        if surrounding_elves == 1:
            continue
        my_dir = dir
        for d in range(4):
            if my_dir == 0:
                row = [-1 for x in range(3)]
                col = [x for x in range(-1, 2)]
            elif my_dir == 1:
                row = [1 for x in range(3)]
                col = [x for x in range(-1, 2)]
            elif my_dir == 2:
                row = [x for x in range(-1, 2)]
                col = [-1 for x in range(3)]
            else:
                row = [x for x in range(-1, 2)]
                col = [1 for x in range(3)]
            move = None
            for j in range(3):
                pp = (e[0]+row[j], e[1]+col[j])
                if pp in pos:
                    move = None
                    break
                if j == 1:
                    move = pp
            if move is not None:
                if move in considered:
                    considered[move] = None
                else:
                    considered[move] = e
                break
            my_dir += 1
            my_dir = my_dir % 4
    newpos = set()

    if len(considered) == 0:
        print(round)
        break
    else:
        print(round)

    for c in considered:
        if considered[c] is None:
            continue
        newpos.add(c)
        pos.remove(considered[c])
    for e in newpos:
        pos.add(e)
