# https://adventofcode.com/2020/day/18
day = "18"

#part 1
# txt = open("../input/day" + day + ".txt", "r")
# # txt = open("../tst/day" + day + "_test.txt", "r")
# txt = txt.readlines()
# txt.append("\n")
# summage = 0

# def find_match(l,lvl=0):
#     idx = -1
#     for i in l:
#         idx += 1
#         if i == '(':
#             lvl += 1
#         if i == ')':
#             lvl -= 1
#         if lvl == 0:
#             return idx

# def get_res(l,i=0,result=None,op=None):
#     c = l[i]
#     num = 0
#     while c.isnumeric():
#         num = num*10 + int(c)
#         i += 1
#         c = l[i]
#     if c == '(':
#         idx = find_match(l[i:])
#         res2 = get_res(l[i+1:idx+i]+"\n")
#         if op is None:
#             result = res2
#         elif op is "+":
#             result = result + res2
#         elif op is "*":
#             result = result * res2
#         return get_res(l,idx+i+1,result)
#     elif c == '+' or c == '*':
#         if result is None:
#             result = num
#         elif op == '+':
#             result = result + num
#         elif op == '*':
#             result = result * num
#         return get_res(l,i+1,result,c)
#     elif c == "\n" or c == ")":
#         if op is '+':
#             return result + num
#         elif op is '*':
#             return result * num
#         return result

# summage = 0
# for l in txt:
#     if l == "\n":
#         ''
#         continue
#     l = l.replace(" ","")
#     summage += get_res(l)

# print(summage)


#part2
txt = open("../input/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")
txt = txt.readlines()
txt.append("\n")
summage = 0

def find_match(l,lvl=0):
    idx = -1
    for i in l:
        idx += 1
        if i == '(':
            lvl += 1
        if i == ')':
            lvl -= 1
        if lvl == 0:
            return idx

def get_res(l,i=0,result=None,op=None):
    c = l[i]
    num = 0
    while c.isnumeric():
        num = num*10 + int(c)
        i += 1
        c = l[i]
    if c == '(':
        idx = find_match(l[i:])
        res2 = get_res(l[i+1:idx+i]+"\n")
        if op is None:
            result = res2
        elif op is "+":
            result = result + res2
        elif op is "*":
            result = result * res2
        return get_res(l,idx+i+1,result)
    elif c == '+' or c == '*':
        if result is None:
            result = num
        elif op == '+':
            result = result + num
        elif op == '*':
            result = result * num
        return get_res(l,i+1,result,c)
    elif c == "\n" or c == ")":
        if op is '+':
            return result + num
        elif op is '*':
            return result * num
        return result

def get_left_term(l,i):
    i -= 1
    str_builder = ""
    closers = 0
    while closers > 0 or (i >= 0 and (l[i] != "+" and l[i] != "*")):
        if i < 0:
            break
        if l[i] == ")":
            closers += 1
        if l[i] == "(":
            closers -= 1
            if closers == 0:
                break
        str_builder += l[i]
        i -= 1
    str_builder = str_builder[::-1]
    if i == -1:
        return "(" + str_builder
    else:
        return l[:i+1] + "(" + str_builder

def get_right_term(l,i):
    i += 1
    str_builder = ""
    openers = 0
    while openers > 0 or (i < len(l)-1 and (l[i] != "+" and l[i] != "*")):
        if l[i] =="\n":
            break
        if l[i] == "(":
            openers += 1
        if l[i] == ")":
            openers -= 1
            if openers == 0:
                break
        str_builder += l[i]
        i += 1
    if i == len(l):
        return  str_builder + ")"
    else:
        return str_builder + ")" + l[i:-1]

summage = 0
for l in txt:
    if l == "\n":
        ''
        continue
    l = l.replace(" ","")
    pluses = set()
    i = 0
    plus_found = 0
    while l[i] != "\n":
        if l[i] == "+":
            plus_found += 1
            if plus_found not in pluses:
                l = get_left_term(l,i) + "+" + get_right_term(l,i) + "\n"
                i = 0
                pluses.add(plus_found)
                plus_found = 0
                continue
        i += 1
    summage += get_res(l)

print(summage)
