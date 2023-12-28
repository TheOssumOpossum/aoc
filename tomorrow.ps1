# creates folders and files for the next day (run before midnight)
# creates a temporary download script to download input for the current day (run that after midnight)
$day = [int]$(Get-Date -Format "dd") + 1
$year = $(Get-Date -Format "yyyy")
$month = $(Get-Date -Format "MM")
if (($day -gt 25) -or !($month -eq 12)){
    Write-Host "Cannot init $year day $day"
    exit
}
python3 new_day.py
cd $year
echo "python3 ..\download_input.py $day $year" >> download.ps1
echo "rm ./download.ps1" >> download.ps1
