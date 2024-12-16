import sys
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

PRINT = False
directions = [(0,1),(-1,0),(0,-1),(1,0)] # right, up, left, down
directions_map = {y:directions[x] for x,y in enumerate('>^<v')}
m = {}
viz = set()
s = 0

# p1
# Grid Parser
for i, line in enumerate(groups[0].splitlines()):
    for j, char in enumerate(line):
        m[(i,j)] = char
        if char == '@':
            pos = (i, j)

# Character Parser
for i, line in enumerate(groups[1].splitlines()):
    for j, char in enumerate(line):
        d = directions_map[char]
        new_pos = pos
        pos_to_move = [pos]
        move = False
        while True:
            new_pos = (new_pos[0] + d[0], new_pos[1] + d[1])
            if m[new_pos] == '.':
                move = True
                break
            if m[new_pos] == '#':
                break
            if m[new_pos] == 'O':
                pos_to_move.append(new_pos)
        moved = set()
        if move:
            for k, x in enumerate(pos_to_move[::-1]):
                new_pos = (x[0] + d[0], x[1] + d[1])
                if k == len(pos_to_move) - 1:
                    m[x] = '.'
                    m[new_pos] = '@'
                    pos = new_pos
                    moved.add(new_pos)
                    moved.add(x)
                else:
                    m[new_pos] = 'O'
                    moved.add(new_pos)

        if PRINT:
            cur_row = 0
            for x in list(m):
                if x[0] != cur_row:
                    cur_row += 1
                    print('')
                if x in moved:
                    print('\033[94m' + m[x] + '\033[0m', end='')
                else:
                    print(str(m[x]),end='')        
            print('')
            print('')

for x in list(m):
    if m[x] == 'O':
        s += 100*x[0] + x[1]
print('p1', s)


#p2
m = {}
s = 0

# Grid Parser
for i, line in enumerate(groups[0].splitlines()):
    for j, char in enumerate(line):
        m[(i,j*2)] = char
        if char == '@':
            pos = (i, j*2)
            m[(i,j*2+1)] = '.'
        elif char == '#':
            m[(i,j*2+1)] = char
        elif char == 'O':
            m[(i,j*2)] = '['
            m[(i,j*2+1)] = ']'
        elif char == '.':
            m[(i,j*2+1)] = '.'

# Character Parser
for i, line in enumerate(groups[1].splitlines()):
    for j, char in enumerate(line):
        d = directions_map[char]
        all_pos_to_move = [pos]
        pos_to_move = [pos]
        move = True
        while True:
            new_pos_to_move = []
            for p in pos_to_move:
                new_pos = (p[0] + d[0], p[1] + d[1])
                if m[new_pos] == '#':
                    move = False
                    break
                if m[new_pos] == '[':
                    new_pos_to_move.append(new_pos)
                    if char == '^' or char == 'v':
                        new_pos_to_move.append((new_pos[0], new_pos[1] + 1))
                elif m[new_pos] == ']':
                    new_pos_to_move.append(new_pos)
                    if char == '^' or char == 'v':
                        new_pos_to_move.append((new_pos[0], new_pos[1] - 1))
            if move is False:
                break
            if len(new_pos_to_move) == 0:
                break
            pos_to_move = new_pos_to_move
            all_pos_to_move.extend(pos_to_move)
        moved = set()
        if move:
            for k, x in enumerate(all_pos_to_move[::-1]):
                new_pos = (x[0] + d[0], x[1] + d[1])
                if k == len(all_pos_to_move) - 1:
                    m[x] = '.'
                    m[new_pos] = '@'
                    pos = new_pos
                    moved.add(new_pos)
                    moved.add(x)
                else:
                    m[new_pos] = m[x]
                    moved.add(new_pos)
            for x in all_pos_to_move:
                if x not in moved:
                    m[x] = '.'

        if PRINT:
            cur_row = 0
            for x in list(m):
                if x[0] != cur_row:
                    cur_row += 1
                    print('')
                if x in moved:
                    print('\033[94m' + m[x] + '\033[0m', end='')
                else:
                    print(str(m[x]),end='')        
            print('')
            print('')

for x in list(m):
    if m[x] == '[':
        s += 100*x[0] + x[1]
print('p2', s)
