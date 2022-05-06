DuckDB implementatation of the queries from the [PublicBI dataset](https://github.com/cwida/public_bi_benchmark)

The PublicBI dataset does not (yet) contain results as many queries do not contain ORDER BY clauses.
However, it is a suitable benchmark for evaluating compression or operating on larger (real-life) datasets.

Run the [Python script](download-data-and-results.py) to download (part) of the data. 
Then choose to run a query from the [queries](queries) directory or test compression/checkpointing performance
using the benchmarks in the [checkpoints](checkpoints) directory.

The original dataset was compressed with bzip2. They have been compressed with GZIP to work
directly in DuckDB. These can be found [here](https://zenodo.org/record/6277287) and 
[here](https://zenodo.org/record/6344717).