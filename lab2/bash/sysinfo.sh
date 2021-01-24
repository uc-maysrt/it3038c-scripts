#!/bin/bash
#This script will email us our user, IP, hostname, and today's date
emailaddress=maysrt@mail.uc.edu
ip=$(ip a | grep 'dynamic ens192'| awk '{print $2}')
today=$(date +"%m-%d-%Y %H:%M:%S")
mail -s "IT3038C Linux IP" $emailaddress <<<$(printf "
IP Address: $ip \c
Hostname: $HOSTNAME \c
Machine Type: $MACHTYPE \c
Bash Version: $BASH_VERSION \c
Date: $today")
