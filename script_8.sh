#!/bin/bash

array=(apple pear plum banana orange)
	echo "Array items:"
for item in ${array[*]}
do
	printf " %s\n" $item
done
