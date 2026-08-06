#!/usr/bin/env bash

if [[ $# -eq 0 ]]; then
    echo "Usage: error_handling.sh <person>"
    exit 1
elif [[ $# -ge 2 ]]; then
    echo "Usage: error_handling.sh <person>"
    exit 1
else
    temp_str="Hello, $1"
    echo "$temp_str"
    exit 0
fi
