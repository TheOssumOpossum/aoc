# https://adventofcode.com/2020/day/16

day = "16"
#part 1
# txt = open("../../input/2020/day" + day + ".txt", "r")
# # txt = open("../tst/day" + day + "_test.txt", "r")
# txt = txt.readlines()
# txt.append("\n")

# all_nums = []
# criteria = {}
# your_ticket = True
# for l in txt:
#     if l == "\n":
#         ''
#     l = l.strip()
#     if "," in l: #numbers
#         if your_ticket:
#             your_ticket = False
#             continue
#         nums = l.split(",")
#         for n in nums:
#             all_nums.append(int(n))
#     if ":" in l and l[-1] != ":": #criteria
#         txt = l.split(":")
#         criterion = txt[0].strip()
#         txt = txt[1].split("or")
#         for i in txt:
#             i.strip()
#             start, end = i.split('-')
#             start.strip()
#             end.strip()
#             if criterion not in criteria:
#                 criteria[criterion] = []
#             criteria[criterion].append([int(start),int(end)])
#             # print(criteria)
# sum = 0
# for n in all_nums:
#     valid = False
#     for c in criteria:
#         if criteria[c][0][0] <= n <= criteria[c][0][1] or criteria[c][1][0] <= n <= criteria[c][1][1]:
#             valid = True
#             break
#     if valid == False:
#         sum += n
# print(sum)

#part 2
txt = open("../../input/2020/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")
txt = txt.readlines()
txt.append("\n")

tickets = {}
criteria = {}
t = 0
for l in txt:
    if l == "\n":
        ''
    l = l.strip()
    if "," in l: #numbers
        nums = l.split(",")
        ticket_nums = []
        for n in nums:
            ticket_nums.append(int(n))
        tickets[t] = ticket_nums
        t += 1
    if ":" in l and l[-1] != ":": #criteria
        txt = l.split(":")
        criterion = txt[0].strip()
        txt = txt[1].split("or")
        for i in txt:
            i.strip()
            start, end = i.split('-')
            start.strip()
            end.strip()
            if criterion not in criteria:
                criteria[criterion] = []
            criteria[criterion].append([int(start),int(end)])
            # print(criteria)

sum = 0
for ticket in tickets:
    t = tickets[ticket]
    valid_cols = 0
    for n in t:
        for c in criteria:
            if criteria[c][0][0] <= n <= criteria[c][0][1] or criteria[c][1][0] <= n <= criteria[c][1][1]:
                valid_cols += 1
                break
    if valid_cols != 20:
        tickets[ticket] = None

# sum = 0
# sum2 = 0
# for t in tickets:
#     if tickets[t] == None:
#         sum += 1
#     else:
#         sum2 += 1
# print(sum,sum2)

definite_map = {}
found_criteria = set()
do_print = True
while True:
    if len(found_criteria) == 20:
        break
    for i in range(20):
        could_map = []
        if i in definite_map:
            continue
        for c in criteria:
            if c in found_criteria:
                continue
            criteria_valid = True
            for t in tickets:
                tkt = tickets[t]
                if tkt == None:
                    continue
                n = tkt[i]
                if (criteria[c][0][0] > n or n > criteria[c][0][1]) and (criteria[c][1][0] > n or n > criteria[c][1][1]):
                    criteria_valid = False
                    break
            if criteria_valid:
                could_map.append(c)
        if len(could_map) == 1:
            definite_map[i] = could_map[0]
            found_criteria.add(could_map[0])
            print(could_map[0], i)

result = 1
for i in definite_map:
    if 'departure' in definite_map[i]:
        result *= tickets[0][i]
print(result)
