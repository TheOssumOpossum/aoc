import sys
import re
import collections

day = '05'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample2' if sys.argv[1] == '2' else 'sample'))
lines = f.read().strip().splitlines()

#part 1
s = 0
for i, line in enumerate(lines):
    l = line.strip()
    if i == 0:
        seeds = [int(x) for x in re.findall("\d+",l)]
        
mins = []
for ss in seeds:
    prev = 'seeds'
    found = False
    s = ss
    for i, l in enumerate(lines[2:]):
        if '-to-' in l:
            found = False
        elif l != '' and found == False:
            dest_start, source_start, length = re.findall("\d+",l)
            dest_start = int(dest_start)
            source_start = int(source_start)
            length = int(length)
            if source_start <= s <= source_start+length:
                s = dest_start + ( s - source_start)
                found = True
        elif l == '':
            continue
    mins.append(s)

print(min(mins))        
        
#part 2
s = 0
windows = []
for i, line in enumerate(lines):
    l = line.strip()
    if i == 0:
        seeds = [int(x) for x in re.findall("\d+",l)]
        for i in range(0,len(seeds),2):
            windows.append((seeds[i],seeds[i]+seeds[i+1]-1))

next_windows = windows
new_windows = []
for i, l in enumerate(lines[2:]):
    if '-to-' in l:
        windows = next_windows
        next_windows = []
    elif l != '' and len(windows) > 0:
        dest_start, source_start, length = re.findall("\d+",l)
        dest_start = int(dest_start)
        source_start = int(source_start)
        length = int(length)
        new_windows = []
        for w in windows:
            before = during = after = None
            if w[0] < source_start:
                before = (w[0],min(source_start, w[1]))
                new_windows.append(before)
            if w[1] > source_start + length:
                after = (max(w[0],source_start+length), w[1])
                new_windows.append(after)
            if w[0] <= source_start <= w[1] or w[0] <= source_start+length <= w[1] or source_start <= w[0] <= source_start+length or source_start <= w[1] <= source_start+length:
                during = (max(source_start, w[0]),min(source_start+length,w[1]))
                during_length = during[1] - during[0]
                offset = (max(source_start, w[0]))-source_start
                during = (dest_start+(offset), dest_start+during_length+offset)
                next_windows.append(during)
        windows = new_windows
    elif l == '':
        next_windows.extend(windows)
        windows = next_windows

next_windows.extend(windows)
windows = next_windows

mins = float('inf')
for w in windows:
    mins = min(w[0],mins)
print(mins)
