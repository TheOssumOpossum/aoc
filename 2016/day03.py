import os
import sys
import re

f = open(f'{f"{os.path.dirname(os.path.realpath(__file__))}/../input/{os.path.dirname(os.path.realpath(__file__))[-4:]}/" if (len(sys.argv) >= 2 and sys.argv[1] == "1") else f"{os.path.dirname(os.path.realpath(__file__))}/"}{os.path.split(os.path.realpath(__file__))[1][3:5]}_{"data" if (len(sys.argv) >= 2 and sys.argv[1] == "1") else "sample" if len(sys.argv) < 2 or sys.argv[1] == "0" else "sample" + sys.argv[1]}.txt')
txt = f.read().strip()
lines = txt.split('\n')


#Part 1
s = 0
for i, line in enumerate(lines):
    nums = [int(x) for x in re.findall("\d+", line)]
    max_num = max(nums)
    nums.remove(max_num)
    if len(nums) < 2:
        assert False
    if sum(nums) > max_num:
        s += 1
print(s)

#Part 2
ss = 0
for i in range(0, len(lines), 3):
    nums1 = [int(x) for x in re.findall("\d+", lines[i])]
    nums2 = [int(x) for x in re.findall("\d+", lines[i+1])]
    nums3 = [int(x) for x in re.findall("\d+", lines[i+2])]
    t1 = [x[0] for x in [nums1, nums2, nums3]]
    t2 = [x[1] for x in [nums1, nums2, nums3]]
    t3 = [x[2] for x in [nums1, nums2, nums3]]
    max1 = max(t1)
    max2 = max(t2)
    max3 = max(t3)
    t1.remove(max1)
    t2.remove(max2)
    t3.remove(max3)
    if len(t1) < 2:
        assert False
    if len(t2) < 2:
        assert False
    if len(t3) < 2:
        assert False
    if sum(t1) > max1:
        ss += 1
    if sum(t2) > max2:
        ss += 1
    if sum(t3) > max3:
        ss += 1
print(ss)