#!/bin/bash

echo -n "Enter name file:"
read var1
if [ -e "./$var1" ]; then
	echo "File $var1 exists"
else
	echo "File $var1 does not exist"
fi
