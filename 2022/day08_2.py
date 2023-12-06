from lib.grid import grid
import sys
sys.path.append('../')

day = '08'
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('day{}_{}.txt'.format(day, 'sample' if sample else 'data'))

lines = f.read().splitlines()

x = grid(lines, True)
s = 0
ss = 0
for i in range(x.height):
    for j in range(x.width):
        seq1 = x.goUp(i, j)
        seq2 = x.goDown(i, j)
        seq3 = x.goLeft(i, j)
        seq4 = x.goRight(i, j)
        v1 = v2 = v3 = v4 = True
        s1 = s2 = s3 = s4 = 0
        h = x.rows[i][j]
        for a in seq1:
            s1 += 1
            if a >= h:
                v1 = False
                break
        for a in seq2:
            s2 += 1
            if a >= h:
                v2 = False
                break
        for a in seq3:
            s3 += 1
            if a >= h:
                v3 = False
                break
        for a in seq4:
            s4 += 1
            if a >= h:
                v4 = False
                break
        if v1 or v2 or v3 or v4:
            s += 1
        ss = max(ss, s1 * s2 * s3 * s4)
print(s, ss)
