import sys
import os
from datetime import date 

if not os.path.exists('new_day.py'):
    print('This script should be run from the root!')
    sys.exit()

YEAR  = date.today().strftime("%Y")
DAY = str(int(date.today().strftime("%d"))+1)
MONTH = date.today().strftime("%m")
if (MONTH != '12' or int(DAY) > 25) and len(sys.argv) < 3:
    print('Please a specify a year and date.')
    sys.exit()

if (len(sys.argv) >= 2):
    DAY = int(sys.argv[1])
if (len(sys.argv) >= 3):
    YEAR = sys.argv[2]
    if int(DAY) >= 2000:
        DAY, YEAR = YEAR, DAY

DAY = '{:02d}'.format(int(DAY))
if int(YEAR) < 2015 or 0 > int(DAY) > 25:
    print(f'Cannot create files for {YEAR} day:{DAY}')
    sys.exit()
print(f'Creating files for {YEAR} day:{DAY}')
    
CWD = os.getcwd()

if not os.path.exists(f'{CWD}/{YEAR}'):
    os.makedirs(f'{CWD}/{YEAR}')
if not os.path.exists(f'{CWD}/input/{YEAR}'):
    os.makedirs(f'{CWD}/input/{YEAR}')
f = open("template.py")
template = f.read()
f.close()
f = open(f'{YEAR}/day{DAY}.py',"w")
f.write(template)
f.close()
f = open(f'{YEAR}/day{DAY}_sample.txt',"w")
f.close()
f = open(f'{YEAR}/day{DAY}_sample2.txt',"w")
f.close()
f = open(f'input/{YEAR}/day{DAY}_data.txt',"w")
f.close()
