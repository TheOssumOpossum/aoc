import sys

day = 17
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

lines = f.read().splitlines()

#part 1
wind = ''
for line in lines:
    l = line.strip()
    if l == '':
        continue
    wind = l
print(wind)
width = 7
rocks = 5
drops = 2022
# drops = 10

r = -1
m = {}
min_y = 0
w = -1
push = True
for _ in range(drops):
    # print(_)
    # for y in range(20,-1,-1):
    #     s = ''
    #     for x in range(7):
    #         s += '.' if (x,y) not in m else '#'
    #     print(s)
    r += 1
    r = r % rocks
    tmp = []
    min_y += 3
    match r:
        case 0:
            for i in range(4):
                tmp.append([2+i, min_y])
            min_y += 1
            max_x = 5
        case 1:
            tmp.append([3, min_y])
            for i in range(3):
                tmp.append([2+i, min_y+1])
            tmp.append([3, min_y+2])
            min_y += 3
            max_x = 4
        case 2:
            for i in range(3):
                tmp.append([2+i, min_y])
            tmp.append([4, min_y+1])
            tmp.append([4, min_y+2])
            min_y += 3
            max_x = 4
        case 3:
            for i in range(4):
                tmp.append([2, min_y+i])
            min_y += 4
            max_x = 2
        case 4:
            for i in range(2):
                for j in range(2):
                    tmp.append([2+i, min_y+j])
            min_y += 2
            max_x = 3
    min_x = 2
    while True:
        # print(tmp, max_x, min_x, wind[(w+1)%len(wind)] if push else 'v')
        if push:
            push = False
            w += 1
            w = w % len(wind)
            dir = 0
            if wind[w] == '<':
                dir = -1
            else:
                dir = 1
            if min_x == 0 and dir == -1:
                continue
            if max_x == 6 and dir == 1:
                continue
            move = True
            for x in tmp:
                if (x[0]+dir, x[1]) in m:
                    move = False
                    break
            if move:
                for i in range(len(tmp)):
                    tmp[i][0] += dir
                max_x += dir
                min_x += dir
            continue
        else:
            push = True
            move = True
            for x in tmp:
                if (x[0], x[1]-1) in m or x[1]-1 == -1:
                    move = False
                    break
            if move:
                min_y -= 1
                for i in range(len(tmp)):
                    tmp[i][1] -= 1
            else:
                for i in tmp:
                    m[(i[0],i[1])] = '#'
                break

xx = sorted(list(m))

for y in range(15,-1,-1):
    s = ''
    for x in range(7):
        s += '.' if (x,y) not in m else '#'
    print(s)
# print(xx)

max_y = 0
for i in m:
    max_y = max(max_y, i[1])
print(max_y)

#2876 too low
