# https://adventofcode.com/2020/day/2

import re

day = "02"

input = open("../input/day" + day + ".txt", "r")
# input = open("../tst/day" + day + "_test.txt", "r")

#part 1
# valid = 0
# for line in input:
#     min_term, max_term, char, password = re.split(' |\-|\: ', line[:-1])
#     count = 0
#     for c in password:
#         if c == char:
#             count += 1
#     # print(count, min_term, max_term, password, char)
#     if count >= int(min_term) and count <= int(max_term):
#         valid += 1
# print(valid)

#part 2
valid = 0
for line in input:
    first_term, second_term, char, password = re.split(' |\-|\: ', line[:-1])
    count = 0
    if password[int(first_term)-1] == char:
        if password[int(second_term)-1] != char:
            valid += 1
    else:
        if password[int(second_term)-1] == char:
            valid += 1
print(valid)
