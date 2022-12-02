day = '00'
sample = True

f = open('day{}_{}.txt'.format(day,'sample' if sample else 'data'))

lines = f.read().splitlines()

for line in lines:
	l = line.strip()

