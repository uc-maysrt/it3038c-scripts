#!/bin/bash
#This script will email us our user, IP, hostname, and today's date
emailaddress=maysrt@mail.uc.edu
ip=$(ip a | grep 'dynamic ens192'| awk '{print $2}')
today=$(date +"%m-%d-%Y %H:%M:%S")
content="IP Address: $ip | Hostname: $HOSTNAME | Machine Type: $MACHTYPE | Bash Version: $BASH_VERSION | Date: $today"
mail -s "IT3038C Linux IP" $emailaddress <<<$(echo -e $content)
