# https://adventofcode.com/2020/day/5
import re

day = "05"

txt = open("../../input/2020/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")

#part 1
# max_seat_id = 0

# for line in txt:
#     lo = 0
#     hi = 127
#     l = 0
#     r = 7
#     for c in line:
#         if c == "F":
#             hi = (lo+hi)//2
#             continue
#         if c == "B":
#             lo = (lo+hi)//2
#         if c == "L":
#             r = (l+r)//2
#         if c == "R":
#             l = (l+r)//2
#     seat_id = hi*8 + r
#     if seat_id > max_seat_id:
#         max_seat_id = seat_id
# print(max_seat_id)

#part 2
seats = []

for line in txt:
    lo = 0
    hi = 127
    l = 0
    r = 7
    for c in line:
        if c == "F":
            hi = (lo+hi)//2
            continue
        if c == "B":
            lo = (lo+hi)//2
        if c == "L":
            r = (l+r)//2
        if c == "R":
            l = (l+r)//2
    seat_id = hi*8 + r
    seats.append(seat_id)
seats.sort()
i = 0
for i in range(1,len(seats)-1):
    if seats[i] + 2 == seats[i+1]:
        print (seats[i])
