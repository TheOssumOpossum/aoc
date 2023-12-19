import sys
import re
import collections
import functools

day = '19'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip().split('\n\n')

workflows, candidates = lines

# parse
r = collections.defaultdict(list)
for w in workflows.splitlines():
    name, rest = w[:-1].split('{')
    rules = rest.split(',')
    for rule in rules:
        if ':' in rule:
            r[name].append(tuple(rule.split(':')))
        else:
            r[name].append((None, rule))

# part 1
def process():
    name = 'in'
    i = 0
    while name != 'A' and name != 'R':
        rule,next = r[name][i]
        if rule is None:
            name = next
            i = 0
            continue
        result = eval(rule)
        if result:
            name = next
            i = 0
        else:
            i += 1
    if name == 'A':
        return x+m+a+s
    return 0

# part 2
from copy import deepcopy
p2 = 0
xmas_map = {x:y for y,x in enumerate('xmas')}
def process2(min_ranges=[1 for _ in range(4)], max_ranges=[4000 for _ in range(4)], name='in', i = 0):
    global p2
    diffs = list(map(lambda x,y: y - x + 1,min_ranges, max_ranges))
    for d in diffs:
        if d < 0:
            return
    if name == 'A':
        p2 += functools.reduce(lambda x,y : x*y, diffs)
        return
    if name == 'R':
        return 
    rule, next = r[name][i]
    if rule is None:
        process2(min_ranges, max_ranges, next)
        return
    idx = xmas_map[rule[0]]
    number = int(rule[2:])
    if '>' in rule:
        min_ranges_og = deepcopy(min_ranges)
        max_ranges_og = deepcopy(max_ranges)
        
        min_ranges[idx] = max(min_ranges[idx], number+1)
        process2(min_ranges, max_ranges_og, next)
        
        max_ranges[idx] = min(max_ranges[idx], number)
        process2(min_ranges_og, max_ranges, name, i+1)
    if '<' in rule:
        min_ranges_og = deepcopy(min_ranges)
        max_ranges_og = deepcopy(max_ranges)
        
        max_ranges[idx] = min(max_ranges[idx], number-1)
        process2(min_ranges_og, max_ranges, next)
            
        min_ranges[idx] = max(min_ranges[idx], number)
        process2(min_ranges, max_ranges_og, name, i+1)

ss = 0
for c in candidates.splitlines():
    x,m,a,s = [int(x) for x in re.findall("\d+",c)]
    ss += process()
print(ss)

process2()
print(p2)
