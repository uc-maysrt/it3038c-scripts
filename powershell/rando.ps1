$RANDO = 0
$Logfile = "C:\logs\rando.log"

for ($i = 0; $i -lt 5; $i++){
    $RANDO =Get-Random -Maximum 1000 -Minimum 1
    write-host($RANDO)
    add-content $Logfile "INFO: Random number is ${RANDO}"
}