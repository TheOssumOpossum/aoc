# https://adventofcode.com/2020/day/17
import copy

day = "17"

# #part 1 v2
# txt = open("../input/day" + day + ".txt", "r")
# # txt = open("../tst/day" + day + "_test.txt", "r")
# # txt = open("../tst/day" + day + "_test2.txt", "r")
# txt = txt.readlines()
# txt.append("\n")
# result = 0

# rows = -1
# cols = 0
# empty_map = []
# cur_map = []
# for l in txt:
#     if l == "\n":
#         continue
#         ''
#     l = l.strip()
#     if cols == 0:
#         cols = len(l)
#     col = -1
#     rows += 1
#     cur_map.append([])
#     for c in l:
#         col += 1
#         cur_map[rows].append(c)

# cycles = 6
# first_map = []
# for i in range(cycles*2+rows+cycles*2):
#     first_map.append([])
#     for j in range(cycles*2+cols+cycles*2):
#         if cycles*2-1 <= i < cycles*2+rows and cycles*2-1 <= j < cycles*2+cols-1:
#             first_map[i].append(cur_map[i-cycles*2-rows][j-cycles*2-rows])
#         else:
#             first_map[i].append(".")

# # for i in range(len(first_map)):
#     # string = ""
#     # for j in range(len(first_map[0])):
#         # string += first_map[i][j]
#     # print(string)

# for i in range(rows+cycles*2+cycles*2):
#     empty_map.append([])
#     for j in range(cols+cycles*2+cycles*2):
#         empty_map[i].append(".")

# maps = []
# for c in range(cycles*2+cycles*2):
#     if c == cycles*2:
#         maps.append(copy.deepcopy(first_map))
#         continue
#     maps.append(copy.deepcopy(empty_map))

# for _ in range(cycles):
#     next_maps = []
#     for m in range(len(maps)):
#         if m == 0 or m == len(maps)-1:
#             next_maps.append(copy.deepcopy(empty_map))
#             continue
#         new_map = []
#         for r in range(cycles*2+rows+cycles*2):
#             new_map.append([])
#             for c in range(cycles*2+cols+cycles*2):
#                 active_neighbors = 0
#                 for x in [-1, 0, 1]:
#                     for y in [-1, 0, 1]:
#                         for z in [-1, 0, 1]:
#                             if x == y == z == 0:
#                                 continue
#                             if r+y < 0 or r+y >= cycles*2+rows+cycles*2 or c+x < 0 or c+x >= cycles*2+cols+cycles*2:
#                                 continue
#                             # print(m+z, r+y, c+x)
#                             if maps[m+z][r+y][c+x] == "#":
#                                 active_neighbors += 1
#                             if active_neighbors > 3:
#                                 break
#                         if active_neighbors > 3:
#                             break
#                     if active_neighbors > 3:
#                         break
#                 if maps[m][r][c] == ".":
#                     if active_neighbors == 3:
#                         new_map[r].append("#")
#                     else:
#                         new_map[r].append(".")
#                 else:
#                     if 2 <= active_neighbors <= 3:
#                         new_map[r].append("#")
#                     else:
#                         new_map[r].append(".")
#         next_maps.append(copy.deepcopy(new_map))
#     maps = copy.deepcopy(next_maps)

# active = 0
# for m in range(len(maps)):
#     for r in range(len(maps[m])):
#         for c in range(len(maps[m][r])):
#             if maps[m][r][c] == "#":
#                 active += 1
# print(active)

#part 1 v1
# txt = open("../input/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")
# txt = txt.readlines()
# txt.append("\n")
# result = 0

# rows = -1
# cols = 0
# empty_map = {}
# cur_map = {}
# for l in txt:
#     if l == "\n":
#         ''
#     l = l.strip()
#     if cols == 0:
#         cols = len(l)
#     col = -1
#     rows += 1
#     for c in l:
#         col += 1
#         if rows not in cur_map:
#             cur_map[rows] = []
#         cur_map[rows].append(c)

# cycles = 6
# first_map = {}
# for i in range(-cycles*2,cycles*2+rows):
#     for j in range(-cycles*2, cycles*2+cols):
#         if i not in first_map:
#             first_map[i] = []
#         if 0 <= i < rows and 0 <= j < cols:
#             first_map[i].append(cur_map[i][j])
#         else:
#             first_map[i].append(".")

# for i in range(-cycles*2,rows+cycles*2):
#     for j in range(-cycles*2,cols+cycles*2):
#         if i not in empty_map:
#             empty_map[i] = []
#         empty_map[i].append(".")

# maps = []
# for c in range(-cycles*2,cycles*2):
#     if c == 0:
#         maps.append(copy.deepcopy(first_map))
#         continue
#     maps.append(copy.deepcopy(empty_map))

# hyper_maps = []
# hyper_maps.append(maps)
# for asd in range(cycles):
#     next_maps = []
#     for m in range(len(maps)):
#         if m == 0 or m == len(maps)-1:
#             next_maps.append(copy.deepcopy(empty_map))
#             continue
#         new_map = {}
#         for r in range(-cycles*2,cycles*2+rows):
#             for c in range(-cycles*2,cycles*2+cols):
#                 active_neighbors = 0
#                 for x in [-1, 0, 1]:
#                     for y in [-1, 0, 1]:
#                         for z in [-1, 0, 1]:
#                             for w in [-1, 0, 1]:
#                                 if x == y == z == w == 0:
#                                     continue
#                                 if r+y <= -cycles*2-1 or r+y >= cycles*2+rows:
#                                     continue
#                                 if maps[m+z][r+y][c+x] == "#":
#                                     active_neighbors += 1
#                                 if active_neighbors > 3:
#                                     break
#                         if active_neighbors > 3:
#                             break
#                     if active_neighbors > 3:
#                         break
#                 if maps[m][r][c] == ".":
#                     if r not in new_map:
#                         new_map[r] = []
#                     if active_neighbors == 3:
#                         new_map[r].append("#")
#                     else:
#                         new_map[r].append(".")
#                 else:
#                     if r not in new_map:
#                         new_map[r] = []
#                     if 2 <= active_neighbors <= 3:
#                         new_map[r].append("#")
#                     else:
#                         new_map[r].append(".")
#         next_maps.append(copy.deepcopy(new_map))
#     maps = copy.deepcopy(next_maps)

# active = 0
# for m in range(len(maps)):
#     for r in maps[m]:
#         for c in range(len(maps[m][r])):
#             if maps[m][r][c] == "#":
#                 active += 1
# print(active)


#part 2
txt = open("../input/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")
txt = txt.readlines()
txt.append("\n")
result = 0

rows = -1
cols = 0
cur_map = []
for l in txt:
    if l == "\n":
        continue
        ''
    l = l.strip()
    if cols == 0:
        cols = len(l)
    col = -1
    rows += 1
    cur_map.append([])
    for c in l:
        col += 1
        cur_map[rows].append(c)

cycles = 6
first_map = []
for i in range(cycles*2+rows+cycles*2):
    first_map.append([])
    for j in range(cycles*2+cols+cycles*2):
        if cycles*2-1 <= i < cycles*2+rows and cycles*2-1 <= j < cycles*2+cols-1:
            first_map[i].append(cur_map[i-cycles*2-rows][j-cycles*2-rows])
        else:
            first_map[i].append(".")

empty_map = []
for i in range(rows+cycles*2+cycles*2):
    empty_map.append([])
    for j in range(cols+cycles*2+cycles*2):
        empty_map[i].append(".")

maps = []
for c in range(cycles*2+cycles*2):
    if c == cycles*2:
        maps.append(copy.deepcopy(first_map))
        continue
    maps.append(copy.deepcopy(empty_map))


empty_maps = []
for i in range(rows+cycles*2+cycles*2):
    empty_maps.append(copy.deepcopy(empty_map))

hyper_maps = []
for c in range(cycles*2+cycles*2):
    if c == cycles*2:
        hyper_maps.append(copy.deepcopy(maps))
        continue
    hyper_maps.append(copy.deepcopy(empty_maps))


for cycle_no in range(cycles):
    next_hyper_maps = []
    for h in range(len(hyper_maps)):
        if h == 0 or h == len(hyper_maps)-1:
            next_hyper_maps.append(copy.deepcopy(empty_maps))
            continue
        print("%10.2f"% (float((cycle_no*len(hyper_maps)+h)/((cycles)*len(hyper_maps)-2)*100)),"% complete")
        next_maps = []
        for m in range(len(maps)):
            if m == 0 or m == len(maps)-1:
                next_maps.append(copy.deepcopy(empty_map))
                continue
            new_map = []
            for r in range(cycles*2+rows+cycles*2-1):
                new_map.append([])
                for c in range(cycles*2+cols+cycles*2-1):
                    active_neighbors = 0
                    for x in [-1, 0, 1]:
                        for y in [-1, 0, 1]:
                            for z in [-1, 0, 1]:
                                for w in [-1, 0, 1]:
                                    if w == x == y == z == 0:
                                        continue
                                    # print(h+w, m+z, r+y, c+x)
                                    if r+y < 0 or r+y >= cycles*2+rows+cycles*2-1 or c+x < 0 or c+x >= cycles*2+cols+cycles*2-1:
                                        continue
                                    # print(h+w, m+z, r+y, c+x)
                                    if hyper_maps[h+w][m+z][r+y][c+x] == "#":
                                        # print(h+w, m+z, r+y, c+x)
                                        active_neighbors += 1
                                    if active_neighbors > 3:
                                        break
                                if active_neighbors > 3:
                                    break
                            if active_neighbors > 3:
                                break
                        if active_neighbors > 3:
                            break
                    if hyper_maps[h][m][r][c] == ".":
                        if active_neighbors == 3:
                            new_map[r].append("#")
                        else:
                            new_map[r].append(".")
                    else:
                        if 2 <= active_neighbors <= 3:
                            new_map[r].append("#")
                        else:
                            new_map[r].append(".")
            next_maps.append(copy.deepcopy(new_map))
        next_hyper_maps.append(copy.deepcopy(next_maps))
    hyper_maps = copy.deepcopy(next_hyper_maps)

active = 0
for h in range(len(hyper_maps)):
    for m in range(len(hyper_maps[h])):
        for r in range(len(hyper_maps[h][m])):
            for c in range(len(hyper_maps[h][m][r])):
                if hyper_maps[h][m][r][c] == "#":
                    active += 1
print(active)
