import sys
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

safe = 0
safe2 = 0

def is_safe_check(n):
    increase = None
    is_safe = False
    for j in range(1, len(n)):
        diff = n[j] - n[j-1]
        if diff == 0:
            break
        if diff > 0:
            if increase is False:
                break
            if increase is None:
                increase = True
            if diff > 3:
                break
        else:
            if increase is True:
                break
            if increase is None:
                increase = False
            if diff < -3:
                break
    else:
        is_safe = True
    if is_safe:
        return 1
    else:
        return 0

for i, line in enumerate(lines):
    nums = line.split(' ')
    n = []
    for nn in nums:
        n.append(int(nn))
    increase = None
    is_safe = False
    safe += is_safe_check(n)
    if not is_safe_check(n):
        for i in range(len(n)):
            if is_safe_check(n[:i]+n[i+1:]):
                safe2 += 1
                break
    else:
        safe2 += 1

        

print(safe)
print(safe2)
