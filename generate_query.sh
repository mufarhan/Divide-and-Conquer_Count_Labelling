#!/bin/bash

# Define the list of region codes for the road networks
# Assumes the graph files have been unzipped and are available (e.g., USA-road-d.USA.gr)
REGIONS=(
    "USA" "CTR" "W" "E" "LKS" "CAL" 
    "NE" "NW" "FLA" "COL" "BAY" "NY"
)

# The path to your compiled query generation binary
GENERATOR_BIN="./query_generator"

# Directory where the graph files are located
INPUT_DIR="."

# Directory to store the generated query files (will be created if it doesn't exist)
OUTPUT_DIR="queries"

echo "Starting query generation for ${#REGIONS[@]} regions..."
echo "-------------------------------------------------------"

# 1. Check if the binary exists (ensures 'make query_generator' was run)
if [ ! -f "$GENERATOR_BIN" ]; then
    echo "Error: Query generator binary not found at $GENERATOR_BIN."
    echo "Please ensure you have run 'make query_generator' successfully."
    exit 1
fi

# 2. Create output directory
mkdir -p "$OUTPUT_DIR"
echo "Query files will be saved in the '$OUTPUT_DIR' directory."
echo "-------------------------------------------------------"

for region in "${REGIONS[@]}"; do
    INPUT_FILE="${INPUT_DIR}/USA-road-d.${region}.gr"
    # Output prefix will result in files like queries/USA_random_pairs.txt
    OUTPUT_PREFIX="${OUTPUT_DIR}/${region}"

    echo "--- Processing ${region} ---"

    if [ -f "$INPUT_FILE" ]; then
        echo "Running: $GENERATOR_BIN $INPUT_FILE $OUTPUT_PREFIX"
        
        # Execute the C++ query generator binary
        $GENERATOR_BIN "$INPUT_FILE" "$OUTPUT_PREFIX"

        if [ $? -eq 0 ]; then
            echo "${region} queries successfully generated."
            echo "   Generated: ${OUTPUT_PREFIX}_random_pairs.txt (1M pairs)"
            echo "   Generated: ${OUTPUT_PREFIX}_dist_bucket_0.txt to 9.txt (100K total pairs)"
        else
            echo "Error: Query generation failed for ${region}. Check C++ output above."
        fi
    else
        echo "Warning: Input graph file not found: $INPUT_FILE. Skipping region."
    fi
    echo "-------------------------------------------------------"
done

echo "All query generation tasks completed."
