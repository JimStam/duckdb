import subprocess
import os
import re

duckdb_root_dir = "duckdb"
final_averages = []

for file in sorted(os.listdir(".")):
    if file.endswith(".benchmark"):
        print(file)
        # Run the benchmark runner
        benchmark_run = subprocess.run([f"{duckdb_root_dir}/build/release/benchmark/benchmark_runner",
                                        f"benchmark/micro/compression/rle_sorted/{file}"], capture_output=True)

        # Parse the output
        benchmark_run = benchmark_run.stderr.decode('utf-8')
        print(benchmark_run)
        result_list = re.split('[\t \n]', benchmark_run)
        run_result_indexes = [5, 8, 11, 14, 17]
        result_list = [float(result_list[i]) for i in run_result_indexes]

        # Compute average checkpointing time
        average_run_time = sum(result_list)/len(result_list)

        # Add to final results
        final_averages.append(average_run_time)

print(final_averages)