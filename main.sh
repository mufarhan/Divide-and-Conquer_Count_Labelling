# Prepare dataset and queries
make
bash download.sh
bash generate_query.sh

# DCL
bash index_dcl.sh
bash query_dcl.sh

# TC
make -C TreeCount
bash index_tc.sh
bash query_tc.sh
