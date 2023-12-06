# https://adventofcode.com/2020/day/3

day = "03"

input = open("../../input/2020/day" + day + ".txt", "r")
# input = open("../tst/day" + day + "_test.txt", "r")

map = {}

i = 0
for l in input:
    j = 0
    for c in l:
        if c == '\n':
            continue
        map[(i,j)] = l[j]
        j += 1
    i += 1

# width = 11
width = 31

h = 0
l = 0
trees = 0

max_height = 322
# max_height = 10

while h < max_height+1:
    if map[(h,l)] == '#':
        trees += 1
    l += 3
    l = l%width
    h += 1
print(trees)
a1 = trees

#part 2
h = 0
l = 0
r = 1
d = 1
trees = 0
while h < max_height+1:
    if map[(h,l)] == '#':
        trees += 1
    l += r
    l = l%width
    h += d
a0 = trees

h = 0
l = 0
r = 5
d = 1
trees = 0
while h < max_height+1:
    if map[(h,l)] == '#':
        trees += 1
    l += r
    l = l%width
    h += d
a2 = trees

h = 0
l = 0
r = 7
d = 1
trees = 0
while h < max_height+1:
    if map[(h,l)] == '#':
        trees += 1
    l += r
    l = l%width
    h += d
a3 = trees

h = 0
l = 0
r = 1
d = 2
trees = 0
while h < max_height+1:
    if map[(h,l)] == '#':
        trees += 1
    l += r
    l = l%width
    h += d
a4 = trees

print(a0*a1*a2*a3*a4)
print(a0,a1,a2,a3,a4)
