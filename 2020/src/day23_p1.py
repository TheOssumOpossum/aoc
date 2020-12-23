# https://adventofcode.com/2020/day/23

day = "23"

#part 1
txt = open("../input/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")
txt = txt.readlines()
txt.append("\n")
result = 0

moves = 100
cups = []

for l in txt:
    if l == "\n":
        ''
    l = l.strip()
    for c in l:
        cups.append(int(c))

current_cup = 0
for m in range(moves):
    picked_up = []
    current_cup_label = cups[current_cup]
    picked_up.append(cups[(current_cup+1)%9])
    picked_up.append(cups[(current_cup+2)%9])
    picked_up.append(cups[(current_cup+3)%9])
    for p in picked_up:
        cups.remove(p)

    i = 0
    for c in cups:
        if c == current_cup_label:
            new_cur_idx = i
            break
        i += 1

    modified_current_cup_label = current_cup_label
    found_dest = False
    decrement = 1
    while not found_dest:
        i = 0
        for c in cups:
            if c == modified_current_cup_label - decrement:
                found_dest = True
                dest_idx = i
            i += 1
        if found_dest:
            break
        if modified_current_cup_label - decrement < 0:
            modified_current_cup_label = 10
            decrement = 0
        decrement += 1
    new_cups = [0 for x in range(9)]

    iters = 0
    j = -1
    insert_idx = current_cup
    i = new_cur_idx
    while iters < 9:
        iters += 1
        if 0 <= j < 3:
            new_cups[insert_idx] = picked_up[j]
            j += 1
            new_cups[insert_idx] = cups[i]
            if cups[i] == modified_current_cup_label - decrement:
                j = 0
            i = (i+1)%6
        insert_idx = (insert_idx + 1) % 9


    cups = new_cups
    current_cup += 1
    if current_cup == 9:
        current_cup = 0

print(cups)
result = ""
found_one = False
for c in cups:
    if c == 1:
        found_one = True
    elif found_one:
        result += str(c)
for c in cups:
    if c == 1:
        found_one = False
    elif found_one:
        result += str(c)
print(result)
