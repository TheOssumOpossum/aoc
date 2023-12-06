# https://adventofcode.com/2020/day/19

day = "19"

#part 1
txt = open("../../input/2020/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")
txt = txt.readlines()
txt.append("\n")
result = 0

reading_rules = True
dic = {}
rulematcher = {}

# rulematcher[4] = ["a"]
# rulematcher[5] = ["b"]
rulematcher[33] = ["a"]
rulematcher[123] = ["b"]
def develop_rule():
    i = 0
    # while len(rulematcher) < 6:
    while len(rulematcher) < 137:
        i += 1
        i = i%len(dic)
        if i in rulematcher:
            continue
        if dic[i][1] == None:
            rules = dic[i][0]
            ready = True
            for r in rules:
                if r not in rulematcher:
                    ready = False
                    break
            if not ready:
                continue
            rulematcher[i] = ([],None)
            for r in rules:
                rulematcher[i][0].append(rulematcher[r])
        else:
            all_rules = []
            for j in dic[i][0]:
                all_rules.append(j)
            for j in dic[i][1]:
                all_rules.append(j)
            ready = True
            for r in all_rules:
                if r not in rulematcher:
                    ready = False
                    break
            if not ready:
                continue
            rulematcher[i] = ([],[])
            for r in dic[i][0]:
                rulematcher[i][0].append(rulematcher[r])
            for r in dic[i][1]:
                rulematcher[i][1].append(rulematcher[r])

ii = 0

def does_work(l,rule):
    global ii
    if rule is None:
        return False
    if isinstance(rule, str):
        res = l[ii] == rule
        ii += 1
        return res
    elif isinstance(rule, tuple):
        old_i = ii
        if does_work(l,rule[0]):
            return True
        else:
            ii = old_i
            return does_work(l,rule[1])
    elif isinstance(rule, list):
        list_works = True
        old_i = ii
        for j in range(len(rule)):
            list_works = list_works and does_work(l,rule[j])
            if not list_works:
                break
        if list_works:
            return list_works
        ii = old_i
        return list_works
    print('error')


first_time = True

for l in txt:
    if l == "\n":
        reading_rules = False
        continue
    l = l.strip()
    if reading_rules:
        x = l.split(":")
        rule_num = int(x[0])
        rules = x[1].split(" ")
        rules = rules[1:]
        first_rules = []
        second_rules = []
        first_set = True
        for r in rules:
            if r == '"a"':
                r = "a"
            elif r == '"b"':
                r = "b"
            if r == "|":
                first_set = False
                continue
            if first_set:
                if r.isnumeric():
                    r = int(r)
                first_rules.append(r)
            else:
                if r.isnumeric():
                    r = int(r)
                second_rules.append(r)
        if len(second_rules) > 0:
            dic[rule_num] = (first_rules, second_rules)
        else:
            dic[rule_num] = (first_rules, None)
    else:
        if first_time:
            develop_rule()
            first_time = False
        ii = 0
        if does_work(l,rulematcher[0]):
            if ii == len(l):
                result += 1
print(result)
