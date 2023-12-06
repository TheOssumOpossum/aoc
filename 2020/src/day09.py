# https://adventofcode.com/2020/day/09

day = "09"

txt = open("../../input/2020/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")

#part 1
# result = 0
# preamble = 25
# dic = []
# i = 0

# def two_sum(ls, tgt):
#     dic = {}
#     for i in range(len(ls)):
#         dic[tgt-ls[i]] = i
#     for i in ls:
#         if i in dic and dic[i] != i:
#             return True
#     return False

# for l in txt:
#     l = l.strip()
#     num = int(l)
#     if i < preamble:
#         dic.append(num)
#         i += 1
#         continue
#     found = False
#     for j in dic:
#         if two_sum(dic, num):
#             dic.pop(0)
#             dic.append(num)
#             found = True
#             break
#     if not found:
#         print(num)
#         break

#part2
prev_not_found = False
first = 0
last = 0
invalid_num = 1492208709
# invalid_num = 127
dic = []
for l in txt:
    l = l.strip()
    dic.append(int(l))

yes_break = False
for i in range(len(dic)):
    if dic[i] > invalid_num:
        continue

    running_sum = dic[i]

    smallest = dic[i]
    biggest = dic[i]
    for j in range(i+1,len(dic)):
        if dic[j] > biggest:
            biggest = dic[j]
        if dic[j] < smallest:
            smallest = dic[j]

        running_sum += dic[j]
        if running_sum == invalid_num:
            print(smallest+biggest)
            yes_break = True
            break
        if running_sum > invalid_num:
            break
    if yes_break:
        break
