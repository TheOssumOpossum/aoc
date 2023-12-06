import sys
import re

day = '09'
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('day{}_{}.txt'.format(day,'sample2' if sample else 'data'))

lines = f.read().splitlines()

# #part 1
# viz = set()
# viz.add((0,0))
# hx = 0
# hy = 0
# tx = 0
# ty = 0
# for line in lines:
#     l = line.strip()
#     if l == '':
#         continue
#     steps = re.findall("\d+",l)[0]
#     steps = int(steps)
#     direc = l[0]
#     for i in range(steps):
#         match direc:
#             case 'R':
#                 hx += 1
#             case 'L':
#                 hx -= 1
#             case 'U':
#                 hy += 1
#             case 'D':
#                 hy -= 1
#         if abs(hx-tx) > 1 or abs(hy-ty) > 1:
#             if hx == tx:
#                 if hy > ty:
#                     ty += 1
#                 else:
#                     ty -= 1
#             elif hy == ty:
#                 if hx > tx:
#                     tx += 1
#                 else:
#                     tx -= 1
#             else:
#                 if hy > ty:
#                     ty += 1
#                 else:
#                     ty -= 1
#                 if hx > tx:
#                     tx += 1
#                 else:
#                     tx -= 1
#         viz.add((tx,ty))
#         # print(hx,hy)
#     # manhattan = abs(hx-tx) + abs(hy-ty)
#     # if manhattan > 1:
    
# print(len(viz))
# # print(sorted(list(viz)))
        
#part 2
viz = set()
viz.add((0,0))
# rope = [[0,0] for i in range(10)]
rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
# hx = 0
# hy = 0
# tx = 0
# ty = 0
for line in lines:
    l = line.strip()
    if l == '':
        continue
    steps = re.findall("\d+",l)[0]
    steps = int(steps)
    direc = l[0]
    for i in range(steps):
        match direc:
            case 'R':
                rope[0][0] = rope[0][0] + 1
            case 'L':
                rope[0][0] -= 1
            case 'U':
                rope[0][1] += 1
            case 'D':
                rope[0][1] -= 1
        for i in range(0,9):
            if abs(rope[i][0]-rope[i+1][0]) > 1 or abs(rope[i][1]-rope[i+1][1]) > 1:
                if rope[i][0] == rope[i+1][0]:
                    if rope[i][1] > rope[i+1][1]:
                        rope[i+1][1] += 1
                    else:
                        rope[i+1][1] -= 1
                elif rope[i][1] == rope[i+1][1]:
                    if rope[i][0] > rope[i+1][0]:
                        rope[i+1][0] += 1
                    else:
                        rope[i+1][0] -= 1
                else:
                    if rope[i][1] > rope[i+1][1]:
                        rope[i+1][1] += 1
                    else:
                        rope[i+1][1] -= 1
                    if rope[i][0] > rope[i+1][0]:
                        rope[i+1][0] += 1
                    else:
                        rope[i+1][0] -= 1
        viz.add((rope[9][0],rope[9][1]))
    
print(len(viz))
# print(sorted(list(viz)))
        
    





