#!/usr/bin/env bash

if [[ $# -ne 2 ]]; then
    echo "error"
    exit 1
fi
series=$1
span=$2
length=${#series}
if (( span > length )); then
    echo "span must not exceed string length"
    exit 1
fi
if (( span < 0 )); then
    echo "span must not be negative"
    exit 1
fi
if (( span == 0 )); then
    echo "1"
    exit 0
fi
current_max=0
for ((i = 0; i <= length - span; i++)); do
    product=1
    for ((j = 0; j < span; j++)); do
        digit=${series:i+j:1}
        if [[ ! $digit =~ ^[0-9]+$ ]]; then
            echo "digits input must only contain digits"
            exit 1
        fi
        ((product *= digit))
    done
    if (( product > current_max )); then
        current_max=$product
    fi
done
echo "$current_max"