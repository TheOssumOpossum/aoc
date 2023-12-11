import sys

day = '11'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip().splitlines()

s = 0
m = {}
galaxies = {}
g = 0
for i, line in enumerate(lines):
    l = line.strip()
    for j, c in enumerate(l):
        m[(i,j)] = c

large_rows = set()
large_cols = set()

for row in range(len(lines)):
    empty = True
    for col in range(len(lines[0])):
        if m[(row,col)] != '.':
            empty = False
            break
    if empty:
        large_rows.add(row)
        
for col in range(len(lines[0])):
    empty = True
    for row in range(len(lines)):
        if m[(row,col)] != '.':
            empty = False
            break
    if empty:
        large_cols.add(col)
        
def recalculate_galaxies(factor=1000000):
    global g
    g = 0
    for p in m:
        row, col = p
        offset_row = 0
        offset_col = 0
        for i in large_rows:
            if row >= i:
                offset_row += factor-1
        for i in large_cols:
            if col >= i:
                offset_col += factor-1
        if m[p] == '#':
            galaxies[g] = (row+offset_row, col+offset_col)
            g += 1

def find_dist(i,j):
    return abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

def find_dist_pairs(factor):
    recalculate_galaxies(factor)
    s = 0
    for i in range(g):
        for j in range(g):
            if i >= j:
                continue
            s += find_dist(i,j)
    print(f'factor {factor}:', s)

find_dist_pairs(2)
find_dist_pairs(1000000)
# find_dist_pairs(10)
# find_dist_pairs(100)
