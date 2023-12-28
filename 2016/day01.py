import sys

f = open(f'{f"../input/{__file__[-15:-11]}/" if (len(sys.argv) >= 2 and sys.argv[1] == "1") else ""}day{__file__[-5:-3]}_{"data" if (len(sys.argv) >= 2 and sys.argv[1] == "1") else "sample" if len(sys.argv) < 2 or sys.argv[1] == "0" else "sample" + sys.argv[1]}.txt')
txt = f.read().strip()
lines = txt.split('\n')

# Part 1 and 2
s = 0
directions = [(0,1),(-1,0),(0,-1),(1,0)]
dir = 0
x = y = 0
viz = set()
ss = None
for i, line in enumerate(lines):
    steps = line.split(', ')
    for step in steps:
        dist = int(step[1:])
        if step[0] == 'L':
            dir += 1
        else:
            dir -= 1
        dir %= 4
        # x += directions[dir][0] * int(j[1:])
        # y += directions[dir][1] * int(j[1:])
        x_add = directions[dir][0] * dist
        y_add = directions[dir][1] * dist

        def addViz(x,y):
            if (x,y) not in viz:
                viz.add((x,y))
            elif ss is None:
                ss = abs(x) + abs(y)

        for _ in range(abs(x_add)):
            x += -1 if x_add < 0 else 1
            addViz(x,y)
        for _ in range(abs(y_add)):
            y += -1 if y_add < 0 else 1
            addViz(x,y)
s = abs(x) + abs(y)

print(s)
print(ss)