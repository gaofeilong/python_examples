#!/bin/bash
if [[ $# -ne 1 ]]; then
        echo "invalid argument"
        exit 2
else
        echo "install part1..."
        echo "install part2..."
        echo "install part3..."
        if [[ $1 == "-i" ]]; then
                exit 0
        else
                exit 1
        fi
fi
