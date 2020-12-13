# https://adventofcode.com/2020/day/10

day = "10"

txt = open("../input/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test2.txt", "r")

#part 1
# nums = []
# for l in txt:
#     if l == "\n":
#         ''
#     l = l.strip()
#     nums.append(int(l))

# nums.sort()

# prev = 0
# ones = 0
# threes = 0
# for i in nums:
#     if i - prev == 1:
#         ones += 1
#     else:
#         threes += 1
#     prev = i
# threes += 1

# print(ones,threes,ones*threes)

#part 2
ways = {}
nums = []
the_max = 0
for l in txt:
    if l == "\n":
        ''
    l = l.strip()
    nums.append(int(l))
    if int(l) > the_max:
        the_max = int(l)

the_max += 3
nums.sort()
print(the_max)
ways[the_max] = 1
for i in range(len(nums)-1,-1,-1):
    cur_ways = 0
    if nums[i]+3 in ways:
        cur_ways += ways[nums[i]+3]
    if nums[i]+2 in ways:
        cur_ways += ways[nums[i]+2]
    if nums[i]+1 in ways:
        cur_ways += ways[nums[i]+1]
    ways[nums[i]] = cur_ways
cur_ways = 0
i = 0
if 3 in ways:
    cur_ways += ways[3]
if 2 in ways:
    cur_ways += ways[2]
if 1 in ways:
    cur_ways += ways[1]
ways[0] = cur_ways
print(ways[0])
