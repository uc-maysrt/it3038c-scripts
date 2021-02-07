#!/bin/bash
# This script outputs the IP address and Hostname of a machine
greeting="This is a script. Hello!"
a=$(ip a | grep 'dynamic ens192' | awk '{print $2}')

echo $greeting, thanks for joining us!
echo '$greeting, thanks for joining us! You owe me $20'
echo "$greeting, thanks for joining us!"
echo "$greeting, you owe me \$20"


echo Machine type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Session length: $SECONDS
echo Home Dir: $HOME
echo My IP is $a
