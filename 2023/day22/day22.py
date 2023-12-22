import sys
from copy import deepcopy

day = '22'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip().splitlines()

bricks = []
for i, line, in enumerate(lines):
    l = line.strip()
    b1, b2 = l.split('~')
    x1, y1, z1 = map(int, b1.split(','))
    x2, y2, z2 = map(int, b2.split(','))
    if i < len('ABCDEFGHIJKLMNOQPRS'):
        brick_name = 'ABCDEFGHIJKLMNOPQRS'[i]
    else:
        brick_name = i
    bricks.append((x1, y1, z1, x2, y2, z2, brick_name))

def is_supported(b, world2):
    x1, y1, z1, x2, y2, z2, brick_name = b
    z = z1 - 1
    if z == 0:
        return True
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if (x, y, z) in world2:
                return True
    return False

def do_fall(bricks):
    did_fall = False
    new_bricks = []
    world = set()
    for (x1, y1, z1, x2, y2, z2, brick_name) in bricks:
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                world.add((x, y, z2))

    for b in bricks:
        x1, y1, z1, x2, y2, z2, brick_name = b
        if not is_supported(b, world):
            did_fall = True
            z1 -= 1
            z2 -= 1
            b2 = (x1, y1, z1, x2, y2, z2, brick_name)
            new_bricks.append(b2)
        else:
            new_bricks.append(b)
    return did_fall, new_bricks

did_fall = True
while did_fall:
    bricks = sorted(bricks, key=lambda x: x[2])
    did_fall, bricks = do_fall(bricks)
stacked_bricks = set(bricks)

disintegrate = 0
for i, b in enumerate(bricks):
    b_copy = deepcopy(bricks)
    del b_copy[i]
    did_fall, _ = do_fall(b_copy)
    if not did_fall:
        disintegrate += 1
print(disintegrate)

block_falls = 0
for i, b2 in enumerate(bricks):
    b_copy = deepcopy(bricks)
    del b_copy[i]
    did_fall = True
    while did_fall:
        did_fall, b_copy = do_fall(b_copy)
    new_stack = set(b_copy)
    block_falls += int((len(stacked_bricks ^ new_stack)-1) / 2)
print(block_falls)
