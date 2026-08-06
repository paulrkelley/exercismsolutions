#!/usr/bin/env bash

if [[ $# -ne 2 ]]; then
    echo "Usage: hamming.sh <string1> <string2>"
    exit 1
fi
string1=$1
string2=$2
differences=0
if [[ ${#string1} -ne ${#string2} ]]; then
    echo "strands must be of equal length"
    exit 1
fi
for ((i = 0; i < ${#string1}; i++)); do
    if [[ "${string1:i:1}" != "${string2:i:1}" ]]; then
        ((differences++))
    fi
done
echo "$differences"
