import requests
import os
from datetime import date
import browser_cookie3
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))

#Get cookies from the browser
cj = browser_cookie3.firefox()
if not (".adventofcode.com" in str(cj)):
    cj = browser_cookie3.chrome()
    
#Get today number of day
day_today = date.today().strftime("%d").lstrip("0")
year_today = date.today().strftime("%Y")

#If we provide an argument, use it as the desired day. Ex: ./startDay.py 5. Otherwise use day_today
if len(sys.argv) > 1:
    day = int(sys.argv[1])
    if len(sys.argv) > 2:
        year = int(sys.argv[2])
        if day >= 2000:
            day, year = year, day
    else:
        year = year_today
    if 0 < day < 31 or day > day_today and year == year_today:
        exit("No input exists for 12/{}/{}".format(day, year))
else:
    day = day_today
    year = year_today

print(f"Initializing {year} day:{day}")
if not os.path.exists(f"{script_dir}\\input"):
    print('hi')
    os.mkdir(f"{script_dir}\\input")
if not os.path.exists(f"{script_dir}\\input\\{year}"):
    os.mkdir(f"{script_dir}\\input\\{year}")
os.chdir(f"{script_dir}\\input\\{year}")
r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies = cj)
with open("day{:02d}_data.txt".format(int(day)),"w") as f:
    f.write(r.text)
