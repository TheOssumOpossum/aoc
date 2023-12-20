import sys
import re
import collections
import functools

day = '20'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip().splitlines()

m = {}
inputs = collections.defaultdict(list)
for i, line in enumerate(lines):
    l = line.strip()
    source, dest = l.split('->')
    source = source.strip()
    dest = dest.strip()
    destinations = dest.split(', ')
    if source == 'broadcaster':
        start_sources = destinations
    else:
        switch = source[0]
        source = source[1:]
        m[source] = (False, switch, destinations)
        for d in destinations:
            inputs[d].append(source)
        
m['rx'] = (False, '!', [])
inputs_memory = {}

rxparents = set()
def getallparents(source):
    for p in inputs[source]:
        if m[p][1] == '%':
            rxparents.add(p)
        elif p in inputs['rx']:
            getallparents(p)
        else:
            rxparents.add(p)
getallparents('rx')
        
button_hits = 1000
hi = 0
lo = 0
q = collections.deque()
on = collections.defaultdict(set)
lcms = set()
lcm_found = False
i = -1
while not lcm_found:
    i += 1
    lo += 1
    for s in start_sources:
        q.append((False, s))
        lo += 1
    
    while q:
        incoming_high, source = q.popleft()
        if source not in m:
            continue
        memory, switch, destinations = m[source]
        if switch == '%' and not incoming_high:
            outgoing = not memory
            if outgoing:
                on[source].add(i)
            m[source] = (not memory, switch, destinations)
            for d in destinations:
                q.append((outgoing, d))
                if outgoing:
                    hi += 1
                else:
                    lo += 1
        elif switch == '&':
            outgoing = False
            for p in inputs[source]:
                if m[p][0] == False:
                   outgoing = True
                   break
            m[source] = (outgoing, switch, destinations)
            if outgoing:
                on[source].add(i)
            for d in destinations:
                q.append((outgoing, d))
                if outgoing:
                    hi += 1
                else:
                    lo += 1
        elif source == 'rx' and not lcm_found:
            for x in on:
                if x not in rxparents:
                    continue
                ls = sorted(on[x])
                diff = 0
                if len(on[x]) < 2:
                    continue
                for ii, y in enumerate(ls[1:2]):
                    diff = y - ls[ii]
                lcms.add(diff)
            if len(lcms) == len(rxparents):
                lcm_found = True
                import math
                print('rx is on:',math.lcm(*list(lcms)))
    
    if(i == button_hits-1):
        print(f'hi:{hi} lo:{lo}')
        print('1000 button presses:', hi*lo)
