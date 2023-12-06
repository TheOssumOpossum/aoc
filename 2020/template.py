# https://adventofcode.com/2020/day/0
import re

day = "0"

file_path = "../input/day{0}.txt".format(day)
file_path = "../tst/day{0}_test.txt".format(day)

txt = open(file_path, "r")
lines = txt.readlines().append("\n")

# dic = {}
# i = 0
# max_len = 0

for l in lines:
    #Handle empty line
    # if l == "\n":
        # ''

    l = l.strip()

    #Get max length of line
    # if len(l) > max_len:
    #     max_len = len(l)

    #Build 2D Map
    # j = 0
    # for c in l:
    #     dic[(i,j)] = c
    #     j += 1

    #Split line into terms by the delimiters
    # delimiters = [' ', ',' , '\:' ]
    # rex_split_string = ''.join([c + '|' for c in delimiters])
    # terms = re.split(rex_split_string, l)
    # dic[i] = terms

    #Increment row number
    i += 1

lines = i
