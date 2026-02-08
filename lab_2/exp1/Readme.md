# Experiment 1 — Execution Time Measurement (Vector Addition)

## Objective
Measure execution time of parallel vector addition using OpenMP with different thread counts (1-9 threads).

## Implementation
- **Vector Size**: 100,000,000 elements
- **Operation**: C[i] = A[i] + B[i]
- **Parallelization**: OpenMP `#pragma omp parallel for`

## Results

| Threads | Time (seconds) |
|---------|----------------|
| 1       | 0.372          |
| 2       | 0.174          |
| 3       | 0.164          |
| 4       | 0.168          |
| 5       | 0.182          |
| 6       | 0.189          |
| 7       | 0.173          |
| 8       | 0.168          |
| 9       | 0.168          |

## Analysis
- **Best Performance**: 3 threads (0.164s) - 2.27x speedup
- **Optimal Range**: 3-4 threads
- **Key Insight**: Vector addition is memory-bound. Beyond 4 threads, overhead outweighs benefits.

## Compilation
```bash
gcc -fopenmp ques_1.c -o ques_1
```
