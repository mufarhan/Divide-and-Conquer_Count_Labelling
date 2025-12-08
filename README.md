# Divide and Conquer Labelling (DCL) and TreeCount

This repository provides the implementation of Divide and Conquer Labelling (DCL), a method for accelerating shortest-path counting queries on large road networks. A baseline method, TreeCount, is included for comparison.

## Repository Structure

**src/**  
Contains the DCL implementation:  
• `road_network.h/.cpp` – core graph library  
• `util.h/.cpp` – utility functions  
• `index.cpp` – builds a DCL index  
• `query.cpp` – loads an index and answers queries

**TreeCount/**  
Baseline TreeCount implementation and scripts.

**Sample Datasets/**  
Example graph and query-pair files.

**main.sh**  
Runs both DCL and TreeCount for comparative evaluation.

## Compilation

From the `src/` directory:
```bash
make
````

## Usage

### Build a DCL index

```bash
./index <graph_file> <index_file>
```

### Query using a DCL index

```bash
./query <index_file> <query_file>
```

Sample data is provided in `Sample Datasets/`.

## Datasets

Real-world road networks used in the project can be downloaded from:
[http://www.diag.uniroma1.it/~challenge9/download.shtml](http://www.diag.uniroma1.it/~challenge9/download.shtml)

## Running Both Methods

Use:

```bash
./main.sh
```

to compile and run DCL and TreeCount on the same dataset.

```
```

# Datasets

 Real road networks used in this paper can be found at http://www.diag.uniroma1.it/~challenge9/download.shtml

# References

* Muhammad Farhan, Henning Koehler, and Qing Wang, **[Divide-and-Conquer: Scalable Shortest Path Counting on Large Road Networks](https://dl.acm.org/doi/pdf/10.1145/3725400)**. SIGMOD 2025.
