#!/usr/bin/env bash

num=$1
if [[ $# -eq 0 ]]; then
    echo "Error: invalid input"
    exit 1
elif [[ $num == "total" ]]; then
    echo "18446744073709551615"
    exit 0
elif [[ $num -le 0 || $num -ge 65 ]]; then
    echo "Error: invalid input"
    exit 1
else
    echo "2 ^ ($num - 1)" | bc
    exit 0
fi