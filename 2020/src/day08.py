# https://adventofcode.com/2020/day/8

day = "08"

txt = open("../../input/2020/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")

#part1
# result = 0

# instructions = {}
# run = set()
# i = -1

# for l in txt:
#     i += 1
#     l = l.strip()
#     instruction, num = l.split(' ')
#     num = int(num)
#     instructions[i] = (instruction, num)

# print(instructions)

# i = 0
# acc = 0
# while True:
#     if i in run:
#         break
#     run.add(i)
#     instruction = instructions[i]
#     print(instruction)
#     if instruction[0] == "nop":
#         i += 1
#         continue
#     elif instruction[0] == "jmp":
#         i += instruction[1]
#         continue
#     elif instruction[0] == "acc":
#         acc += instruction[1]
#         i += 1

# print(acc)

#part2
result = 0

instructions = {}
i = -1

for l in txt:
    i += 1
    l = l.strip()
    instruction, num = l.split(' ')
    num = int(num)
    instructions[i] = (instruction, num)
max_lines = i
print(max_lines)

for ins in instructions:

    run = set()
    if instructions[ins][0] == "acc":
        continue
    was_jmp = False
    if instructions[ins][0] == "jmp":
        was_jmp = True
        instructions[ins] = ("nop", instructions[ins][1])
    else:
        instructions[ins] = ("jmp", instructions[ins][1])
    yes_break = False
    acc = 0
    i = 0
    # print(instructions)
    while True:
        if i == max_lines+1:
            yes_break = True
            # print(acc)
            break
        if i in run:
            break
        run.add(i)
        instruction = instructions[i]
        # print(instruction)
        if instruction[0] == "nop":
            i += 1
            continue
        elif instruction[0] == "jmp":
            i += instruction[1]
            continue
        elif instruction[0] == "acc":
            acc += instruction[1]
            # print(i, acc, instruction[1])
            i += 1
    if was_jmp:
        instructions[ins] = ("jmp", instructions[ins][1])
    else:
        instructions[ins] = ("nop", instructions[ins][1])
    if(yes_break):
        break

print(acc)
