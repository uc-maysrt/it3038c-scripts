function getIP{
	(get-netipaddress).ipv4address | Select-String "192*"
}
function getHostname{
	(Get-ComputerInfo).CsName | Select-String "maysrt-win"
}
function getPsversion{
	($HOST.major)
}

$IP = getIP
$hostname = gethostname
$psversion = getPsversion
$date = get-Date



$Body = "This machine's IP is $IP. User is $env:username. Hostname is $hostname. PowerShell Version $psversion. Today's date is $date"
Write-Host("$Body")

#Send-MailMessage -To "maysrt@mail.uc.edu" -From "maysrt@mail.uc.edu" -Subject "IT3038C Windows SysInfo" -Body $Body -SmtpServer smtp.google.com -port 587 -UseSSL -Credentials (Get-Credential)