#!/bin/bash

# Create directory structure for the project
#nparticipants=$1
nparticipants=12

mdkir dataset

for p in $(seq 1 $nparticipants); do
    mkdir -p dataset/sub-$p/data
    mkdir -p dataset/sub-$p/beh
done

