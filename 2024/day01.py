import sys
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

l1 = []
l2 = []
for l in lines:
    a,b = l.split('   ')
    l1.append(a)
    l2.append(b)

l1 = sorted(l1)
l2 = sorted(l2)

s = 0
for i in range(len(l1)):
    s += abs(int(l1[i])-int(l2[i]))
print(s)

x = {}
for a in l2:
    if a not in x:
        x[a] = 0
    x[a] += 1
    
sss = 0
for a in l1:
    if a not in x:
        continue
    sss += int(a) * x[a]

print(sss)
