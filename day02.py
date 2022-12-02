day = '02'
sample = False

f = open('day{}_{}.txt'.format(day,'sample' if sample else 'data'))

#part 1
# lines = f.readlines()
# score = 0

# for line in lines:
# 	l = line.strip()
# 	elf, you = l.split(' ')
# 	if you == 'Y':
# 		score += 2
# 		if elf == 'A':
# 			score += 6
# 		if elf == 'B':
# 			score += 3
# 	if you == 'X':
# 		score += 1
# 		if elf == 'A':
# 			score += 3
# 		if elf == 'C':
# 			score += 6
# 	if you == 'Z':
# 		score += 3
# 		if elf == 'C':
# 			score += 3
# 		if elf == 'B':
# 			score += 6

# print(score)

#part 2
lines = f.readlines()
score = 0

for line in lines:
	l = line.strip()
	elf, you = l.split(' ')
	if you == 'Y':
		score += 3
		if elf == 'A':
			score += 1
		elif elf == 'B':
			score += 2
		elif elf == 'C':
			score += 3
	if you == 'X':
		score += 0
		if elf == 'A':
			score += 3
		elif elf == 'B':
			score += 1
		else:
			score += 2
	if you == 'Z':
		score += 6
		if elf == 'C':
			score += 1
		elif elf == 'B':
			score += 3
		else:
			score += 2

print(score)

