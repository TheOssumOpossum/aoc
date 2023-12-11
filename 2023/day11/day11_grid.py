import sys
sys.path.append('../..')
from lib.grid import grid

day = '11'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip().splitlines()

g = grid(lines)

long_rows = set()
long_cols = set()
for i, row in enumerate(g.rows):
    if '#' not in row:
        long_rows.add(i)
for i, col in enumerate(g.cols):
    if '#' not in col:
        long_cols.add(i)

print(long_rows, long_cols)
galaxies = g.getVals('#')

m = {}
i = 0
for x in galaxies:
    factor = 1e6
    row, col = x
    row_offset = 0
    col_offset = 0
    for r in long_rows:
        if row > r:
            row_offset += 1
    for c in long_cols:
        if col > c:
            col_offset += 1
    m[i] = (row+row_offset*(factor-1), col+col_offset*(factor-1))
    i += 1 

def calcDist(i,j):
    a = m[i]
    b = m[j]
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
s = 0

for j in range(i):
    for k in range(i):
        if j >= k:
            continue
        s += calcDist(j,k)
print(s)
