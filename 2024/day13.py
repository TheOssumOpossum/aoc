import sys
import re
sys.path.append('../')
from lib.read import read

lines, groups = read(__file__)

s = 0
ss = 0

# Group Parser
for add in 0, 10000000000000:
    s = 0
    for i, group in enumerate(groups):
        x1, y1 = [int(x) for x in re.findall('\d+', group.splitlines()[0])]
        x2, y2 = [int(x) for x in re.findall('\d+', group.splitlines()[1])]
        px, py = [int(x) for x in re.findall('\d+', group.splitlines()[2])]
        
        px += add
        py += add
        
        # [A] [x] = [b]
        # A = [[x1, y1]
        #      [x2, y2]]
        #
        # [x] = [A]^-1 [b]
        # [A]^-1 = [[+y2, -y1],
        #           [-x2, +x1]] * det
        # det = 1/(x1*y2 - y1*x2)
        #
        # [b] = [[px],
        #        [py]]
        #
        # [x] = [[+px*y2 - py*x2],
        #        [-px*y1 + py*x1]] * det
        
        a = (px*y2 + py*-x2)/(x1*y2 - y1*x2)
        b = (px*-y1 + py*x1)/(x1*y2 - y1*x2)
        if int(a) == a and int(b) == b:
            s += int(3*a + b)
    print(s)

# The linear program that couldn't:
# import pulp as pl

# for i, group in enumerate(groups):
#     x1, y1 = [int(x) for x in re.findall('\d+', group.splitlines()[0])]
#     x2, y2 = [int(x) for x in re.findall('\d+', group.splitlines()[1])]
#     px, py = [int(x) for x in re.findall('\d+', group.splitlines()[2])]
    
#     px += 10000000000000
#     py += 10000000000000
    
#     problem = pl.LpProblem("problem", pl.LpMinimize)
#     a = pl.LpVariable('a', lowBound= 0, cat = pl.LpInteger)
#     b = pl.LpVariable('b', lowBound= 0, cat = pl.LpInteger)
#     problem += 3 * a + b
#     problem += x1 * a + x2 * b == px
#     problem += y1* a + y2 * b == py
#     result = pl.PULP_CBC_CMD(msg=0).solve(problem)
#     print(pl.value(a), pl.value(b))
    
#     print(pl.LpStatus[result])
#     if pl.LpStatus[result] != 'Infeasible':
#         s += pl.value(a)*3 + pl.value(b)
