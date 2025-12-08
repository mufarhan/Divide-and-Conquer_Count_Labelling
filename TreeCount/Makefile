CC=g++ -march=native -O3
CFLAGS=-c -I. -std=c++0x -Wfatal-errors

all: TC_index TC_query

TC_index: TreeCount.o Graph.o TreeDecomp.o
	$(CC) TreeCount.o Graph.o TreeDecomp.o -o TC_index
	
TC_query: TreeCountQuery.o Graph.o TreeDecomp.o
	$(CC) TreeCountQuery.o Graph.o TreeDecomp.o -o TC_query

TreeCountQuery.o: src/TreeCountQuery.cpp
	$(CC) $(CFLAGS) src/TreeCountQuery.cpp -o TreeCountQuery.o

TreeCount.o: src/TreeCount.cpp
	$(CC) $(CFLAGS) src/TreeCount.cpp -o TreeCount.o

Graph.o: src/Graph.cpp
	$(CC) $(CFLAGS) src/Graph.cpp -o Graph.o

TreeDecomp.o: src/TreeDecomp.cpp
	$(CC) $(CFLAGS) src/TreeDecomp.cpp -o TreeDecomp.o

.PHONY: clean
clean:
	-rm *.o
