function getIP{
	(get-netipaddress).ipv4address | Select-String "192*"
}

#Grabs the hostname.
function getHostname{
	(Get-ComputerInfo).CsName
}

#Gets just the Major Powershell Version
function getPsversion{
	($HOST.Version.Major)
}
$IP = getIP

#Converts hostname to a String then makes the string lower case.
$hostname = (gethostname).ToString().ToLower()
$psversion = getPsversion

$date = (get-Date -format "dddd MM/dd/yyyy HH:mm") 

$Body = "This machine's IP is $IP. User is $env:username. Hostname is $hostname. PowerShell Version $psversion. Today's date is $date"
#Test that the $Body shows up in the way wanted
Write-Host("$Body")

#Send-MailMessage -To "maysrt@mail.uc.edu" -From "maysrd@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $Body -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)
