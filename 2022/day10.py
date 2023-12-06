import sys
sys.path.append('../')
from lib import grid

day = '10'
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

lines = f.read().splitlines()

#part 1
# cycle = 0
# val = 1
# marks = [20, 60, 100, 140, 180, 220]
# s = 0
# vals = [1]
# for line in lines:
#     # l = line.strip()
#     # if l[0] == 'a':
#     #     cycle += 1
#     #     if cycle in marks:
#     #         s += val*cycle
#     #         print(cycle,val,'pre')
#     #     cycle += 1
#     #     val += int(l[5:])
#     #     print('adding', int(l[5:]))
#     #     # print(int(l[5:]), val)
#     #     if cycle in marks:
#     #         s += val*cycle
#     #         print(cycle,val,'post')
#     # else:
#     #     cycle += 1
#     #     if cycle in marks:
#     #         s += val*cycle
#     #         print(cycle,val,'noop')
#     l = line.strip()
#     if l == '':
#         continue
#     if l[0] == 'a':
#         vals.append(val)
#         val += int(l[5:])
#         vals.append(val)
#     else:
#         vals.append(val)
# cycle = 0
# for i in vals:
#     cycle += 1
#     if cycle in marks:
#         s += cycle * i
# # print(val)


# print('s',s)

#part 2
cycle = 0
val = 1
marks = [20, 60, 100, 140, 180, 220]
s = 0
vals = [1]
for line in lines:
    # l = line.strip()
    # if l[0] == 'a':
    #     cycle += 1
    #     if cycle in marks:
    #         s += val*cycle
    #         print(cycle,val,'pre')
    #     cycle += 1
    #     val += int(l[5:])
    #     print('adding', int(l[5:]))
    #     # print(int(l[5:]), val)
    #     if cycle in marks:
    #         s += val*cycle
    #         print(cycle,val,'post')
    # else:
    #     cycle += 1
    #     if cycle in marks:
    #         s += val*cycle
    #         print(cycle,val,'noop')
    l = line.strip()
    if l == '':
        continue
    if l[0] == 'a':
        vals.append(val)
        val += int(l[5:])
        vals.append(val)
    else:
        vals.append(val)
cycle = 0
for i in vals:
    cycle += 1
    if cycle in marks:
        s += cycle * i
# print(val)

base = 0
screen_row = ['.' for i in range(40)]
while base < 240:
    for i in range(base,base+40):
        if abs(vals[i]-i%40) < 2:
            screen_row[i%40] = '#'
    x = ''
    for i in screen_row:
        x += str(i)
    print(x)
    screen_row = ['.' for i in range(40)]
    base += 40

# print('s',s)
