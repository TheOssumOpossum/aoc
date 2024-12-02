from typing import Iterable

def _transform(ls, f):
    if isinstance(ls, str):
        return '\n'.join([''.join(x) for x in f(ls.splitlines())])
    elif isinstance(ls, dict):
        height = max([x[0] for x in ls.keys()])
        width = max([x[1] for x in ls.keys()])
        new_ls = [[ls[(x,y)] for y in range(width+1)] for x in range(height+1)]
        transform = f(new_ls)
        m = {}
        for x, line in enumerate(transform):
            for y, char in enumerate(line):
                m[(x,y)] = char
        return m
    else:
        return f(ls)

# [[0, 1]
#  [2, 3]]
# ==>
# [[0, 2]
#  [1, 3]]
def transpose(ls):
    return _transform(ls, lambda x: list(map(list, zip(*x))))

# [[0, 1]
#  [2, 3]]
# ==>
# [[1, 3]
#  [0, 2]]
def rot270(ls):
    return list(_transform(ls, lambda x: reversed(list(map(list, zip(*x))))))

# [[0, 1]
#  [2, 3]]
# ==>
# [[2, 0]
#  [3, 1]]
def rot90(ls):
    return list(_transform(ls, lambda x: list(map(list,zip(*reversed(x))))))

# [[0, 1]
#  [2, 3]]
# ==>
# [0, 1, 2, 3]
def flatten(ls):
    def flatten_help(ls):
        for x in ls:
            if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
                yield from flatten_help(x)
            else:
                yield x
    return [x for x in flatten_help(ls)]
