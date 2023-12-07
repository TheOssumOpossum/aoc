import sys
import os

YEAR = 2023

if (len(sys.argv) == 2):
    day = int(sys.argv[1])
    day = '{:02d}'.format(day)
    if not os.path.exists(os.getcwd() + '/' + str(YEAR)):
        os.makedirs(os.getcwd() + '/' + str(YEAR))
    if not os.path.exists(os.getcwd() + '/' + str(YEAR) + '/' + 'day{}'.format(day)):
        os.makedirs(os.getcwd() + '/' + str(YEAR) + '/' + 'day{}'.format(day))
    f = open("{}/day{}/day{}.py".format(YEAR,day,day),"w")
    f.write(
'''import sys
import re
import collections
import functools

day = ''' + '\'{}\''.format(day) + '''
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample2' if sys.argv[1] == '2' else 'sample'))
lines = f.read().strip().splitlines()

s = 0
m = {}
for i, line in enumerate(lines):
    l = line.strip()
''')
    f.close()
    f = open("{}/day{}/day{}_sample.txt".format(YEAR,day,day),"w")
    f.close()
    f = open("{}/day{}/day{}_sample2.txt".format(YEAR,day,day),"w")
    f.close()
    f = open("input/{}/day{}_data.txt".format(YEAR,day,day),"w")
    f.close()
