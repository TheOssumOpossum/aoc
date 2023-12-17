import sys
import collections
import heapq

day = '17'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip().splitlines()

m = collections.defaultdict(list)
for i, line in enumerate(lines):
    l = line.strip()
    for j, c in enumerate(l):
        m[(i,j)] = int(c)
        
directions = [(0,1),(-1,0),(0,-1),(1,0)]
H = len(lines)-1
W = len(lines[0])-1

for MIN_DIST, MAX_DIST in [(0,3),(4,10)]:
    q = []
    viz = {}
    # Initialize heap to be the starting location, going right and down with travel distance 0 and total distance 0
    for r,c,d in [(0,0,0),(0,0,3)]:
        heapq.heappush(q,(0,r,c,d,0))
        
    while q:
        distance, row, col, direction, travel = heapq.heappop(q)
        if (row, col, direction, travel) in viz:
            continue
        if row == H and col == W and travel < MIN_DIST:
            continue
        viz[(row,col, direction, travel)] = distance
        
        def addToQueue(row, col, direction, travel=1):
            row += directions[direction][0]
            col += directions[direction][1]
            if (row,col) not in m:
                return
            heapq.heappush(q,(m[(row,col)] + distance, row, col, direction, travel))
            
        if travel < MAX_DIST:
            addToQueue(row, col, direction, travel + 1)
            
        if travel >= MIN_DIST:
            direction += 1
            direction %= 4
            addToQueue(row, col, direction)
            direction -= 2
            direction %= 4
            addToQueue(row, col, direction)
    
    min_dist = 999999
    for (row, col, a, b),distance in viz.items():
        if row == H and col == W:
            min_dist = min(min_dist, distance)
    
    print(min_dist)
