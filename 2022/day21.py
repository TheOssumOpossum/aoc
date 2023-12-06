import sys
import re
day = 21
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

lines = f.read().strip().splitlines()

#part 1
x = {}
for line in lines:
    l = line.strip()
    a = re.findall('[a-z]+', l)
    if len(a) == 1:
        x[a[0]] = int(re.findall('[-\d]+',l)[0])
    else:
        x[a[0]] = (a[1], re.findall('[-+/*]{1}', l)[0], a[2])

def getVal(monkey):
    global x
    if type(x[monkey]) == int:
        return x[monkey]
    else:
        return eval(str(str(getVal(x[monkey][0])) + x[monkey][1] + str(getVal(x[monkey][2]))))

print(int(getVal('root')))


#part 2
def getVal1(monkey):
    global x
    if monkey == 'root':
        return getVal1(x[monkey][0]), getVal1(x[monkey][2])
    if type(x[monkey]) == int:
        return x[monkey]
    else:
        return eval(str(str(getVal1(x[monkey][0])) + x[monkey][1] + str(getVal1(x[monkey][2]))))

top = 100000000000000
bot = 0
iii = 100000000000000

x['humn'] = top
s1, s2 = getVal1('root')
x['humn'] = bot
s3, s4 = getVal1('root')

if s1 > s2:
    iii = -iii
    bot = top
    top = 0

while True:
    # print(top,bot)

    x['humn'] = int((top+bot)/2)
    s5,s6 = getVal1('root')

    if s6 > s5:
        top = int((top+bot)/2)
    else:
        bot = int((top+bot)/2)
    if abs(top-bot) <= 1:
        # print(top,bot)
        break

x['humn'] = top
s1, s2 = getVal1('root')
x['humn'] = bot
s3, s4 = getVal1('root')
if s1 == s2:
    print(int(top))
if s3 == s4:
    print(int(bot))
