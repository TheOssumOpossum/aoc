import sys
import re

day = '02'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample2' if sys.argv[1] == '2' else 'sample'))
lines = f.read().strip().splitlines()

#part 1
# game = 0
# games = 0
# s = 0
# for line in lines:
#     game += 1
#     games += game
#     l = line.strip()
#     x = re.findall("\d+|\w+|;",l)
#     x = x[2:]
#     b = 0
#     r = 0
#     g = 0
#     i = -1
#     for a in x:
#         i += 1
#         if a == ';':
#             if r > 12 or g > 13 or b > 14:
#                 s += game
#                 b = 0
#                 r = 0
#                 g = 0
#                 break
#             b = 0
#             r = 0
#             g = 0
#         else:
#             if a.isnumeric():
#                 if x[i+1] == 'red':
#                     r += int(a)
#                 elif x[i+1] == 'blue':
#                     b += int(a)
#                 elif x[i+1] == 'green':
#                     g += int(a)
#     if r > 12 or g > 13 or b > 14:
#         s += game
#         b = 0
#         r = 0
#         g = 0
# print(games-s) 

#part 2
s = 0
for line in lines:
    l = line.strip()
    x = re.findall("\d+|\w+|;",l)
    x = x[2:]
    b = 0
    r = 0
    g = 0
    bx = 0
    rx = 0
    gx = 0
    i = -1
    for a in x:
        i += 1
        if a == ';':
            bx = max(b, bx)
            rx = max(r, rx)
            gx = max(g, gx)
            b = 0
            r = 0
            g = 0
        else:
            if a.isnumeric():
                # print(a)
                if x[i+1] == 'red':
                    r += int(a)
                elif x[i+1] == 'blue':
                    b += int(a)
                elif x[i+1] == 'green':
                    g += int(a)
    bx = max(b, bx)
    rx = max(r, rx)
    gx = max(g, gx)
    p = bx*rx*gx
    
    s += p
print(s) 
