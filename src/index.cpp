#include "road_network.h"
#include "util.h"

#include <iostream>
#include <cstring>

using namespace std;
using namespace road_network;

const size_t MB = 1024 * 1024;

int main([[maybe_unused]]int argc, char** argv)
{

     // read graph
    ifstream ifs(argv[1]);
    Graph g;
    read_graph(g, ifs);
    ifs.close();

    util::start_timer();
    // degree 1 node contraction
    vector<Neighbor> closest;
    g.contract(closest);

    // construct index
    vector<CutIndex> ci;
    g.create_cut_index(ci, 0.2);
    g.reset();

    ContractionHierarchy ch;
    g.create_sc_graph(ch, ci, closest);
    ContractionIndex con_index(ci, closest);

    cout << "created index of size " << con_index.size() / MB << " MB in " << util::stop_timer() << "s" << endl;

    // write index
    ofstream ofs(string(argv[2]) + string("_dcl"));
    con_index.write(ofs);
    ofs.close();

    return 0;
}
