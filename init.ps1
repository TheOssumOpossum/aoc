$day = [int]$(Get-Date -Format "dd") + 1
$year = $(Get-Date -Format "yyyy")
python new_day.py
cd $year\day$day\
