# https://adventofcode.com/2020/day/11
import copy

day = "11"

# txt = open("../input/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")
# txt = open("../tst/day" + day + "_test2.txt", "r")

#part 1

# dic = {}

# i = -1
# height = 0
# max_width = 0
# for l in txt:
#     i += 1
#     if l == "\n":
#         ''

#     l = l.strip()
#     j = -1
#     width = 0
#     for c in l:
#         j += 1
#         dic[(i,j)] = c
#         width += 1
#         if width > max_width:
#             max_width = width
# # print(dic)
# height = i
# # print(height)

# # for i in range(height+1):
# #     string = ""
# #     for j in range(max_width):
# #         string += dic[(i,j)]
# #     print(string)
# # print('')

# # iters = 5
# prev_occupied = -1
# while True:
# # for iter in range(iters):
#     prev_dic = copy.deepcopy(dic)
#     occupied = 0
#     for i in range(height+1):
#         for j in range(max_width):
#             if dic[(i,j)] == '#':
#                 occupied += 1
#     if occupied == prev_occupied:
#         print(occupied)
#         break
#     else:
#         prev_occupied = occupied
#     for i in range(height+1):
#         string = ""
#         for j in range(max_width):
#             string += dic[(i,j)]
#         # print(string)
#     # print('')
#     for i in range(height+1):
#         for j in range(max_width):
            if dic[(i,j)] == 'L':
                if (i - 1 < 0 or prev_dic[(i-1,j)] != '#'):
                    if (i + 1 >= height+1 or prev_dic[(i+1,j)] != '#'):
                        if (j - 1 < 0 or prev_dic[(i,j-1)] != '#'):
                            if (j + 1 >= max_width or prev_dic[(i,j+1)] != '#'):
                                if (i - 1 < 0 or j - 1 < 0 or prev_dic[(i-1,j-1)] != '#'):
                                    if (i - 1 < 0 or j + 1 >= max_width or prev_dic[(i-1,j+1)] != '#'):
                                        if (i + 1 >= height+1 or j + 1 >= max_width or prev_dic[(i+1,j+1)] != '#'):
                                            if (i + 1 >= height+1 or j - 1 < 0 or prev_dic[(i+1,j-1)] != '#'):
                                                dic[(i,j)] = '#'
                                                continue
            elif dic[(i,j)] == '#':
                occupied = 0
                if (i - 1 >= 0 and prev_dic[(i-1,j)] == '#'):
                    occupied += 1
                if (i + 1 < height+1 and prev_dic[(i+1,j)] == '#'):
                    occupied += 1
                if (j - 1 >= 0 and prev_dic[(i,j-1)] == '#'):
                    occupied += 1
                if (j + 1 < max_width and prev_dic[(i,j+1)] == '#'):
                    occupied += 1
                if (i - 1 >= 0 and j - 1 >= 0 and prev_dic[(i-1,j-1)] == '#'):
                    occupied += 1
                if (i - 1 >= 0 and j + 1 < max_width and prev_dic[(i-1,j+1)] == '#'):
                    occupied += 1
                if (i + 1 < height+1 and j + 1 < max_width and prev_dic[(i+1,j+1)] == '#'):
                    occupied += 1
                if (i + 1 < height+1 and j - 1 >= 0 and prev_dic[(i+1,j-1)] == '#'):
                    occupied += 1
                if occupied >= 4:
                    dic[(i,j)] = 'L'
                continue

# # occupied = 0
# # for i in range(height+1):
# #     for j in range(max_width):
# #         if dic[(i,j)] == '#':
# #             occupied += 1
# # print(occupied)


txt = open("../input/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")
# txt = open("../tst/day" + day + "_test2.txt", "r")

#part 2
dic = {}

i = -1
height = 0
max_width = 0
for l in txt:
    i += 1
    if l == "\n":
        ''

    l = l.strip()
    j = -1
    width = 0
    for c in l:
        j += 1
        dic[(i,j)] = c
        width += 1
        if width > max_width:
            max_width = width
height = i

# for i in range(height+1):
#     string = ""
#     for j in range(max_width):
#         string += dic[(i,j)]
#     print(string)
# print('')

def walk_find_seat(i,j):
    a = i
    b = j
    seats = 0
    while a > 0:
        a -= 1
        if prev_dic[(a,b)] == '#':
            seats += 1
            break
        elif prev_dic[(a,b)] == 'L':
            break

    a = i
    b = j
    while a < height:
        a += 1
        if prev_dic[(a,b)] == '#':
            seats += 1
            break
        elif prev_dic[(a,b)] == 'L':
            break

    a = i
    b = j
    while b > 0:
        b -= 1
        if prev_dic[(a,b)] == '#':
            seats += 1
            break
        elif prev_dic[(a,b)] == 'L':
            break

    a = i
    b = j
    while b < max_width-1:
        b += 1
        if prev_dic[(a,b)] == '#':
            seats += 1
            break
        elif prev_dic[(a,b)] == 'L':
            break

    a = i
    b = j
    while a > 0 and b < max_width-1:
        a -= 1
        b += 1
        if prev_dic[(a,b)] == '#':
            seats += 1
            break
        elif prev_dic[(a,b)] == 'L':
            break

    a = i
    b = j
    while a < height and b < max_width-1:
        a += 1
        b += 1
        if prev_dic[(a,b)] == '#':
            seats += 1
            break
        elif prev_dic[(a,b)] == 'L':
            break

    a = i
    b = j
    while a < height and b > 0:
        a += 1
        b -= 1
        if prev_dic[(a,b)] == '#':
            seats += 1
            break
        elif prev_dic[(a,b)] == 'L':
            break

    a = i
    b = j
    while a > 0 and b > 0:
        a -= 1
        b -= 1
        if prev_dic[(a,b)] == '#':
            seats += 1
            break
        elif prev_dic[(a,b)] == 'L':
            break
    return seats



prev_occupied = -1
iters = 0
while True:
    iters += 1
    prev_dic = copy.deepcopy(dic)
    occupied = 0
    for i in range(height+1):
        for j in range(max_width):
            if dic[(i,j)] == '#':
                occupied += 1
    if occupied == prev_occupied:
        print(occupied, iters)
        break
    else:
        prev_occupied = occupied
    # for i in range(height+1):
    #     string = ""
    #     for j in range(max_width):
    #         string += dic[(i,j)]
    #     print(string)
    # print('')
    for i in range(height+1):
        for j in range(max_width):
            if dic[(i,j)] == 'L':
                if walk_find_seat(i,j) == 0:
                    dic[(i,j)] = '#'
                    continue
            elif dic[(i,j)] == '#':
                if walk_find_seat(i,j) >= 5:
                    dic[(i,j)] = 'L'
                continue

# occupied = 0
# for i in range(height+1):
#     for j in range(max_width):
#         if dic[(i,j)] == '#':
#             occupied += 1
# print(occupied)
