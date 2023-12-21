import sys
import collections

day = '21'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip().splitlines()

# part 1 and part 2
m = {}
q = collections.deque()
for i, line in enumerate(lines):
    l = line.strip()
    for j, c in enumerate(l):
        m[(i,j)] = c
        if c == 'S':
            q.append((i,j))
        
steps = 0
total_p1 = 64
total = 26501365
directions = [(0,1),(-1,0),(0,-1),(1,0)]
viz = set()
quadratic = []
while steps < total:
    steps += 1
    new_q = collections.deque()
    viz = set()
    while len(q):
        x = q.popleft()
        row, col = x
        for d in directions:
            new_pos = (row+d[0], col+d[1])
            new_pos_ref = ((row+d[0])%len(lines), (col+d[1])%len(lines[0]))
            if m[new_pos_ref] != '#':
                if new_pos not in viz:
                    viz.add(new_pos)
                    new_q.append(new_pos)
    
    q = new_q
    if (steps % (len(lines)) == (total % len(lines))):
        print(f'step:{steps} \tpositions:{len(viz)}')
        quadratic.append(len(viz))
        if len(quadratic) == 3:
            import numpy
            xs = [i for i in range(3)]
            ys = [i for i in quadratic]
            f = numpy.polyfit(xs,ys,2)
            print(f'polynomial: {f}')
            x = (total - (total % len(lines))) // len(lines)
            part2 = int(f[0]*x**2 + f[1]*x + f[2])
            print(f'part2: {part2}')
            break
    if steps == total_p1:
        print(f'part1: {len(viz)}')
