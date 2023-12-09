import sys
import re
import collections

day = '09'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample2' if sys.argv[1] == '2' else 'sample'))
lines = f.read().strip().splitlines()

# part 1 and 2
s = 0
ss = 0
for i, line in enumerate(lines):
    hist = collections.defaultdict(list)
    l = line.strip()
    nums = [int(x) for x in re.findall("-?\d+",l)]
    hist[0] = nums
    j = 0
    while set(hist[j]) ^ set([0]):
        new_nums = []
        nums = hist[j]
        for k, n in enumerate(nums[:-1]):
            new_nums.append(nums[k+1] - n)
        hist[j+1] = new_nums
        j += 1
    last = 0
    for k in range(j-1, -1, -1):
        last = hist[k][-1] + hist[k+1][-1]
        first = hist[k][0] - hist[k+1][0]
        hist[k] = [first] + hist[k] + [last]
    s += last
    ss += first
print(s)
print(ss)
