import sys
import collections
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

m = {}
freqs = collections.defaultdict(set)

# Grid Parser
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        m[(i,j)] = char
        if char != '.':
            freqs[char].add((i,j))
antifreqs = set()
antifreqs2 = set()
for f in freqs:
    antennas = freqs[f]
    for a in antennas:
        for b in antennas:
            if a == b:
                continue
            dx, dy = (a[0] - b[0], a[1] - b[1])
            if (a[0] + dx, a[1] + dy) in m:
                antifreqs.add((a[0] + dx, a[1] + dy))
            for k in range(0,50):
                if (a[0] + dx*k, a[1] + dy*k) in m:
                    antifreqs2.add((a[0] + dx*k, a[1] + dy*k))
                
print(len(antifreqs))
print(len(antifreqs2))
