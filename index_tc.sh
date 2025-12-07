#!/bin/bash

# --- Configuration ---
REGIONS=(
    "BAY" "NY"
)

# Path to the TreeCount indexer binary
TC_INDEXER="./TreeCount/TC_index"
# Directory to store the baseline TreeCount indexes
OUTPUT_DIR="tc_indexes"
# ---------------------

echo "Starting TreeCount Index Creation for ${#REGIONS[@]} datasets..."
echo "--------------------------------------------------------"

# Check if index executable exists
if ! [ -x "$TC_INDEXER" ]; then
    echo "Error: '$TC_INDEXER' executable not found or not executable."
    echo "Please ensure the TreeCount binary is compiled at that path."
    exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"
echo "TreeCount index files will be saved in the '$OUTPUT_DIR' directory."
echo "--------------------------------------------------------"

for region in "${REGIONS[@]}"; do
    GRAPH_FILE="USA-road-d.${region}.gr"
    # Use a distinct suffix for TC indexes
    INDEX_FILE="${OUTPUT_DIR}/USA-road-d.${region}.tc_idx" 
    
    echo "📂 Processing region: ${region}"
    
    if [ -f "$GRAPH_FILE" ]; then
        # Run the TreeCount Indexing command: ./TreeCount/src/TC_index -g graph_file -o output_file
        echo "   -> Running TC Indexer: $TC_INDEXER -g $GRAPH_FILE -o $INDEX_FILE"
        "$TC_INDEXER" -g "$GRAPH_FILE" -o "$INDEX_FILE"
    else
        echo "   Skipping: Graph file ${GRAPH_FILE} not found. Ensure the download/unzip step ran successfully."
    fi
    
    echo "--------------------------------------------------------"
done

echo "TreeCount Indexing complete."
