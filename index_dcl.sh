#!/bin/bash

# --- Configuration ---
REGIONS=(
    "USA" "CTR" "W" "E" "LKS" "CAL" 
    "NE" "NW" "FLA" "COL" "BAY" "NY"
)
# ---------------------

echo "Starting Index Creation for ${#REGIONS[@]} datasets..."
echo "--------------------------------------------------------"

# Check if index executable exists
if ! [ -x "./index" ]; then
    echo "Error: './index' executable not found or not executable."
    echo "Please ensure you have compiled your project successfully."
    exit 1
fi

for region in "${REGIONS[@]}"; do
    GRAPH_FILE="USA-road-d.${region}.gr"
    INDEX_FILE="USA-road-d.${region}.idx" 
    
    echo "📂 Processing region: ${region}"
    
    if [ -f "$GRAPH_FILE" ]; then
        # Run the Indexing command
        echo "   -> Running indexer: ./index ${GRAPH_FILE} ${INDEX_FILE}"
        ./index "$GRAPH_FILE" "$INDEX_FILE"
    else
        echo "   Skipping: Graph file ${GRAPH_FILE} not found. Ensure the gunzip step ran successfully."
    fi
    
    echo "--------------------------------------------------------"
done

echo "Indexing complete."
