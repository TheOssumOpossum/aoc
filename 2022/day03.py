day = '03'
sample = False

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

# part 1
# lines = f.read().splitlines()

# s = 0
# for line in lines:
# 	l = line.strip()
# 	x = set()
# 	for i in range(int(len(l)/2)):
# 		x.add(l[i])
# 	for i in range(int(len(l)/2),len(l)):
# 		letter = l[i]
# 		if letter in x:
# 			if ord(letter) <= ord('Z'):
# 				s += 27 + ord(letter) - ord('A')
# 			else:
# 				s += ord(letter) - ord('a') + 1
# 			break
# print(s)

#part 2
lines = f.read().splitlines()

s = 0
i = 0
first = set()
second = set()
third = set()
for line in lines:
	line = line.strip()
	if i == 0:
		first = set()
		for l in line:
			first.add(l)
		i += 1
		continue
	elif i == 1:
		second = set()
		for l in line:
			second.add(l)
		i += 1
		continue
	else:
		i = 0
		third = set()
		for l in line:
			third.add(l)
		for letter in first:
			if letter in second and letter in third:
				if ord(letter) <= ord('Z'):
					s += 27 + ord(letter) - ord('A')
				else:
					s += ord(letter) - ord('a') + 1
print(s)
