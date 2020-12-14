# https://adventofcode.com/2020/day/14

day = "14"

txt = open("../input/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")
# txt = open("../tst/day" + day + "_test2.txt", "r")

#part1
# mask = 0
# results = {}
# for l in txt:
#     if l == "\n":
#         ''
#     l = l.strip()
#     l = l.split("=")
#     # print(l)
#     if l[0] == "mask ":
#         mask = l[1].strip()
#     else:
#         mem_location = l[0].split('[')
#         mem_location = mem_location[1].split(']')
#         mem_location = int(mem_location[0])

#         num = int(l[1])
#         numb = format(num, '#038b')

#         new_num = ""
#         for i in range(len(mask)):
#             j = i + 2
#             if mask[i] == "X":
#                 new_num += numb[j]
#             elif mask[i] == "1":
#                 new_num += '1'
#             elif mask[i] == "0":
#                 new_num += '0'
#         new_num = '0b' + new_num
#         new_num = int(new_num, 2)
#         results[mem_location] = new_num
#         # "{0:b}".format(37)

# sum = 0
# for i in results:
#     sum += results[i]
# print(sum)

#part 2

def permute(i,sum):
    global x_locations
    if i == len(x_locations):
        return sum
    mem_locations.append(permute(i+1,sum+(1<<x_locations[i])))
    mem_locations.append(permute(i+1,sum))

mask = 0
results = {}
x_locations = []
for l in txt:
    if l == "\n":
        ''
    l = l.strip()
    l = l.split("=")
    # print(l)
    if l[0] == "mask ":
        mask = l[1].strip()
        # print(mask)
    else:
        mem_location = l[0].split('[')
        mem_location = mem_location[1].split(']')
        mem_location = int(mem_location[0])

        sum_value = int(l[1])
        written_number = format(mem_location, '#038b')

        result = ""
        x_locations = []
        for i in range(len(mask)):
            j = i + 2
            if mask[i] == "X":
                result += "0"
                x_locations.append(35-i)
            elif mask[i] == "1":
                result += '1'
            elif mask[i] == "0":
                result += written_number[j]

        mem_locations = []

        result = '0b' + result
        base_number = int(result, 2)
        permute(0,base_number)
        # print(mem_locations)
        # print(result)
        for i in mem_locations:
            if i:
                results[i] = sum_value



sum = 0
for i in results:
    sum += results[i]
print(sum)
