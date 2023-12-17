#!/bin/bash

echo "$1"
count=0

while read
do
	((count=$count+1))
done <$1

echo $count
