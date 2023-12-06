import sys

day = 20
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

#part 1
# lines = f.read().strip().splitlines()

# m = []
# nums = []
# numdynums = {}
# class LL:
#     def __init__(self, val, uuid):
#         self.val = val
#         self.uuid = uuid
#         self.prev = None
#         self.next = None

#     def __str__(self):
#         return (self.uuid)

# head = None
# prev = None
# cur = None
# for line in lines:
#     l = line.strip()
#     x = int(l)
#     s = ''
#     if x not in numdynums:
#         numdynums[x] = 1
#         s = str(x) + 'a'
#     else:
#         numdynums[x] += 1
#         s = str(x) + str(chr(96 + numdynums[x]))
#     nums.append(s)
#     if head is None:
#         head = LL(x, s)
#         prev = head
#     else:
#         cur = LL(x, s)
#         prev.next = cur
#         cur.prev = prev
#         prev = cur
# head.prev = cur
# cur.next = head

# print(nums)
# cur = head

# for n in nums:
#     while True:
#         if cur.uuid == n:
#             break
#         else:
#             cur = cur.next

#     save_val = cur.val
#     save_uuid = cur.uuid
#     cur = cur.prev
#     cur.next = cur.next.next
#     cur.next.prev = cur
#     for i in range(abs(save_val)):
#         if save_val > 0:
#             cur = cur.next
#         else:
#             cur = cur.prev
#     save_next = cur.next
#     cur.next = LL(save_val, save_uuid)
#     cur.next.prev = cur
#     cur.next.next = save_next
#     cur.next.next.prev = cur.next

# while True:
#     if cur.val == 0:
#         break
#     cur = cur.next
# s = 0
# for i in range(3000):
#     cur = cur.next
#     if i == 999 or i == 1999 or i == 2999:
#         s += cur.val
# print(s)

#part 2
lines = f.read().strip().splitlines()

m = []
nums = []
numdynums = {}
class LL:
    def __init__(self, val, uuid):
        self.val = val
        self.uuid = uuid
        self.prev = None
        self.next = None

    def __str__(self):
        return (self.uuid)

head = None
prev = None
cur = None
for line in lines:
    l = line.strip()
    x = int(l)
    s = ''
    if x not in numdynums:
        numdynums[x] = 1
        s = str(x) + 'a'
    else:
        numdynums[x] += 1
        s = str(x) + str(chr(96 + numdynums[x]))
    nums.append(s)
    if head is None:
        head = LL(x*811589153, s)
        prev = head
    else:
        cur = LL(x*811589153, s)
        prev.next = cur
        cur.prev = prev
        prev = cur
head.prev = cur
cur.next = head

print(nums)
cur = head

for _ in range(10):
    for n in nums:
        while True:
            if cur.uuid == n:
                break
            else:
                cur = cur.next

        save_val = cur.val
        save_uuid = cur.uuid
        cur = cur.prev
        cur.next = cur.next.next
        cur.next.prev = cur
        for i in range(abs(save_val)%(len(nums)-1)):
            if save_val > 0:
                cur = cur.next
            else:
                cur = cur.prev
        save_next = cur.next
        cur.next = LL(save_val, save_uuid)
        cur.next.prev = cur
        cur.next.next = save_next
        cur.next.next.prev = cur.next

while True:
    if cur.val == 0:
        break
    cur = cur.next
s = 0
for i in range(3000):
    cur = cur.next
    if i == 999 or i == 1999 or i == 2999:
        s += cur.val
print(s)
