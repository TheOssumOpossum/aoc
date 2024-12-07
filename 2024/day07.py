import sys
sys.path.append('../')
from lib.read import read
import math 

lines, groups = read(__file__)

s = 0
ss = 0

def canSum(nums, val, p2=False, cur=0):
    if cur == 0:
        cur = nums[0]
        nums = nums[1:]
    if len(nums) == 0:
        return val == cur
    n = nums[0]
    return canSum(nums[1:], val, p2, cur+n) or canSum(nums[1:], val, p2, cur*n) or (p2 and canSum(nums[1:], val, p2, cur*10**(int(math.log10(n))+1)+n))

# Line Parser
for i, line in enumerate(lines):
    res, nums = line.split(': ')
    nums = [int(x) for x in nums.split(' ')]
    res = int(res)
    if canSum(nums, res):
        s += res
    if canSum(nums, res, True):
        ss += res

print(s)
print(ss)
