# https://adventofcode.com/2020/day/13

day = "13"

txt = open("../../input/2020/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test2.txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")

#part 1

# i = 0
# timestamp = 0
# busses = []
# for l in txt:
#     if l == "\n":
#         ''
#     l = l.strip()
#     if i == 0:
#         timestamp = int(l)
#     else:
#         busses = l.split(',')
#     i += 1

# min_leave = float('inf')
# min_bus = 0
# for i in busses:
#     if i == 'x':
#         continue
#     x = 0
#     while x < timestamp:
#         x += int(i)
#     if x - timestamp < min_leave:
#         min_leave = x - timestamp
#         min_bus = int(i)

# print(min_leave, min_bus, min_leave * min_bus)

#part2
i = 0
timestamp = 0
busses = []
for l in txt:
    if l == "\n":
        ''
    l = l.strip()
    if i == 0:
        timestamp = int(l)
    else:
        busses = l.split(',')
    i += 1

iter = -1

dic = {}

offset = -1
for i in busses:
    offset += 1
    if i == 'x':
        continue
    else:
        dic[int(i)] = offset

valid_nums = set()

xx = dic.keys()
yy = sorted(xx, reverse=True)
zz = []
for i in yy:
    zz.append((i,dic[i]))

print(zz)

iter = 1249621287870

while True:
    if iter % 1000000 == 0:
        print("hi", iter)
    iter += 1
    x = (iter * int(zz[0][0])) - zz[0][1]
    leave_after = 0
    # print(x)
    do_continue = False
    for i in zz:
        # print(i)
        leave_after = i[1]
        if ((x + leave_after)) % int(i[0]) != 0:
            # print(i[0], x+leave_after)
            # print(int(i), leave_after, ((x + leave_after)) % int(i))
            do_continue = True
            break
        # else:
            # print(i[0], x+leave_after)
    # break
    if do_continue:
        # break
        continue
    else:
        print(x)
        break
