#!/bin/bash

find ~/watch -type f -and -newer ~/log/script_10.log -exec cat {} \;
find ~/watch -type f -and -newer ~/log/script_10.log -exec mv {} {}.back \;

rm ~/log/script_10.log 

message="$(date +"%y-%m-%d %T")"
echo $message >>~/log/script_10.log
