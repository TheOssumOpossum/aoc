# https://adventofcode.com/2020/day/22

day = "22"

#part 1
# txt = open("../../input/2020/day" + day + ".txt", "r")
# # txt = open("../tst/day" + day + "_test.txt", "r")
# # txt = open("../tst/day" + day + "_test2.txt", "r")
# txt = txt.readlines()
# txt.append("\n")
# result = 0

# d1 = []
# d2 = []
# p1 = True
# for l in txt:
#     if l == "\n":
#         ''
#         continue
#     l = l.strip()
#     if l == "Player 2:":
#         p1 = False
#     if "Player" in l:
#         continue
#     if p1:
#         d1.append(int(l))
#     else:
#         d2.append(int(l))

# while len(d1) != 0 and len(d2) != 0:
#     b1 = d1.pop(0)
#     b2 = d2.pop(0)
#     print(b1,b2)
#     if b1 > b2:
#         d1.append(b1)
#         d1.append(b2)
#     else:
#         d2.append(b2)
#         d2.append(b1)
#     # print(d1,d2)
#     # break

# result = 0
# if len(d1) > 0:
#     print(d1)
#     mult = 1
#     for i in range(len(d1)-1,-1,-1):
#         result += d1[i]*mult
#         mult += 1
# else:
#     print(d2)
#     mult = 1
#     for i in range(len(d2)-1,-1,-1):
#         result += d2[i]*mult
#         mult += 1

# print(result)

#part 2
txt = open("../../input/2020/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")
# txt = open("../tst/day" + day + "_test2.txt", "r")
txt = txt.readlines()
txt.append("\n")
result = 0

d1 = []
d2 = []
p1 = True
for l in txt:
    if l == "\n":
        ''
        continue
    l = l.strip()
    if l == "Player 2:":
        p1 = False
    if "Player" in l:
        continue
    if p1:
        d1.append(int(l))
    else:
        d2.append(int(l))

import copy
import collections
d1 = collections.deque(d1)
d2 = collections.deque(d2)

results = {}

def battle(d1,d2,previous_rounds=set(),depth=0):
    while True:
        # print(depth,len(previous_rounds))
        if (tuple(d1),tuple(d2)) in results:
            return results[(tuple(d1),tuple(d2))]
        if (tuple(d1),tuple(d2)) in previous_rounds:
            if depth == 1:
                return d1
            return "p1"
        # print(len(previous_rounds))
        previous_rounds.add((tuple(d1),tuple(d2)))
        b1 = d1.popleft()
        b2 = d2.popleft()
        winner = None
        if len(d1) >= b1 and len(d2) >= b2:
            new_set = set()
            new_d1 = []
            new_d2 = []
            for i in range(b1):
                new_d1.append(d1[i])
            for i in range(b2):
                new_d2.append(d2[i])
            new_d1 = collections.deque(new_d1)
            new_d2 = collections.deque(new_d2)
            winner = battle(new_d1,new_d2,new_set,depth+1)
            results[(tuple(d1), tuple(d2))] = winner
        if winner != "p2" and (b1 > b2 or winner == "p1"):
            d1.append(b1)
            d1.append(b2)
        elif winner == "p2" or b2 > b1:
            d2.append(b2)
            d2.append(b1)
        if len(d1) == 0:
            # print(depth)
            if depth == 1:
                return d2
            return "p2"
        elif len(d2) == 0:
            # print(depth)
            if depth == 1:
                return d1
            return "p1"

prev_rounds = set()
winning_deck = battle(d1,d2,prev_rounds, depth=1)

result = 0
print(winning_deck)
if len(winning_deck) > 0:
    # print(winning_deck)
    mult = 1
    for i in range(len(winning_deck)-1,-1,-1):
        result += winning_deck[i]*mult
        mult += 1

print(result)
