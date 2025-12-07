CC = g++ -std=c++2a -O3 -Wall -Wextra -pthread -o
TCC = g++ -std=c++2a -ggdb -Wall -Wextra -o
INC = src/road_network.cpp src/util.cpp

all: index query query_generator

index:
	$(CC) index src/index.cpp $(INC)
query:
	$(CC) query src/query.cpp $(INC)
query_generator:
	$(CC) query_generator src/query_generator.cpp $(INC)

clean:
	rm index query query_generator

.PHONY: index query query_generator
