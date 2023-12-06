# https://adventofcode.com/2020/day/6
import re

day = "06"

txt = open("../../input/2020/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")

#part1
# yes = 0
# yes_q = set()

# for l in txt:
#     if l == "\n":
#         yes += len(yes_q)
# #       print(yes_q)
#         yes_q = set()

#     else:
#         for c in l:
#             if c != '\n':
#                 yes_q.add(c)

# yes += len(yes_q)
# print(yes)


#part 2
yes = 0
yes_q = {}
cur_q = set()


yes_q = {'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,'m':1,'n':1,'p':1,'o':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1}

for l in txt:
    if l == "\n":
        for c in yes_q:
            if yes_q[c] == 1:
                # print("add",c)
                yes += 1
        # print(yes_q)
        # print("new")
        yes_q = {'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,'m':1,'n':1,'p':1,'o':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1}

    else:
        cur_q = set()
        for c in l:
            if c != '\n':
                cur_q.add(c)
                if c not in yes_q:
                    yes_q[c] = 1
        for q in yes_q:
            # print(q, yes_q, cur_q)
            if not(q in cur_q):
                # print("remove")
                yes_q[q] = 0

for c in yes_q:
    if yes_q[c] == 1:
        yes += 1
print(yes)
