import sys

day = '24'
sample = len(sys.argv) < 2 or sys.argv[1] == '0'

f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip().splitlines()

intersections = 0
m = {}
min_ = 7 if sample else 200000000000000
max_ = 27 if sample else 400000000000000
for i, line in enumerate(lines):
    l = line.strip()
    pos, vel = l.split('@ ')
    x,y,z = map(int, pos.split(', '))
    vx, vy, vz = map(int, vel.split(', '))
    m[i] = (x, y, z, vx, vy, vz)
    
import numpy as np
for a in m:
    for b in m:
        if a >= b:
            continue
        x, y, z, vx, vy, vz = m[a]
        x1, y1, z1, vx1, vy1, vz1 = m[b]
        slope = vy / vx
        slop1 = vy1 / vx1
        aa = np.array([[slope, -1],[slop1, -1]])
        bb = np.array([-y + slope * x,-y1 + slop1 * x1])
        if slop1 == slope:
            continue
        result = np.linalg.solve(aa,bb)
        xx = result[0]
        yy = result[1]
        if (min_ <= xx <= max_) and (min_ <= yy <= max_) and ((vx > 0 and xx > x) or (vx < 0 and xx < x)) and ((vx1 > 0 and xx > x1) or (vx1 < 0 and xx < x1)):
            intersections += 1
print(intersections)

        
import z3

solver = z3.Solver()
x, y, z, vx, vy, vz = map(z3.Int, ('x', 'y', 'z', 'vx', 'vy', 'vz'))

for i, (tx, ty, tz, tvx, tvy, tvz) in m.items():
    t = z3.Int(f"t{i}")
    solver.add(t > 0)
    solver.add(x + vx * t == tx + tvx * t)
    solver.add(y + vy * t == ty + tvy * t)
    solver.add(z + vz * t == tz + tvz * t)
if solver.check() == z3.sat:
    m = solver.model()
    a = [x,y,z]
    s = 0
    for i in a:
        s += int(str(m[i]))
    print(s)
