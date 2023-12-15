import sys
import re
import collections

day = '15'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip().splitlines()

s = 0
# part 1
for i, line in enumerate(lines):
    l = line.strip()
    steps = l.split(',')
    break

def hash(step):
    cur_val = 0
    for c in step:
        cur_val += ord(c)
        cur_val *= 17
        cur_val = cur_val % 256
    return cur_val

for step in steps:
    s += hash(step)
print(s)

# part 2
ss = 0
boxes = collections.defaultdict(list)
for step in steps:
    label = re.match("\w+", step)[0]
    box = hash(label)
    if '-' in step:
        for i, l in enumerate(boxes[box]):
            if l[0] == label:
                boxes[box] = boxes[box][:i] + boxes[box][i+1:]
    elif '=' in step:
        f = step[-1]
        for i, l in enumerate(boxes[box]):
            if l[0] == label:
                boxes[box][i] = (label, f)
                break
        else:
            boxes[box].append((label, f))

ss = 0
for box in boxes:
    for i, lens in enumerate(boxes[box]):
        ss += (box+1) * int(lens[1]) * (i+1)
print(ss)
