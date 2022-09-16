$BODY = "This machines's IP is $IP. User is $USER. Hostname is $HOSTNAME. PowerShell Version is $PWSHELL_VER. Today's Date is $CUR_DATE." 
$IP = getIP
$USER = [system.environment]::UserName
$HOSTNAME = hostname
$PWSHELL_VER = $HOST.Version.Major
$CUR_DATE = Get-Date -Format "dddd MM dd yyyy"

#grabs ip of device
function getIP{
(Get-NetIPAddress).IPv4Address | Select-String "192*"
}


#Write-Host($BODY)

Send-MailMessage -From "andrew.warn67@gmail.com" -To "warnera7@mail.uc.edu" -Subject "IT3038c Windows SysInfo" -Body $Body -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)