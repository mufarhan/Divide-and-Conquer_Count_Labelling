# Divide-and-Conquer Labelling (DCL) 

A tool to speed up shortest path counting queries on large road networks, 
It consists of the following main files:

* road_network.h / road_network.cpp: core library
* util.h / util.cpp: library with additional tools

Additional files are:

* index.cpp: create an index file
* query.cpp: load index from a file and evaluate random queries

# Usage

To compile the source in `src/`

    $ make

To construct index:

    $ ./index graph_file_name index_file_name

To query index:

    $ ./query index_file_name query_file_name

`Sample Datasets/` folder provides a sample graph and a sample file containing query pairs

# References

* Muhammad Farhan, Henning Koehler, and Qing Wang, **[Divide-and-Conquer: Scalable Shortest Path Counting on Large Road Networks](https://dl.acm.org/doi/pdf/10.1145/3725400)**. SIGMOD 2025.
