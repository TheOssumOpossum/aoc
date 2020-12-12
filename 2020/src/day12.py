# https://adventofcode.com/2020/day/12

day = "12"

txt = open("../input/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")

#part 1
# result = 0

# x = 0
# y = 0
# x_mult = 1
# y_mult = 0
# angle = 0
# for l in txt:
#     l = l.strip()
#     instruction = l[0]
#     number = int(l[1:])
#     if instruction == 'F':
#         x += x_mult * number
#         y += y_mult * number
#     elif instruction == 'N':
#         y += number
#     elif instruction == 'S':
#         y -= number
#     elif instruction == 'E':
#         x += number
#     elif instruction == 'W':
#         x -= number
#     elif instruction == 'R':
#         angle -= number
#         while angle <= -180:
#             angle += 360
#         if angle == -90:
#             x_mult = 0
#             y_mult = -1
#         elif angle == 0:
#             x_mult = 1
#             y_mult = 0
#         elif angle == 90:
#             x_mult = 0
#             y_mult = 1
#         elif angle == 180:
#             x_mult = -1
#             y_mult = 0
#     elif instruction == 'L':
#         angle += number
#         while angle > 180:
#             angle -= 360
#         if angle == -90:
#             x_mult = 0
#             y_mult = -1
#         elif angle == 0:
#             x_mult = 1
#             y_mult = 0
#         elif angle == 90:
#             x_mult = 0
#             y_mult = 1
#         elif angle == 180:
#             x_mult = -1
#             y_mult = 0

# print(x,y,abs(x)+abs(y))

#part 2
result = 0

x = 0
y = 0
xx = 10
yy = 1
for l in txt:
    l = l.strip()
    instruction = l[0]
    number = int(l[1:])
    if instruction == 'F':
        x += xx * number
        y += yy * number
    elif instruction == 'N':
        yy += number
    elif instruction == 'S':
        yy -= number
    elif instruction == 'E':
        xx += number
    elif instruction == 'W':
        xx -= number
    elif instruction == 'R':
        if number == 90:
            save = xx
            xx = yy
            yy = -save
        elif number == 180:
            xx = -xx
            yy = -yy
        elif number == 270:
            save = xx
            xx = -yy
            yy = save
        print(xx,yy)
    elif instruction == 'L':
        if number == 90:
            save = xx
            xx = -yy
            yy = save
        elif number == 180:
            xx = -xx
            yy = -yy
        elif number == 270:
            save = xx
            xx = yy
            yy = -save
    # break

print(x,y,abs(x)+abs(y))
