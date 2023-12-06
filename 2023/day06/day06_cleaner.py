import sys
import re
import functools

day = '06'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample2' if sys.argv[1] == '2' else 'sample'))
lines = f.read().strip().splitlines()

#part 1 and 2 - sandwich: could probably binary search
for i, line in enumerate(lines):
    l = line.strip()
    if i == 0:
        times1 = [int(x) for x in re.findall("\d+", l)]
        times2 = [int(functools.reduce(lambda a,b: a+b, re.findall("\d+", l)))]
    else:
        records1 = [int(x) for x in re.findall("\d+", l)]
        records2 = [int(functools.reduce(lambda a,b: a+b, re.findall("\d+", l)))]

for x in [(times1, records1), (times2, records2)]:
    times = x[0]
    records = x[1]
    s = 1
    for i, time in enumerate(times):
        start = time
        end = 0
        for j in range(time):
            if j * (time-j) > records[i]:
                start = j
                break
        for j in range(time,-1,-1):
            if j * (time) > records[i]:
                end = j+1
                break
        s*= (end-start)
    print(s)
