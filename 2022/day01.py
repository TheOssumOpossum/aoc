import heapq


day = '01'
sample = False

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

lines = f.readlines()

# part 1
# maxi = -1
# running = 0

# for line in lines:
# 	l = line.strip()
# 	if l == '':
# 		if running > maxi:
# 			maxi = running
# 		running = 0
# 	else:
# 		running += int(l)
# if running > maxi:
# 	maxi = running

# print(maxi)

# part 2
elves = []
running = 0
for line in lines:
	l = line.strip()
	if l == '':
		elves.append(running)
		running = 0
	else:
		running += -int(l)
elves.append(running)

heapq.heapify(elves)
s = 0
s += heapq.heappop(elves)
s += heapq.heappop(elves)
s += heapq.heappop(elves)
print(-s)
