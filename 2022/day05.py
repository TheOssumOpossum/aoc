import re
day = '05'
sample = False

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

# #part 1
# lines = f.read().splitlines()

# width = 0
# crates = {}
# for line in lines:
# 	if '[' in line:
# 		line = re.sub('    ','[x] ', line)
# 		# print(line)
# 		x = re.findall("\w", line)
# 		width = len(x)
# 		col = -1
# 		for c in x:
# 			col += 1
# 			if c == 'x':
# 				continue
# 			if col not in crates:
# 				crates[col] = []
# 			crates[col].append(c)
# 	if 'move' in line:
# 		qty, src, dest = re.findall('\d+', line)
# 		qty = int(qty)
# 		src = int(src) - 1
# 		dest = int(dest) - 1
# 		for i in range(qty):
# 			c = crates[src].pop(0)
# 			crates[dest].insert(0, c)
# res=''
# for i in range(width):
# 	res += crates[i][0]
# print(res)

#part 2
lines = f.read().splitlines()

width = 0
crates = {}
for line in lines:
	if '[' in line:
		line = re.sub('    ','[x] ', line)
		# print(line)
		x = re.findall("\w", line)
		width = len(x)
		col = -1
		for c in x:
			col += 1
			if c == 'x':
				continue
			if col not in crates:
				crates[col] = []
			crates[col].append(c)
	if 'move' in line:
		qty, src, dest = re.findall('\d+', line)
		qty = int(qty)
		src = int(src) - 1
		dest = int(dest) - 1
		x = qty
		for i in range(qty):
			x -= 1
			c = crates[src].pop(x)
			crates[dest].insert(0, c)
res=''
for i in range(width):
	res += crates[i][0]
print(res)
