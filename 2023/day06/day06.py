import sys
import re

day = '06'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample2' if sys.argv[1] == '2' else 'sample'))
lines = f.read().strip().splitlines()

#part 1 and 2 - need to remove spaces for part 2
for i, line in enumerate(lines):
    l = line.strip()
    if i == 0:
        times = [int(x) for x in re.findall("\d+", l)]
    else:
        records = [int(x) for x in re.findall("\d+", l)]

print(times, records)
w = []
for i in range(len(times)):
    ways = 0
    for t in range(times[i]):
        if t * (times[i]-t) > records[i]:
            ways += 1
    w.append(ways)
print(w)
s = 1
for a in w:
    s *= a
print(s)
