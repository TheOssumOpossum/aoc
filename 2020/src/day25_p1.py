inp = '''

'''

inp2 = '''
'''


pb1 = 14082811
pb2 = 5249543

# pb1 = 5764801
# pb2 = 17807724

sn2 = 1
sn1 = 1

l1 = 0
l2 = 0

i = 0

do_break1 = False
do_break2 = False
i = 1
while True:
	i += 1
	sn1 = 1
	sn2 = 1
	sn = 7 #didnt realize 7 was fixed
	print("sn",sn)
	for x in range(1,100000000):
		sn1 *= sn
		sn1 = sn1 % 20201227
		if sn1 == pb1:
			l1 = x
			do_break1 = True
			print("1",sn,l1)
			break
	# if do_break1:
	for x in range(1,1000000000):
		sn2 *= sn
		sn2 = sn2 % 20201227
		if sn2 == pb2:
			l2 = x
			do_break2 = True
			print("2",sn,l2)
			break
	if do_break1 and do_break2:
		break
	else:
		do_break1 = False
		do_break2 = False

print(l1,l2,sn)
new_pb1 =1 
new_pb2=1
for i in range(l2):
	new_pb1 *= pb1
	new_pb1 = new_pb1 % 20201227

for i in range(l1):
	new_pb2 *= pb2
	new_pb2 = new_pb2 % 20201227
print(new_pb1, new_pb2)