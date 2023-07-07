#!/bin/bash

# Specify the directory path
directory="/path/to/directory"

# Loop through each file in the directory
for file in "$directory"/*
do
    # Print the file name
    echo "$file"
done
