import sys
import re
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

# Part 1
s = 0
def validTriangle(sides):
    max_num = max(sides)
    sides.remove(max_num)
    assert len(sides) == 2
    return 1 if sum(sides) > max_num else 0

for i, line in enumerate(lines):
    nums = [int(x) for x in re.findall("\d+", line)]
    s += validTriangle(nums)
print(s)

# Part 2
ss = 0
for i in range(0, len(lines), 3):
    nums1 = [int(x) for x in re.findall("\d+", lines[i])]
    nums2 = [int(x) for x in re.findall("\d+", lines[i+1])]
    nums3 = [int(x) for x in re.findall("\d+", lines[i+2])]
    t1 = [x[0] for x in [nums1, nums2, nums3]]
    t2 = [x[1] for x in [nums1, nums2, nums3]]
    t3 = [x[2] for x in [nums1, nums2, nums3]]
    ss += validTriangle(t1)
    ss += validTriangle(t2)
    ss += validTriangle(t3)
print(ss)
