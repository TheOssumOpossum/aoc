# https://adventofcode.com/2020/day/1

input = open("day01.txt", "r")
# input = open("day01_test.txt", "r")

#part 1
nums = set()
for n in input:
    n = int(n)
    if n in nums:
        print(n*(2020-n))
        break
    else:
        nums.add(2020-n)


#part 2
nums = {}
nums_list = []
i = 0
for n in input:
    n = int(n)
    nums[2020-n] = i
    i += 1
    nums_list.append(n)

borked = False
for i in range(len(nums_list)):
    if borked:
        break
    for j in range(i,len(nums_list)):
        tmp_sum = nums_list[i] + nums_list[j]
        if tmp_sum in nums and nums[tmp_sum] != i and nums[tmp_sum] != j:
            print(nums_list[i]*nums_list[j]*(2020-tmp_sum))
            borked = True
            break