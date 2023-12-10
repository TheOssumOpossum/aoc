# creates folders and files for the next day (run before midnight)
# creates a temporary download script to download input for the current day (run that after midnight)
$day = [int]$(Get-Date -Format "dd") + 1
$year = $(Get-Date -Format "yyyy")
python new_day.py
cd $year\day$day\
echo "python ..\..\download_input.py $day $year" >> download.ps1
echo "rm ./download.ps1" >> download.ps1
