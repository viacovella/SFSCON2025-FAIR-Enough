#!/bin/bash

# Create directory structure for the project
#nparticipants=$1
nparticipants=12

mkdir -p dataset

for p in $(seq -w 1 $nparticipants); do
    mkdir -p dataset/sub-$p/beh
done

