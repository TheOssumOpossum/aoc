# https://adventofcode.com/2020/day/0

day = "0"

txt = open("../../input/2020/day" + day + ".txt", "r")
txt = open("../tst/day" + day + "_test.txt", "r")
# txt = open("../tst/day" + day + "_test2.txt", "r")
txt = txt.readlines()
txt.append("\n")
result = 0

for l in txt:
    if l == "\n":
        ''
    l = l.strip()

print(result)
