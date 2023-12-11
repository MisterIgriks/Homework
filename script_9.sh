#!/bin/bash

echo -n "Enter name file:"
read var1
if [ -f "./$var1" ]; then
	cat $var1 
else
	echo "Error!!! File $var1 does not exist"

fi
