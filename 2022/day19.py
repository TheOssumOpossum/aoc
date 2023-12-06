import sys
import re
import pulp as lp

day = 19
sample = True
if len(sys.argv) >= 2:
    if sys.argv[1] == '1':
        sample = False
    else:
        sample = True

f = open('{}day{}_{}.txt'.format('../input/2022/' if not sample else '', day,'sample' if sample else 'data'))

lines = f.read().splitlines()
# minutes = 24
minutes = 32

def find_quality_level(l):
    global minutes
    blueprint, ore_robot_ore_cost, cly_robot_ore_cost, obs_robot_ore_cost, obs_robot_cly_cost, geo_robot_ore_cost, geo_robot_obs_cost = [int(x) for x in re.findall('\d+',l)]
    robots_geo = []
    problem = lp.LpProblem("problem{:02d}".format(blueprint), lp.LpMaximize)
    for i in range(minutes):
        robots_geo.append(lp.LpVariable("robots_geo{:02d}".format(i), 0, 0 if i == 0 else None, lp.LpInteger))
    problem += sum(robots_geo)
    build_ore = []
    build_cly = []
    build_obs = []
    build_geo = []
    onhand_ore = []
    onhand_cly = []
    onhand_obs = []
    robots_ore = []
    robots_cly = []
    robots_obs = []
    for i in range(minutes):
        if i == 0:
            robots_ore.append(lp.LpVariable("robots_ore{:02d}".format(i), 1, 1, lp.LpInteger))
            robots_cly.append(lp.LpVariable("robots_cly{:02d}".format(i), 0, 0, lp.LpInteger))
            robots_obs.append(lp.LpVariable("robots_obs{:02d}".format(i), 0, 0, lp.LpInteger))
            onhand_ore.append(lp.LpVariable("onhand_ore{:02d}".format(i), 0, 0, lp.LpInteger))
            onhand_cly.append(lp.LpVariable("onhand_cly{:02d}".format(i), 0, 0, lp.LpInteger))
            onhand_obs.append(lp.LpVariable("onhand_obs{:02d}".format(i), 0, 0, lp.LpInteger))
        else:
            robots_ore.append(lp.LpVariable("robots_ore{:02d}".format(i), 0, None, lp.LpInteger))
            robots_cly.append(lp.LpVariable("robots_cly{:02d}".format(i), 0, None, lp.LpInteger))
            robots_obs.append(lp.LpVariable("robots_obs{:02d}".format(i), 0, None, lp.LpInteger))
            onhand_ore.append(lp.LpVariable("onhand_ore{:02d}".format(i), 0, None, lp.LpInteger))
            onhand_cly.append(lp.LpVariable("onhand_cly{:02d}".format(i), 0, None, lp.LpInteger))
            onhand_obs.append(lp.LpVariable("onhand_obs{:02d}".format(i), 0, None, lp.LpInteger))
        build_ore.append(lp.LpVariable("build_ore{:02d}".format(i), 0, 1, lp.LpInteger))
        build_cly.append(lp.LpVariable("build_cly{:02d}".format(i), 0, 1, lp.LpInteger))
        build_obs.append(lp.LpVariable("build_obs{:02d}".format(i), 0, 1, lp.LpInteger))
        build_geo.append(lp.LpVariable("build_geo{:02d}".format(i), 0, 1, lp.LpInteger))
        # only build one robot per turn constraint
        problem += build_ore[-1] + build_cly[-1] + build_obs[-1] + build_geo[-1] <= 1
        if i != 0:
            # don't spend unavailable resources constraint
            problem += onhand_ore[-2] - build_ore[-1] * ore_robot_ore_cost >= 0
            problem += onhand_ore[-2] - build_cly[-1] * cly_robot_ore_cost >= 0
            problem += onhand_ore[-2] - build_obs[-1] * obs_robot_ore_cost >= 0
            problem += onhand_cly[-2] - build_obs[-1] * obs_robot_cly_cost >= 0
            problem += onhand_ore[-2] - build_geo[-1] * geo_robot_ore_cost >= 0
            problem += onhand_obs[-2] - build_geo[-1] * geo_robot_obs_cost >= 0
            # manage resources onhand constraint
            problem += onhand_ore[-1] == onhand_ore[-2] + robots_ore[-2] \
                - build_ore[-1] * ore_robot_ore_cost \
                    - build_cly[-1] * cly_robot_ore_cost \
                        - build_obs[-1] * obs_robot_ore_cost \
                            - build_geo[-1] * geo_robot_ore_cost
            problem += onhand_cly[-1] == onhand_cly[-2] + robots_cly[-2] \
                - build_obs[-1] * obs_robot_cly_cost
            problem += onhand_obs[-1] == onhand_obs[-2] + robots_obs[-2] \
                - build_geo[-1] * geo_robot_obs_cost
            # manage number of robots constraint
            problem += robots_ore[-1] == robots_ore[-2] + build_ore[-1]
            problem += robots_cly[-1] == robots_cly[-2] + build_cly[-1]
            problem += robots_obs[-1] == robots_obs[-2] + build_obs[-1]
            problem += robots_geo[i] == robots_geo[i-1] + build_geo[-1]
    # print(problem)

    status = problem.solve()
    # for v in problem.variables():
    #     print(v, lp.value(v))
    # print(status)
    print(problem.objective.value())
    return problem.objective.value()

s = 0                               # part 1
ss = 1                              # part 2
i = 0                               # part 2
for line in lines:
    l = line.strip()
    # s += find_quality_level(l)    # part 1
    ss *= find_quality_level(l)     # part 2
    i += 1                          # part 2
    if i == 3:                      # part 2
        break                       # part 2

print('part1', s)
print('part2', ss)
