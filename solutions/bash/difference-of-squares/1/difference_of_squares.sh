#!/usr/bin/env bash

square_of_sum() {
    local num=$1
    local sum
    sum=$((num * (num + 1) / 2))
    echo $((sum ** 2))
}

sum_of_squares() {
    local num=$1
    echo $((num * (num + 1) * (2 * num + 1) / 6))
}

difference() {
    local num=$1
    local square_sum
    local sum_squares
    square_sum=$(square_of_sum "$num")
    sum_squares=$(sum_of_squares "$num")
    echo $((square_sum - sum_squares))
}

func=$1
num=$2
if [[ "$func" == "square_of_sum" ]]; then
    square_of_sum "$num"
elif [[ "$func" == "sum_of_squares" ]]; then
    sum_of_squares "$num"
elif [[ "$func" == "difference" ]]; then
    difference "$num"
fi