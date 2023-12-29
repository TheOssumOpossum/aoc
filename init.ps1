# Creates files and downloads inputs for prior advent of code problems.
param($day, $year)
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
cd $dir
if (($year -eq $null)) {
    $month = $(Get-Date -Format "MM")
    if (($day -eq $null)){
        $day = $(Get-Date -Format "dd")
    }
    if (!($month -eq 12) -or ($day -gt 25)) {
        Write-Host "Please specify a day and year."
        exit
    }
    $year = $(Get-Date -Format "yyyy")
}
if ($day -gt 2000) {
    $tmp = $day
    $day = $year
    $year = $tmp
}
if (($day -lt 1) -or ($day -gt 25) -or ($year -lt 2015) -or ($year -gt $(Get-Date -Format "yyyy"))){
    Write-Host "Cannot init $year day $day"
    exit
}
python3 new_day.py $day $year
python3 download_input.py $day $year
cd $year
