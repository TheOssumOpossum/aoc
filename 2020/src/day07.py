# https://adventofcode.com/2020/day/7
import re

day = "07"

# txt = open("../tst/day" + day + "_test2.txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")
txt = open("../input/day" + day + ".txt", "r")

# file_path = "../input/day{0}.txt".format(day)
# file_path = "../tst/day{0}_test.txt".format(day)

#part 1
# available_bags = {}

# for l in txt:
#     l = l.strip()
#     l = l[:-1]

#     terms = l.split()

#     quality_outer = terms[0]
#     color_outer = terms[1]

#     qty = terms[4]
#     qty = 0 if qty == "no" else qty
#     # print(qty)

#     if qty != 0:
#         containers = []
#         i = 4
#         while i < len(terms):
#             qty = terms[i]
#             i += 1
#             if terms[i] == "bags." or terms[i] == "bag.":
#                 break
#             containers.append(terms[i] + terms[i+1])
#             i += 3
#     # print(containers)

#         available_bags[quality_outer + color_outer] = containers
#     # print(available_bags)

# valid_bags = 0
# for bag in available_bags:
#     if bag == 'shinygold':
#         continue
#     visited = set()
#     # print(bag)
#     q = [bag]
#     while q:
#         b = q.pop(0)
#         # print(b)
#         if b in visited:
#             continue
#         visited.add(b)
#         if b == 'shinygold':
#             valid_bags += 1
#             break
#         else:
#             if b in available_bags:
#                 for bs in available_bags[b]:
#                     q.append(bs)

# print(valid_bags)

#part 2
available_bags = {}
qty_map = {}

for l in txt:
    l = l.strip()
    l = l[:-1]

    terms = l.split()

    quality_outer = terms[0]
    color_outer = terms[1]

    qty = terms[4]
    qty = 0 if qty == "no" else qty
    # print(qty)

    if qty != 0:
        containers = []
        i = 4
        while i < len(terms):
            qty = terms[i]
            i += 1
            if terms[i] == "bags." or terms[i] == "bag.":
                break
            containers.append(qty + ":" + terms[i] + terms[i+1])
            i += 3
    # print(containers)

        available_bags[quality_outer + color_outer] = containers
    # print(available_bags)

inside_bags = 0
multiply_stack = []
cur_multiple = 1
# for bag in available_bags:
#     if bag != 'shinygold':
#         continue
#     q = [bag]
#     while q:
#         b = q.pop(0)
#         if ':' in b:
#             print(b)
#             qty, b = b.split(':')
#             inside_bags += int(qty)*cur_multiple
#             cur_multiple *=
#         if b in available_bags:
#             for bs in available_bags[b]:
#                 q.append(bs)

# print(available_bags['fadedfuschia'])

def get_bags(bags):
    # print(bags)
    acc = 0
    if isinstance(bags, str):
        if bags in available_bags:
            return get_bags(available_bags[bags])
        else:
            return 1
    iters = -1
    for b in bags:
        iters += 1
        if ':' in b:
            qty, b = b.split(':')
        acc += 1 + int(qty) * get_bags(b)
    return acc - iters

print(get_bags(available_bags['shinygold'])-1)
