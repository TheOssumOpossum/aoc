import sys
import re
import collections

day = '07'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample2' if sys.argv[1] == '2' else 'sample'))
lines = f.read().strip().splitlines()

# part 1 and 2
hands = []
hands2 = []
vals = ([(x, i) for i, x in enumerate('123456789TJQKA')])
vals = dict(vals)

for i, line in enumerate(lines):
    l = line.strip()
    cards, bet = re.findall("\w+", l)
    bet = int(bet)
    
    js = 0
    counts = collections.defaultdict(int)
    j_counts = collections.defaultdict(int)
    for c in cards:
        counts[c] += 1
        if c == 'J':
            js += 1
            for v in vals:
                j_counts[v] += 1
            continue
        j_counts[c] += 1

    twos = 0
    threes = 0
    for v in counts.values():
        if v == 2:
            twos += 1
        if v == 3:
            threes += 1
    
    def analyze(hands, js, j_counts):
        j_counts = j_counts.values()
        if 5 in j_counts:
            hands.append((7, cards, bet))
        elif 4 in j_counts:
            hands.append((6, cards, bet))
        elif threes and twos or threes and js or twos == 2 and js == 1:
            hands.append((5, cards, bet))
        elif 3 in j_counts:
            hands.append((4, cards, bet))
        elif twos == 2:
            hands.append((3, cards, bet))
        elif 2 in j_counts:
            hands.append((2, cards, bet))
        else:
            hands.append((1, cards, bet))
            
    analyze(hands, 0, counts)
    analyze(hands2, js, j_counts)

def score(hands, vals):
    hands = sorted(hands, key = lambda x: (x[0], vals[x[1][0]], vals[x[1][1]], vals[x[1][2]], vals[x[1][3]], vals[x[1][4]]))
    s = 0
    for i, a in enumerate(hands):
        s += (i+1) * int(a[2])
    print(s)
    
score(hands, vals)
vals['J'] = -1
score(hands2, vals)
