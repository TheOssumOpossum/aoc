# creates folders and files for the next day (run before midnight)
# creates a temporary download script to download input for the current day (run that after midnight)
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
Set-Location $dir
$day = ((Get-Date).AddDays(1)).ToString("dd")
$dayint = [int]$day
$year = $(Get-Date -Format "yyyy")
$month = $(Get-Date -Format "MM")
if (($dayint -gt 25) -or !($month -eq 12)){
    Write-Host "Cannot init $year day $day"
    exit
}
python3 new_day.py
Set-Location $year
if ([System.IO.File]::Exists(".\download.ps1")) {Clear-Content ".\download.ps1"}
Write-Output "python3 ..\download_input.py $day $year" >> download.ps1
Write-Output "if (`$?) { Remove-Item ./download.ps1" >> download.ps1
Write-Output '  [Microsoft.PowerShell.PSConsoleReadLine]::AddToHistory("python ./day$day.py 1")' >> download.ps1
Write-Output '  [Microsoft.PowerShell.PSConsoleReadLine]::AddToHistory("python ./day$day.py 0")' >> download.ps1
Write-Output '}' >> .\download.ps1
[Microsoft.PowerShell.PSConsoleReadLine]::AddToHistory("./download.ps1")
