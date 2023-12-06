import sys

day = 13
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

lines = f.read().splitlines()

#part 1
# a = None
# b = None

# def cmp(a,b,d=0):
#     # print("".join([" " for i in range(d*2)]) + "- Compare " + str(a) + " vs " + str(b))
#     if isinstance(a, int) and isinstance(b, int):
#         if a < b:
#             # print("  ".join([" " for i in range(d*2)]) + "- Left side is smaller, so inputs are in the right order")
#             return 1
#         if a == b:
#             return 0
#         if a > b:
#             # print("  ".join([" " for i in range(d*2)]) + "- Right side is smaller, so inputs are NOT in the right order")
#             return -1
#     elif isinstance(b, int):
#         return cmp(a, [b], d+1)
#     elif isinstance(a, int):
#         return cmp([a], b, d+1)
#     else:
#         for i in range(len(a)):
#             if len(b) <= i:
#                 # print("  ".join([" " for i in range(d*2)]) + "- Right side ran out of items, so inputs are NOT in the right order")
#                 return -1
#             x = cmp(a[i],b[i],d+1)
#             if x == 1:
#                 return 1
#             elif x == 0:
#                 continue
#             elif x == -1:
#                 return -1
#         if len(b) > len(a):
#             # print("  ".join([" " for i in range(d*2)]) + "- Left side ran out of items, so inputs are in the right order")
#             return 1
#         else:
#             return 0
        
# idx = 0
# s = 0
# for line in lines:
#     l = line.strip()
#     if l == '':
#         idx += 1
#         print("")
#         if cmp(a,b) == 1:
#             s += idx
#         a = b = None
#     elif a is None:
#         a = eval(l)
#     else:
#         b = eval(l)
# print(s)

#part 2
a = None
b = None
x = []

def cmp(a,b,d=0):
    # print("".join([" " for i in range(d*2)]) + "- Compare " + str(a) + " vs " + str(b))
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            # print("  ".join([" " for i in range(d*2)]) + "- Left side is smaller, so inputs are in the right order")
            return 1
        if a == b:
            return 0
        if a > b:
            # print("  ".join([" " for i in range(d*2)]) + "- Right side is smaller, so inputs are NOT in the right order")
            return -1
    elif isinstance(b, int):
        return cmp(a, [b], d+1)
    elif isinstance(a, int):
        return cmp([a], b, d+1)
    else:
        for i in range(len(a)):
            if len(b) <= i:
                # print("  ".join([" " for i in range(d*2)]) + "- Right side ran out of items, so inputs are NOT in the right order")
                return -1
            x = cmp(a[i],b[i],d+1)
            if x == 1:
                return 1
            elif x == 0:
                continue
            elif x == -1:
                return -1
        if len(b) > len(a):
            # print("  ".join([" " for i in range(d*2)]) + "- Left side ran out of items, so inputs are in the right order")
            return 1
        else:
            return 0
        
idx = 0
lines.append('[[2]]')
lines.append('[[6]]')
for line in lines:
    l = line.strip()
    if l != '':
        a = eval(l)
        ins = False
        for i in range(len(x)):
            if cmp(a, x[i]) == 1:
                x.insert(i, a)
                ins = True
                break
        if not ins:
            x.append(a)

s = 1
j = 0
for i in x:
    j += 1
    if i == [[2]] or i == [[6]]:
        s = j * s
print(s)
