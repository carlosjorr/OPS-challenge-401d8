# Get the current time
$currentHour = (Get-Date).Hour

# Greet based on the time of day
if ($currentHour -ge 0 -and $currentHour -lt 12) {
    Write-Host "Good morning!"
} elseif ($currentHour -ge 12 -and $currentHour -lt 18) {
    Write-Host "Good afternoon!"
} else {
    Write-Host "Good evening!"
}
