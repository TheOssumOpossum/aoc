import sys
import re
import collections

day = '04'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample2' if sys.argv[1] == '2' else 'sample'))
lines = f.read().strip().splitlines()

# #part 1
# s = 0
# for i, line in enumerate(lines):
#     l = line.strip()
#     a,b = l.split(':')
#     b,c = b.split('|')
#     # print(b)
#     # print(c)
#     n1 = re.findall("\d+",b)
#     n2 = re.findall("\d+",c)
#     n1 = set(n1)
#     n2 = set(n2)
#     n3 = n1 & n2
#     if len(n3) == 0:
#         continue
#     s += 2**(len(n3)-1)
# print(s)
    

#part 2
s = 0
cards = collections.defaultdict(lambda:1)
for i, line in enumerate(lines):
    l = line.strip()
    a,b = l.split(':')
    b,c = b.split('|')
    n1 = re.findall("\d+",b)
    n2 = re.findall("\d+",c)
    n1 = set(n1)
    n2 = set(n2)
    n3 = n1 & n2
    wins = len(n3)
    s += cards[i]
    for j in range(1,wins+1):
        cards[i+j] += 1*cards[i]
print(s)
    