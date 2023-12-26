import collections
import re
import random
import sys
from copy import deepcopy

day = '25'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip().splitlines()

# lines = inp2.strip().splitlines()
m = collections.defaultdict(set)
connections = set()
nodes = set()
for l in lines:
    components = re.findall("\w+",l)
    start = components[0]
    ends = components[1:]
    for e in ends:
        m[start].add(e)
        m[e].add(start)
        connections.add((start,e))
        nodes.add(start)
        nodes.add(e)
  
counts = collections.defaultdict(int)

def path(i,j):
    q = collections.deque()
    q.append((i,[i]))
    viz = set()
    while q:
        cur, p = q.popleft()
        if cur == j:
            for a in p:
                counts[a] += 1
            return
        for n in m[cur]:
            if n not in viz:
                viz.add(n)
                p2 = deepcopy(p)
                p2.append(n)
                q.append((n, p2))

node_map = {}
for i, a in enumerate(nodes):
    node_map[i] = a

for _ in range(300):
    i = random.randint(0, len(nodes)-1)
    j = i
    while i == j:
      j = random.randint(0, len(nodes)-1)
    j = node_map[j]
    i = node_map[i]
    path(i,j)

hot_connections = []

for n in counts:
    count = counts[n]
    for e in m[n]:
      hot_connections.append((count, (n, e)))
      
hot_connections = sorted(hot_connections, reverse=True)
hot_connections = [x[1] for x in hot_connections]
 
def expand(n):
    viz = set()
    q = collections.deque()
    q.append(n)
    while q:
        cur = q.popleft()
        viz.add(cur)
        for n2 in m[cur]:
            if n2 not in viz:
                q.append(n2)
                viz.add(n2)
    return len(viz)

lim = 30
ans = 1
stop = False
for i, c1 in enumerate(hot_connections):
    if stop:
        break
    s1, e1 = c1
    m[s1].remove(e1)
    m[e1].remove(s1)
    for j, c2 in enumerate(hot_connections):
        if j > lim:
            continue
        if stop:
            break
        if i >= j:
            continue
        s2, e2 = c2
        try:
          m[s2].remove(e2)
          m[e2].remove(s2)
        except KeyError:
            continue
        for k, c3 in enumerate(hot_connections):
            if k > lim:
                continue
            if stop:
                break
            if j >= k:
                continue
            s3, e3 = c3
            try:
              m[s3].remove(e3)
              m[e3].remove(s3)
            except KeyError:
                continue
            for n in nodes:
                    size = expand(n)
                    if size != len(nodes):
                          ans *= size
                          ans *= len(nodes) - (size)
                          stop = True
                          break
                    else:
                        break
            m[s3].add(e3)
            m[e3].add(s3)
        m[s2].add(e2)
        m[e2].add(s2)
    m[s1].add(e1)
    m[e1].add(s1)
print(ans)
