# Creates files and downloads inputs for prior advent of code problems.
param($day, $year)
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
Set-Location $dir
if (($null -eq $year)) {
    $month = $(Get-Date -Format "MM")
    if (($null -eq $day)){
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
if (([int]$day -lt 1) -or ([int]$day -gt 25) -or ([int]$year -lt 2015) -or ([int]$year -gt $(Get-Date -Format "yyyy"))){
    Write-Host "Cannot init $year day $day"
    exit
}
python3 new_day.py $day $year
python3 download_input.py $day $year
Set-Location $year
[Microsoft.PowerShell.PSConsoleReadLine]::AddToHistory("python ./day$day.py 1")
[Microsoft.PowerShell.PSConsoleReadLine]::AddToHistory("python ./day$day.py 0")
