#!/bin/bash

# --- Configuration ---
REGIONS=(
    "USA" "CTR" "W" "E" "LKS" "CAL" 
    "NE" "NW" "FLA" "COL" "BAY" "NY"
)

# Define the query file types/suffixes (1 random + 10 distance-bucketed)
QUERY_TYPES=("random_pairs")
for i in {0..9}; do
    QUERY_TYPES+=("dist_bucket_${i}")
done

# Binary names and directories
TC_QUERY_BIN="./TreeCount/src/TC_query"
INDEX_DIR="tc_indexes"
INDEX_SUFFIX=".tc_idx"
QUERY_DIR="queries"
# Directory to store the benchmark output (e.g., timing/result logs)
OUTPUT_DIR="tc_results"
# ---------------------

echo "Starting TreeCount Query Execution for ${#REGIONS[@]} datasets across ${#QUERY_TYPES[@]} query sets."
echo "------------------------------------------------------------------------------------------------"

# 1. Check if query executable exists
if ! [ -x "$TC_QUERY_BIN" ]; then
    echo "Error: '$TC_QUERY_BIN' executable not found or not executable."
    echo "Please ensure the TreeCount binary is compiled at that path."
    exit 1
fi

# 2. Create output directory
mkdir -p "$OUTPUT_DIR"
echo "Benchmark output files will be saved in the '$OUTPUT_DIR' directory."
echo "------------------------------------------------------------------------------------------------"

TOTAL_RUNS=0
SUCCESS_RUNS=0

# Loop 1: Iterate over regions (datasets)
for region in "${REGIONS[@]}"; do
    # Input Index File (from build_tc_indexes.sh)
    INDEX_FILE="${INDEX_DIR}/USA-road-d.${region}${INDEX_SUFFIX}"
    
    if [ ! -f "$INDEX_FILE" ]; then
        echo "Skipping region ${region}: Index file ${INDEX_FILE} not found. Ensure TC indexing completed."
        continue
    fi

    # Loop 2: Iterate over query set types (random or bucketed)
    for type_suffix in "${QUERY_TYPES[@]}"; do
        # Input Query File (from query_generator)
        QUERY_FILENAME="${region}_${type_suffix}.txt"
        QUERY_FILE="${QUERY_DIR}/${QUERY_FILENAME}"
        
        # Output File for results/timing (distinct from others)
        OUTPUT_FILE="${OUTPUT_DIR}/${region}_${type_suffix}.out"
        
        TOTAL_RUNS=$((TOTAL_RUNS + 1))

        if [ -f "$QUERY_FILE" ]; then
            
            # Print combination for easy grepping
            # Format: RUN: REGION | QUERY_TYPE
            echo "--- RUN: ${region} | ${type_suffix} ---"
            
            # Execute the TreeCount Query command: ./TC_query -i index_file -q query_file -o output_file
            echo "   -> Running TC Query: $TC_QUERY_BIN -i $INDEX_FILE -q $QUERY_FILE -o $OUTPUT_FILE"
            "$TC_QUERY_BIN" -i "$INDEX_FILE" -q "$QUERY_FILE" -o "$OUTPUT_FILE"
            
            if [ $? -eq 0 ]; then
                SUCCESS_RUNS=$((SUCCESS_RUNS + 1))
            else
                echo "Error: Execution failed for ${region} with ${type_suffix}. Check TC query output."
            fi

        else
            echo "Skipping query set ${type_suffix} for ${region}: Query file ${QUERY_FILE} not found. Ensure query generation completed."
        fi
    done
    echo "------------------------------------------------------------------------------------------------"
done

echo "TreeCount Benchmark completed."
echo "Summary: ${SUCCESS_RUNS} successful runs out of ${TOTAL_RUNS} total runs."
