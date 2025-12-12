#include "road_network.h"
#include "util.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <stdexcept>

using namespace std;
using namespace road_network;

const size_t NUM_RANDOM_PAIRS = 1000000;
const size_t NUM_BUCKETS = 10;
const distance_t MIN_DIST_BUCKET = 1000;
const size_t BUCKET_SIZE = 10000;

/**
 * @brief Main function to load a graph and generate two types of query sets.
 * * Usage: ./query_generator <graph_file_path> <output_prefix>
 */
int main(int argc, char** argv)
{
    if (argc < 3)
    {
        cerr << "Usage: " << argv[0] << " <graph_file_path> <output_prefix>" << endl;
        return 1;
    }

    const string graph_file_path = argv[1];
    const string output_prefix = argv[2];

    cout << "Loading graph from: " << graph_file_path << endl;

    // 1. Read graph
    ifstream ifs(graph_file_path);
    if (!ifs.is_open())
    {
        cerr << "Error: Could not open graph file: " << graph_file_path << endl;
        return 1;
    }
    Graph g;
    util::start_timer();
    read_graph(g, ifs);
    ifs.close();
    // FIX: Changed 'g.num_nodes()' to 'g.get_nodes()' based on compiler suggestion.
    cout << "Graph loaded with " << g.get_nodes() << " nodes in " << util::stop_timer() << "s" << endl;


    // 2. Prepare the ContractionIndex required for distance bucketing (Task B)
    cout << "Preparing Contraction Index components..." << endl;
    util::start_timer();
    
    // Contraction (needed for ContractionIndex dependencies)
    vector<Neighbor> closest;
    g.contract(closest);

    // Create Cut Index
    vector<CutIndex> ci_cut;
    // Assuming a reasonable parameter like 0.2, as in your example
    ContractionHierarchy ch;
    g.create_sc_graph(ch, ci_cut, closest);
    g.create_cut_index(ci_cut, 0.2); 
    g.reset(); // Reset to original graph state

    // The ContractionIndex object for distance lookups
    ContractionIndex con_index(ci_cut, closest);
    
    cout << "Index components prepared in " << util::stop_timer() << "s" << endl;
    

    // ----------------------------------------------------------------------
    // Task A: Generate 1,000,000 randomly sampled pairs
    // ----------------------------------------------------------------------
    const string file_a_path = output_prefix + "_random_pairs.txt";
    cout << "Generating " << NUM_RANDOM_PAIRS << " uniform random queries to: " << file_a_path << endl;

    ofstream ofs_a(file_a_path);
    if (!ofs_a.is_open())
    {
        cerr << "Error: Could not open output file A: " << file_a_path << endl;
        return 1;
    }

    util::start_timer();
    for (size_t i = 0; i < NUM_RANDOM_PAIRS; ++i)
    {
        // Use random_pair with steps = 0 for uniform random selection
        pair<NodeID, NodeID> q = g.random_pair(0); 
        ofs_a << q.first << " " << q.second << endl;
    }
    ofs_a.close();
    cout << "Generated random queries in " << util::stop_timer() << "s" << endl;


    // ----------------------------------------------------------------------
    // Task B: Generate 10 sets of 10,000 distance-bucketed pairs
    // ----------------------------------------------------------------------
    cout << "Generating " << NUM_BUCKETS << " distance-bucketed query sets (10,000 pairs each)..." << endl;
    
    // Initialize the vector of buckets
    vector<vector<pair<NodeID,NodeID>>> buckets(NUM_BUCKETS);
    
    util::start_timer();
    // Call the user's function to fill the buckets
    g.random_pairs(buckets, MIN_DIST_BUCKET, BUCKET_SIZE, con_index);
    cout << "\nFinished generating all bucketed queries in " << util::stop_timer() << "s" << endl;


    // 3. Write each bucket to a separate file
    for (size_t i = 0; i < NUM_BUCKETS; ++i)
    {
        const string file_b_path = output_prefix + "_dist_bucket_" + to_string(i) + ".txt";
        
        // Assert we have the correct size before writing
        if (buckets[i].size() != BUCKET_SIZE) {
            cerr << "Warning: Bucket " << i << " only contains " << buckets[i].size() << " pairs (expected " << BUCKET_SIZE << ")." << endl;
        }

        ofstream ofs_b(file_b_path);
        if (!ofs_b.is_open())
        {
            cerr << "Error: Could not open output file B for bucket " << i << ": " << file_b_path << endl;
            continue;
        }

        for (const auto& q : buckets[i])
        {
            ofs_b << q.first << " " << q.second << endl;
        }
        ofs_b.close();
        cout << "Wrote bucket " << i << " (" << buckets[i].size() << " pairs) to: " << file_b_path << endl;
    }

    cout << "Query generation complete." << endl;
    return 0;
}
