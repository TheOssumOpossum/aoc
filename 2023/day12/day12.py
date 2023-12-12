import sys
import re
import functools

day = '12'
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and int(sys.argv[1]) >= 2 else 'sample'))
lines = f.read().strip().splitlines()

#part 1 and 2
@functools.lru_cache
def f(nums, string):
     if len(nums) == 0:
        return 1 * '#' not in string
     elif len(string) == 0 or ('?' not in string and '#' not in string):
        return 0
     else:
        first_candidate = re.match(f"^\.*[?#]{{{nums[0]}}}(?!#)", string)
        prefix = re.match("^\.*#+|^\.*\?", string)
        if first_candidate is None:
            if re.match("^\.*#", string):
                return 0
            return f(nums, string[len(prefix[0]):])
        
        first_candidate = first_candidate[0]
        
        # use first candidate
        res = f(nums[1:], string[len(first_candidate)+1:])
        
        # dont use first candidate
        res2 = 0
        if not re.match("^\.*#", string):
            res2 = f(nums, string[len(prefix[0]):])
        return res + res2

def solve(m=None):
    s = 0
    for i, line in enumerate(lines):
        l = line.strip()
        string, nums = l.split()
        nums = [int(x) for x in re.findall("\d+", nums)]
        
        if m is not None:
            nums *= 5
            string = ((string + '?')*5)[:-1]
        
        s += f(tuple(nums), string)
    return s

print(solve())
print(solve(5))


# part 1 - brute force
# def countGroups(l):
#     if '?' in l:
#         return []
#     groups = re.findall("#+", l)
#     return [len(g) for g in groups]
    
# def createStrings(l, maxi):
#     if '#'*(maxi+1) in l:
#         return l
#     if '?' not in l:
#         return l
#     else:
#         res1 = createStrings(l.replace('?', '.', 1), maxi)
#         res2 = createStrings(l.replace('?', '#', 1), maxi)
#         return [res1] + [res2]

# def flatten(xs):
#     for x in xs:
#         if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
#             yield from flatten(x)
#         else:
#             yield x

# for i, line in enumerate(lines):
#     l = line.strip()
#     m, nums = l.split()
#     nums = [int(x) for x in re.findall("\d+", nums)]
#     maxi = max(nums)
#     # nums *= 5
#     # m = ((m + '?')*5)[:-1]
#     # print(m, nums)
#     x = createStrings(m, maxi)
#     x = flatten(x)
#     s = 0
#     for ss in x:
#         if countGroups(ss) == nums:
#             s += 1
