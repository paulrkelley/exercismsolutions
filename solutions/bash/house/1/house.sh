#!/usr/bin/env bash

subjects=("house that Jack built" "malt" "rat" "cat" "dog" "cow with the crumpled horn" "maiden all forlorn" "man all tattered and torn" "priest all shaven and shorn" "rooster that crowed in the morn" "farmer sowing his corn" "horse and the hound and the horn")

actions=("" "lay in" "ate" "killed" "worried" "tossed" "milked" "kissed" "married" "woke" "kept" "belonged to")

recite_clauses() {
    local index=$1
    # Base case: finish with the house and a period.
    if (( index == 0 )); then
        printf '%s.' "${subjects[0]}"
        return
    fi
    printf '%s that %s the ' \
        "${subjects[index]}" \
        "${actions[index]}"
    recite_clauses $((index - 1))
}

recite_verse() {
    local verse=$1
    local index=$((verse - 1))
    printf 'This is the '
    recite_clauses "$index"
    printf '\n'
}

start=$1
end=$2
if [[ $# -ne 2 ]] || (( start < 1 || start > 12 || end < 1 || end > 12 || start > end )); then
    echo "invalid verse range"
    exit 1
fi

for ((verse = start; verse <= end; verse++)); do
    recite_verse "$verse"
done
exit 0
