$IP = getIP
function getIP{
(Get-NetIPAddress).IPv4Address | Select-String "192*"
}


Write-Host("This machine's IP is {0}" -f $IP)
