# https://adventofcode.com/2020/day/4
import re

day = "04"

txt = open("../../input/2020/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")

#part1
# valid = 0
# current_passport = {}
# for l in txt:
#     if l == "\n":
#         print(current_passport)
#         if "byr" in current_passport and "iyr" in current_passport and "eyr" in current_passport and "hgt" in current_passport and "hcl" in current_passport and "ecl" in current_passport and "pid" in current_passport:
#             if "cid" in current_passport:
#                 valid += 1
#                 current_passport= {}
#                 continue
#             valid += 1
#         current_passport = {}
#         continue

#     #Split line into terms by the delimiters
#     delimiters = [' ', '\:' ]
#     rex_split_string = ''.join([c + '|' for c in delimiters])[:-1]
#     terms = re.split(rex_split_string, l[:-1])

#     i = 0
#     while i < len(terms):
#         # print(i,terms,len(terms))
#         current_passport[terms[i]] = terms[i+1]
#         i += 2

# if "byr" in current_passport and "iyr" in current_passport and "eyr" in current_passport and "hgt" in current_passport and "hcl" in current_passport and "ecl" in current_passport and "pid" in current_passport:
#             if "cid" in current_passport:
#                 valid += 1
#                 current_passport= {}
#                 continue
#             valid += 1
# print(valid)

#part2
chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
eyes = ['amb','blu','brn','gry','grn','hzl','oth']
nums = ['0','1','2','3','4','5','6','7','8','9']
valid = 0
current_passport = {}
for l in txt:
    if l == "\n":
        if "byr" in current_passport and 1920 <= int(current_passport["byr"]) <= 2002:
            # print(current_passport["byr"],"valid")
            ''
        else:
            if "byr" in current_passport:
                # print(current_passport["byr"],"invalid")
                ''
            current_passport = {}
            continue
        if "iyr" in current_passport and (2010 <= int(current_passport["iyr"]) <= 2020):
            "asd"
            # print(current_passport["iyr"],"valid",2010 <= int(current_passport["iyr"]) <= 2020)
        else:
            # if "iyr" in current_passport:
                # print(current_passport["iyr"],"invalid")
            current_passport = {}
            continue
        if "eyr" in current_passport and (2020 <= int(current_passport["eyr"]) <= 2030):
            "asd"

        else:
            # if "hgt" in current_passport:
                # print(current_passport["hgt"],"invalid")
            current_passport = {}
            continue
        if "hgt" in current_passport and 4 <= len(current_passport["hgt"]) <= 5 and ((len(current_passport["hgt"]) == 5 and current_passport["hgt"][3:5] == "cm" and 150 <= int(current_passport["hgt"][0:3]) <= 193) or (current_passport["hgt"][2:4] == "in" and 59 <= int(current_passport["hgt"][0:2]) <= 76)):
            # print(current_passport["hgt"])
            # print("hgt valid")
            "asd"
        else:
            current_passport = {}
            continue
        if "hcl" in current_passport and current_passport["hcl"][0] == '#' and len(current_passport["hcl"]) == 7 and (current_passport["hcl"][1] in chars and current_passport["hcl"][2] in chars and current_passport["hcl"][3] in chars and current_passport["hcl"][4] in chars and current_passport["hcl"][5] in chars and current_passport["hcl"][6] in chars):
            # print("hcl valid")
            "asd"
        else:
            current_passport = {}
            continue
        if "ecl" in current_passport and current_passport["ecl"] in eyes:
            # print("ecl valid")
            "asd"
        else:
            current_passport = {}
            continue
        if "pid" in current_passport and len(current_passport["pid"]) == 9 and current_passport["pid"][0] in nums and current_passport["pid"][1] in nums and current_passport["pid"][2] in nums and current_passport["pid"][3] in nums and current_passport["pid"][4] in nums and current_passport["pid"][5] in nums and current_passport["pid"][6] in nums and current_passport["pid"][7] in nums and current_passport["pid"][8] in nums:
            valid += 1
            # print("pid valid")
            current_passport = {}
        else:
            current_passport = {}
            continue
        continue

    #Split line into terms by the delimiters
    delimiters = [' ', '\:' ]
    rex_split_string = ''.join([c + '|' for c in delimiters])[:-1]
    terms = re.split(rex_split_string, l[:-1])

    i = 0
    while i < len(terms):
        # print(i,terms,len(terms))
        current_passport[terms[i]] = terms[i+1]
        i += 2

if "byr" in current_passport and 1920 <= int(current_passport["byr"]) <= 2002:
    # print(current_passport["byr"],"valid")
    ''
else:
    if "byr" in current_passport:
        # print(current_passport["byr"],"invalid")
        ''
    current_passport = {}
if "iyr" in current_passport and (2010 <= int(current_passport["iyr"]) <= 2020):
    "asd"
    # print(current_passport["iyr"],"valid",2010 <= int(current_passport["iyr"]) <= 2020)
else:
    # if "iyr" in current_passport:
        # print(current_passport["iyr"],"invalid")
    current_passport = {}
if "eyr" in current_passport and (2020 <= int(current_passport["eyr"]) <= 2030):
    "asd"

else:
    # if "hgt" in current_passport:
        # print(current_passport["hgt"],"invalid")
    current_passport = {}
if "hgt" in current_passport and 4 <= len(current_passport["hgt"]) <= 5 and ((len(current_passport["hgt"]) == 5 and current_passport["hgt"][3:5] == "cm" and 150 <= int(current_passport["hgt"][0:3]) <= 193) or (current_passport["hgt"][2:4] == "in" and 59 <= int(current_passport["hgt"][0:2]) <= 76)):
    # print(current_passport["hgt"])
    # print("hgt valid")
    "asd"
else:
    current_passport = {}
if "hcl" in current_passport and current_passport["hcl"][0] == '#' and len(current_passport["hcl"]) == 7 and (current_passport["hcl"][1] in chars and current_passport["hcl"][2] in chars and current_passport["hcl"][3] in chars and current_passport["hcl"][4] in chars and current_passport["hcl"][5] in chars and current_passport["hcl"][6] in chars):
    # print("hcl valid")
    "asd"
else:
    current_passport = {}
if "ecl" in current_passport and current_passport["ecl"] in eyes:
    # print("ecl valid")
    "asd"
else:
    current_passport = {}
if "pid" in current_passport and len(current_passport["pid"]) == 9 and current_passport["pid"][0] in nums and current_passport["pid"][1] in nums and current_passport["pid"][2] in nums and current_passport["pid"][3] in nums and current_passport["pid"][4] in nums and current_passport["pid"][5] in nums and current_passport["pid"][6] in nums and current_passport["pid"][7] in nums and current_passport["pid"][8] in nums:
    valid += 1
    # print("pid valid")
    current_passport = {}
else:
    current_passport = {}
print(valid)
