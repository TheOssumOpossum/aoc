# https://adventofcode.com/2020/day/1
import re

day = "0"

# txt = open("../input/day" + day + ".txt", "r")
txt = open("../tst/day" + day + "_test.txt", "r")

dic = {}
i = 0
max_len = 0

for l in txt:
    #Get max length of line
    # if len(l) > max_len:
    #     max_len = len(l)

    #Build 2D Map
    # j = 0
    # for c in l:
    #     if c == '\n':
    #         continue
    #     dic[(i,j)] = c
    #     j += 1

    #Split line into terms by the delimiters
    # delimiters = [' ', ',' , '\:' ]
    # rex_split_string = ''.join([c + '|' for c in delimiters])[:-1]
    # terms = re.split(rex_split_string, l[:-1])
    # dic[i] = terms

    #Increment row number
    i += 1

lines = i
