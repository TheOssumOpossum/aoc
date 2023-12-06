import sys

day = '06'
sample = True
if len(sys.argv) >= 2:
	if sys.argv[1] == '1':
		sample = False
	else:
		sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

lines = f.read().splitlines()

#part 1
# for line in lines:
# 	l = line.strip()
# 	x = []
# 	j = 0
# 	for a in l:
# 		j += 1
# 		if len(x) < 4:
# 			x.append(a)
# 		else:
# 			x.pop(0)
# 			x.append(a)
# 			if x[0] != x[1] and x[0] != x[2] and x[0] != x[3] and x[1] != x[2] and x[1] != x[3] and x[2] != x[3]:
# 				break
# 	print(j)

#part 2
for line in lines:
	l = line.strip()
	x = []
	j = 0
	for a in l:
		j += 1
		if len(x) < 14:
			x.append(a)
		else:
			works = True
			for i in range(len(x)):
				if x[i] in x[:i] + x[i+1:]:
					works = False
					break
			x.pop(0)
			x.append(a)
			if works:
				print(j-1)
				break
	# print(j)
