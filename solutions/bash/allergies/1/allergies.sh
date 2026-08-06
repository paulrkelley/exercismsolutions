#!/usr/bin/env bash

allergic_to() {
    local score=$1
    local item=$2
    local value
    if [[ "$item" == "eggs" ]]; then
        value=1
    elif [[ "$item" == "peanuts" ]]; then
        value=2
    elif [[ "$item" == "shellfish" ]]; then
        value=4
    elif [[ "$item" == "strawberries" ]]; then
        value=8
    elif [[ "$item" == "tomatoes" ]]; then
        value=16
    elif [[ "$item" == "chocolate" ]]; then
        value=32
    elif [[ "$item" == "pollen" ]]; then
        value=64
    elif [[ "$item" == "cats" ]]; then
        value=128
    else
        echo "false"
        return
    fi
    if (( score & value )); then
        echo "true"
    else
        echo "false"
    fi
}

list_allergies() {
    local score=$1
    local allergies=()
    if (( score & 1 )); then
        allergies+=("eggs")
    fi
    if (( score & 2 )); then
        allergies+=("peanuts")
    fi
    if (( score & 4 )); then
        allergies+=("shellfish")
    fi
    if (( score & 8 )); then
        allergies+=("strawberries")
    fi
    if (( score & 16 )); then
        allergies+=("tomatoes")
    fi
    if (( score & 32 )); then
        allergies+=("chocolate")
    fi
    if (( score & 64 )); then
        allergies+=("pollen")
    fi
    if (( score & 128 )); then
        allergies+=("cats")
    fi
    echo "${allergies[*]}"
}

score=$1
command=$2
item=$3
if [[ "$command" == "allergic_to" ]]; then
    allergic_to "$score" "$item"
elif [[ "$command" == "list" ]]; then
    list_allergies "$score"
fi
