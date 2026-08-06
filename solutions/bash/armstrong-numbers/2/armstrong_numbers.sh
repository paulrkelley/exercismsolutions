#!/usr/bin/env bash

total=0
number=$1
length=${#number}
for (( i=0; i<length; i++ )); do
    digit=${number:i:1}
    (( total += digit ** length ))
done
if (( total == number )); then
    echo "true"
else
    echo "false"
fi
