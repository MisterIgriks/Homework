#!/bin/bash

read -p "Enter sentence: " sentence
for word in $sentence; do
    reversed="$word $reversed"
done
echo $reversed