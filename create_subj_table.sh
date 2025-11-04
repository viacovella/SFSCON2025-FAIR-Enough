#!/bin/bash

nparticipants=$1

echo "participant_id age sex"

for p in $(seq -w 1 $nparticipants); do
    curr_mod=$(bc <<< "$p%2")
    if [ $curr_mod -eq 0 ]; then
        echo "sub-$p" $(bc <<< "($RANDOM%18)+18") "M"
    else
        echo "sub-$p" $(bc <<< "($RANDOM%18)+18") "F"
    fi
    
done