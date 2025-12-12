#!/bin/bash

# Base URL for the challenge data
BASE="http://www.diag.uniroma1.it/~challenge9/data/USA-road-d"

# List of region codes derived from your links
REGIONS=(
    "NY"
)

echo "Starting download and extraction of ${#REGIONS[@]} files..."
echo "-------------------------------------------------------"

for region in "${REGIONS[@]}"; do
    FILENAME="USA-road-d.${region}.gr.gz"
    URL="${BASE}/${FILENAME}"

    echo "1. Downloading ${region}..."
    # -q: quiet mode (less spam), --show-progress: shows a nice bar
    wget -q --show-progress "$URL"

    if [ -f "$FILENAME" ]; then
        echo "2. Unzipping ${FILENAME}..."
        gunzip "$FILENAME"
    else
        echo "Error: Failed to download $FILENAME"
    fi
    echo "-------------------------------------------------------"
done

echo "All tasks completed."
