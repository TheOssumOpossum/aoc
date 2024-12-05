import sys
import re
import collections
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

rules = groups[0]
updates = groups[1]

must_come_before = collections.defaultdict(set)
s = 0
ss = 0

for r in rules.splitlines():
    a,b = map(int, r.split('|'))
    must_come_before[a].add(b)

for u in updates.splitlines():
    numbers = [int(x) for x in re.findall('\d+', u)]
    middle = numbers[len(numbers)//2]
    valid = True
    visited = set()
    for n in numbers:
        if len(must_come_before[n].intersection(visited)) != 0:
            valid = False
            break
        visited.add(n)
    if valid:
        s += middle
    else:
        remaining = set(numbers)
        new_list = []
        while remaining:
            for n in remaining:
                if len(must_come_before[n].intersection(remaining)) == (len(remaining) - 1):
                    new_list.append(n)
                    remaining.remove(n)
                    break
        middle = new_list[len(new_list)//2]
        ss += middle

print(s)
print(ss)
