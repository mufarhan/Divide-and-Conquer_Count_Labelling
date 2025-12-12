#include "road_network.h"
#include "util.h"

#include <iostream>
#include <fstream>

using namespace std;
using namespace road_network;

const size_t nr_queries = 1000000;

int main([[maybe_unused]]int argc, char** argv)
{

    ifstream ifs(argv[1]);
    ContractionIndex con_index(ifs);
    ifs.close();

    vector<pair<NodeID, NodeID> > queries; 
    NodeID a, b;

    ifs.open(argv[2]);
    while(ifs >> a >> b)
        queries.push_back(make_pair(a, b));
    ifs.close();

    util::start_timer();
    for (pair<NodeID, NodeID> q : queries)
        con_index.get_spc(q.first, q.second);
    cout << "ran " << queries.size() << " random queries in " << util::stop_timer() << "s" << endl;

    return 0;
}
