from typing import Iterable

def transpose(lines):
    if isinstance(lines[0], str):
        t_lines = list(map(list, zip(*lines)))
        return [''.join(x) for x in t_lines]
    else:
        return list(map(list, zip(*lines)))

def flatten(ls):
    def flatten_help(ls):
        for x in ls:
            if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
                yield from flatten_help(x)
            else:
                yield x
    return [x for x in flatten_help(ls)]

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(transpose(['123','456','789']))
print(flatten([[[1],[1,2],],[[1],[1,2]]]))
