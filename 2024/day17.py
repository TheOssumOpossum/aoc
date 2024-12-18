import sys
import re
import collections
import functools
from copy import deepcopy
sys.path.append('../')
from lib.read import read
from lib.misc import transpose, rot90, rot270, flatten

lines, groups = read(__file__)

print(groups[1])
instructions = [int(x) for x in re.findall('\d', groups[1])]
a,b,c = [int(x) for x in re.findall('\d+', groups[0])]
print(a,b,c,instructions)
# print(ss)

def get_combo(n):
    if n <= 3:
        return (n, n)
    if n == 4:
        return (4, a)
    if n == 5:
        return (5, b)
    if n == 6:
        return (6, c)
    if n == 7:
        return (7, None)

i = 0
s = ''
m = collections.defaultdict(set)

# initial_a = 122_369_249_771_500
initial_a = 15560381
# initial_a = 0
prev = 0
unique_diffs = set()
while True:
    initial_a += 1766664
    a = initial_a
    # print(initial_a)
    # output = []
    j = 0
    i = 0
    b = c = 0
    
    while True:
        # print(i, instructions[i], instructions[i+1], a, b, c)
        opcode = instructions[i]
        # print(i, opcode)
        literal, combo = get_combo(instructions[i+1])
        if opcode == 0:
            # divide
            a = a // 2**combo
        elif opcode == 1:
            b = b ^ literal
        elif opcode == 2:
            b = combo % 8
        elif opcode == 3:
            if a != 0:
                i = literal
                continue
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            # s += str(combo % 8) + ','
            # print(combo%8)
            if instructions[j] != combo % 8:
                # print(j)
                break
            if j >= 5:
                print(j)
                print(initial_a - prev, initial_a)
                prev = initial_a
            # m[j].add(initial_a)
            j += 1
        elif opcode == 6:
            b = a // 2**combo
        elif opcode == 7:
            c = a // 2**combo
        i += 2
        if i >= len(instructions)-1:
            break
    # break
    if j == len(instructions):
        print(initial_a)
        break
    # if initial_a == 5_000_000:
    #     print(sorted(m[3]))
    #     for k in [3]:#, m.keys():
    #         # print(m)
    #         l = sorted(list(m[k]))
    #         prev = None
    #         for i, x in enumerate(l):
    #             if prev is not None:
    #                 # print(x - prev)
    #                 unique_diffs.add(x - prev)
                    
    #             prev = x
            
    #     print(unique_diffs)
    #     break
    # print(s[:-1])
    # print(a,b,c)
        
