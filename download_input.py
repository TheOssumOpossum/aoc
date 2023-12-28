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
MONTH = date.today().strftime("%m")

#If we provide an argument, use it as the desired day. Ex: ./startDay.py 5. Otherwise use day_today
if len(sys.argv) > 1:
    day = int(sys.argv[1])
    if len(sys.argv) > 2:
        year = int(sys.argv[2])
        if day >= 2000:
            day, year = year, day
    else:
        year = year_today
    if (day < 0 or day > 25 or day > int(day_today) and year == int(year_today) or year > int(year_today)):
        exit(f"No input exists for 12/{day}/{year}")
else:
    day = day_today
    year = year_today

if (MONTH != '12' or int(day) > 25) and len(sys.argv) < 3:
    print('Please a specify a year and date.')
    sys.exit()

if year < 2015 or 0 > day > 25:
    print(f'Cannot download input for {year} day {day}')
    sys.exit()

print(f"Downloading input for {year} day {day}")
r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies = cj)
if r.text:
    if not os.path.exists(f"{script_dir}/input"):
        os.mkdir(f"{script_dir}/input")
    if not os.path.exists(f"{script_dir}/input/{year}"):
        os.mkdir(f"{script_dir}/input/{year}")
    os.chdir(f"{script_dir}/input/{year}")
    with open("day{:02d}_data.txt".format(int(day)),"w") as f:
        f.write(r.text)
else:
    print(f'Unable to download input for {year} day:{day}, probably an issue with cookies')
