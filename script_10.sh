#!/bin/bash

find /home/admin1/watch -type f -and -newer /home/admin1/log/script_10.log -exec cat {} \;
find /home/admin1/watch -type f -and -newer /home/admin1/log/script_10.log -exec mv {} {}.back \;

rm /home/admin1/log/script_10.log 

message="$(date +"%y-%m-%d %T")"
echo $message >>/home/admin1/log/script_10.log
