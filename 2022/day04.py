import re

day = '04'
sample = False

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

# #part 1
# lines = f.read().splitlines()

# s = 0
# for line in lines:
# 	l = line.strip()
# 	if l == '':
# 		continue
# 	a,b,c,d = re.findall("\d+", line)
# 	a = int(a)
# 	b = int(b)
# 	c = int(c)
# 	d = int(d)

# 	if (a <= c and d <= b) or (c <= a and b <= d):
# 		s += 1

# print(s)

#part 2
lines = f.read().splitlines()

s = 0
for line in lines:
	l = line.strip()
	if l == '':
		continue
	a,b,c,d = re.findall("\d+", line)
	a = int(a)
	b = int(b)
	c = int(c)
	d = int(d)

	# if (a <= c and d <= b) or (c <= a and b <= d):
	# 	s += 1
	if (c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b):
		s += 1
		
print(s)
