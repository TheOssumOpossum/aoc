# https://adventofcode.com/2020/day/15

day = "15"

txt = open("../input/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")
txt = txt.readlines()

#part 1 + 2

first_said = {}
second_said = {}
j = -1
last_num = -1
for l in txt:
    l = l.strip()
    nums = l.split(',')
    j = -1
    for i in range(len(nums)):
        j += 1
        num = int(nums[i])
        last_num = num
        first_said[last_num] = j

# while j < 2020-1: # PART 1
while j < 30000000-1: # PART 2
    j += 1
    # print(last_num)
    if last_num not in second_said:
        spoken_num = 0
        second_said[last_num] = j - 1
    else:
        spoken_num = second_said[last_num] - first_said[last_num]
    if spoken_num not in first_said:
        first_said[spoken_num] = j
    elif spoken_num not in second_said:
        second_said[spoken_num] = j
    else:
        first_said[spoken_num] = int(second_said[spoken_num])
        second_said[spoken_num] = j
    last_num = spoken_num
print(last_num)
