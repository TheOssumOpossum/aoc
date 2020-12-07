# https://adventofcode.com/2020/day/0

day = "0"

txt = open("../input/day" + day + ".txt", "r")
txt = open("../tst/day" + day + "_test.txt", "r")

result = 0

for l in txt:
    if l == "\n":
        ''

    l = l.strip()

print(result)
