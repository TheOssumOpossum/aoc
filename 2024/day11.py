import sys
sys.path.append('../')
from functools import lru_cache
from lib.read import read

lines, groups = read(__file__)
m = {}

@lru_cache(maxsize=None)
def calc_stones(n, blinks):
    if blinks == 0:
        return 1
    if n == 0:
        return calc_stones(1, blinks-1)
    elif len(str(n)) % 2 == 0:
        a = str(n)
        l = len(a)//2
        s1 = a[:l]
        s2 = a[l:]
        return calc_stones(int(s1), blinks-1) + calc_stones(int(s2), blinks - 1)
    else:
        return calc_stones(n*2024, blinks-1)

stones = [int(x) for x in lines[0].split(' ')]

for blinks in [25, 75]:
    ans = 0
    for s in stones:
        ans += calc_stones(s, blinks)
    print(ans)
