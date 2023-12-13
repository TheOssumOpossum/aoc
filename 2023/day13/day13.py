import sys

day = '13'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip()

# part 1 and 2
mirrors = lines.split('\n\n')
s = 0
s2 = 0
for i, m in enumerate(mirrors):
    def find_reflection(lines, reject=0):
        ss = 0
        def find_split(lines, reject, factor=100):
            for row in range(len(lines)):
                th = lines[:row]
                bh = lines[row:]
                if not th or not bh:
                    continue
                
                def is_reflection():
                    reflect = True
                    for j in range(min(len(th), len(bh))):
                        if th[-(j+1)] != bh[j]:
                            reflect = False
                            return
                    if reflect:
                        ss = factor*len(th)
                        if ss != reject:
                            return ss

                ss = is_reflection()
                if ss:
                    return ss
            return reject
        
        ss = find_split(lines, reject)
        if ss != reject:
            return ss
        
        mirror_t = []
        lines_t = list(map(list, zip(*lines)))
        for x in lines_t:
            mirror_t.append(''.join(x))
        
        ss = find_split(mirror_t, reject, 1)
        if ss != reject:
            return ss
    
    mirror = m.split('\n')
    ss = find_reflection(mirror)
    s += ss
    found = False
    for row, line in enumerate(mirror):
        for col, char in enumerate(mirror[row]):
            og_row = mirror[row]
            mirror[row] = mirror[row][:col] + ('.' if char == '#' else '#') + mirror[row][col+1:]
            sss = find_reflection(mirror, ss)
            mirror[row] = og_row
            if sss:
                s2 += sss
                break
        else:
            continue
        break

print(s)
print(s2)
