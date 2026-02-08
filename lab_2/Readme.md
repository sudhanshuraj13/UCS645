# Lab 2: OpenMP Parallel Programming Experiments

## Overview
This lab explores fundamental concepts in parallel programming using OpenMP, focusing on performance analysis, scalability, synchronization, and memory optimization. Seven comprehensive experiments demonstrate key parallel computing principles and their practical implications.

---

## Experiment 1: Execution Time Measurement (Vector Addition)

### Objective
Measure execution time of parallel vector addition using OpenMP with varying thread counts (1-9 threads).

### Implementation
- **Vector Size**: 100,000,000 elements
- **Operation**: `C[i] = A[i] + B[i]`
- **Parallelization**: `#pragma omp parallel for`

### Observation
- **Best Performance**: 3 threads (0.164s) - 2.27x speedup
- **Optimal Range**: 3-4 threads
- **Performance Degradation**: Beyond 4 threads, overhead outweighs benefits
- **Memory-Bound Nature**: Vector addition is limited by memory bandwidth, not computation

### Conclusion
Vector addition demonstrates that more threads don't always mean better performance. The workload is memory-bound, and optimal performance occurs at 3-4 threads with diminishing returns beyond that point.

---

## Experiment 2: Speedup, Parallel Efficiency & Throughput

### Objective
Evaluate performance scaling by calculating speedup, parallel efficiency, and throughput using Experiment 1 data.

### Formulas
- **Speedup**: S(p) = T₁ / Tₚ
- **Efficiency**: E(p) = S(p) / p × 100%
- **Throughput**: N / Tₚ (operations/second)

### Observation
- **Super-linear Speedup**: 2 threads achieved 107% efficiency due to improved cache utilization
- **Peak Throughput**: 609.8 million ops/sec at 3 threads (2.27x improvement)
- **Rapid Efficiency Decline**: From 75.67% (3 threads) to 24.56% (9 threads)
- **Scalability Limit**: Efficiency drops below 50% after 4 threads

### Conclusion
The experiment reveals that parallel efficiency degrades rapidly beyond 3-4 threads for memory-bound operations. The 2-thread super-linear speedup demonstrates the importance of cache effects in parallel performance.

---

## Experiment 3: Strong Scaling and Weak Scaling

### Objective
Analyze scalability using π calculation with numerical integration, evaluating both strong and weak scaling metrics.

### Implementation
- **Problem**: Calculate π using Riemann sum
- **Strong Scaling**: Fixed 500M iterations across varying cores
- **Weak Scaling**: 100M iterations per core (constant workload per core)

### Results

**Strong Scaling** (Fixed workload):
| Cores | Time (s) | Speedup |
### Implementation
- **Problem**: Calculate π using Riemann sum
- **Strong Scaling**: Fixed 500M iterations across varying cores
- **Weak Scaling**: 100M iterations per core (constant workload per core)

### Observation

## Experiment 4: Scheduling and Load Imbalance

### Objective
Compare OpenMP loop scheduling strategies (static, dynamic, guided) for imbalanced workloads.

### Implementation
- **Workload**: Progressive computation - iteration i requires (i+1)×50,000 operations
- **Total Iterations**: 1,000
- **Scheduling Strategies**: static, dynamic (chunk=4), guided

### Results
| Schedule  | T_max (s) | T_avg (s) | Imbalance |
|-----------|-----------|-----------|-----------|
| static    | 233.29    | 112.63    | 107.13%   |
| dynamic,4 | 172.87    | 168.96    | 2.31%     |
| guided    | 167.69    | 166.68    | 0.60%     |

### Key Findings
- **Static Scheduling**: Catastrophic 107% imbalance - some threads finish 2x faster than others
- **Dynamic Scheduling**: Dramatically reduced to 2.31% imbalance, 26% faster than static
- **Guided Scheduling**: Best performance with only 0.60% imbalance, 28% faster than static
- **Performance Impact**: Poor scheduling can more than double execution time

### Conclusion
For workloads with variable iteration costs, **guided scheduling provides optimal load balancing** with minimal overhead. Static scheduling should only be used when all iterations have similar execution times. The experiment demonstrates that scheduling strategy is critical for performance in imbalanced workloads.
### Implementation
- **Workload**: Progressive computation - iteration i requires (i+1)×50,000 operations
- **Total Iterations**: 1,000
- **Scheduling Strategies**: static, dynamic (chunk=4), guided

### Observation
| Method           | Time (s) | Speedup |
|------------------|----------|---------|
### Implementation
- **Workload**: Parallel summation of 10 million iterations
- **Methods**: Critical section (mutual exclusion) vs Reduction (thread-private copies)

### Observationdemonstrates the **critical importance of choosing appropriate synchronization mechanisms**. For accumulation operations, reduction provides 72x better performance. Critical sections should be reserved for complex operations that cannot use reduction. The massive overhead shows why understanding synchronization is essential for efficient parallel programming.

---

## Experiment 6: False Sharing and Cache Line Contention

### Objective
Investigate performance impact of false sharing and demonstrate mitigation through padding.

### Implementation
Two implementations tested:
1. **Struct-based**: UnpaddedData vs PaddedData (with 64-byte alignment)
2. **Array-based**: Adjacent elements vs cache-line separated elements

### Results
### Implementation
Two implementations tested:
1. **Struct-based**: UnpaddedData vs PaddedData (with 64-byte alignment)
2. **Array-based**: Adjacent elements vs cache-line separated elements

### Observation
False sharing is a **critical hardware-level bottleneck** causing 3-5x slowdowns. Simple padding to 64-byte cache line boundaries eliminates the problem. The experiment shows that understanding cache coherence is essential for parallel programming - even logically independent operations can interfere at the hardware level.

---

## Experiment 7: Memory Bandwidth Saturation

### Objective
Measure memory bandwidth limitations using the Triad kernel (A = B + scalar × C).

### Implementation
- **Operation**: `A[i] = B[i] + 3.3 * C[i]`
- **Array Size**: 100 million elements (2.4 GB total)
- **Bandwidth Formula**: (3 × N × 8 bytes) / T_p

### Results
| Cores | Time (s) | Bandwidth (GB/s) | Speedup |
|-------|----------|------------------|---------|
| 1     | 0.838    | 2.86             | 1.00x   |
| 2     | 0.208    | 11.54            | 4.03x   |
| 3     | 0.174    | 13.79            | 4.82x   |
| 4     | 0.177    | 13.56            | 4.73x   |
| 8     | 0.170    | 14.12            | 4.93x   |

### Implementation
- **Operation**: `A[i] = B[i] + 3.3 * C[i]`
- **Array Size**: 100 million elements (2.4 GB total)
- **Bandwidth Formula**: (3 × N × 8 bytes) / T_p

### ObservationLearned

1. **Not All Workloads Scale Equally**
   - Compute-bound (Exp 3): Near-linear scaling
   - Memory-bound (Exp 1, 7): Limited by bandwidth, plateaus early
   - Load-imbalanced (Exp 4): Requires intelligent scheduling

2. **Synchronization Matters Enormously**
   - Wrong choice (critical section) can cause 72x slowdown
   - Reduction is optimal for accumulation operations
   - Minimize synchronization frequency and scope

3. **Hardware Effects Are Real**
   - False sharing (Exp 6): 3-5x slowdown from cache coherence
   - Memory bandwidth (Exp 7): Physical limits cap parallelism
   - Cache effects: Can cause super-linear speedup (Exp 2)

4. **Optimal Thread Count Varies**
   - Memory-bound: 3-4 threads optimal
   - Compute-bound: Scales to available cores
   - Always measure - more threads ≠ better performance

5. **Scheduling Strategy Is Critical**
   - Static: Only for uniform workloads
   - Dynamic: Good for moderate imbalance
   - Guided: Best for highly variable workloads

### Performance Spectrum Summary

| Experiment | Best Speedup | Efficiency | Bottleneck       |
|------------|--------------|------------|------------------|
| Exp 1      | 2.27x (3T)   | 75.67%     | Memory bandwidth |
| Exp 2      | 2.27x (3T)   | 75.67%     | Memory bandwidth |
| Exp 3      | 11.36x (20T) | >83%       | Computation      |
| Exp 4      | 72% faster   | N/A        | Load imbalance   |
| Exp 5      | 72.25x       | N/A        | Synchronization  |
| Exp 6      | 5.11x        | N/A        | False sharing    |
| Exp 7      | 4.93x (8T)   | 61.6%      | Memory bandwidth |

### Best Practices Derived

1. **Profile Before Parallelizing**: Identify compute vs memory-bound bottlenecks
2. **Choose Right Synchronization**: Prefer reduction over critical sections
3. **Consider Cache Lines**: Pad data structures to avoid false sharing
4. **Use Appropriate Scheduling**: Match strategy to workload characteristics
5. **Measure Efficiency**: Track speedup and efficiency, not just execution time
6. **Understand Hardware Limits**: Memory bandwidth and cache coherence matter
7. **Right-size Thread Count**: Optimal count depends on workload type

### When to Use OpenMP

**Good Candidates**:
- Compute-intensive loops (matrix operations, numerical integration)
- Embarrassingly parallel problems
- Large data sets with independent operations

**Poor Candidates**:
- Memory-bandwidth limited operations
- Highly serialized algorithms
- Fine-grained parallelism with high overhead
- Small data sets where overhead dominates

---

## Lab Statistics

- **Total Experiments**: 7
- **Programming Language**: C with OpenMP
- **Total Lines of Code**: ~500 lines across all experiments
- **Visualization Scripts**: 7 Python scripts for performance analysis
- **Key Metrics Measured**: Execution time, speedup, efficiency, throughput, bandwidth, imbalance
- **Thread Counts Tested**: 1-23 cores depending on experiment
- **Largest Dataset**: 2.4 GB (Experiment 7)

---

## Compilation Instructions

All experiments compiled with:
```bash
gcc -fopenmp <filename>.c -o <output> -lm
```

## Files Structure
```
lab_2/
├── exp1/ - Execution Time Measurement
├── exp2/ - Speedup & Efficiency Analysis
├── exp3/ - Strong & Weak Scaling
├── exp4/ - Scheduling Strategies
├── exp5/ - Synchronization Overhead
├── exp6/ - False Sharing
└── exp7/ - Memory Bandwidth Saturation
```

Each experiment folder contains:
- C source code
- Python plotting script
- Detailed README with analysis
- Generated performance graphs

---

## References
- OpenMP Specification 5.0
- "Parallel Programming in OpenMP" by Rohit Chandra et al.
- STREAM Benchmark Documentation
- Intel Threading Building Blocks Documentation