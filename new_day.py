import sys
import os
from datetime import date 

# YEAR = 2023


YEAR  = date.today().strftime("%Y").lstrip("0")
day = str(int(date.today().strftime("%d"))+1)

if (len(sys.argv) >= 2):
    day = int(sys.argv[1])
    day = '{:02d}'.format(day)
if (len(sys.argv) >= 3):
    YEAR = sys.argv[2]
    
print(f"Creating files for {YEAR} day:{day}")
    
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
f = open('{}day{}_{}.txt'.format('../../input/2023/' if len(sys.argv) >= 2 and sys.argv[1] == '1' else '',day,'data' if len(sys.argv) >= 2 and sys.argv[1] == '1' else 'sample{}'.format(sys.argv[1]) if int(sys.argv[1]) >= 2 else 'sample'))
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
