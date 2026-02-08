#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

#define CACHE_LINE_SIZE 8

typedef struct {
    double value;
} UnpaddedData;

typedef struct {
    double value;
    double padding[CACHE_LINE_SIZE];
} PaddedData;

int main() {
    const long long iterations = 100000000;
    int n_threads = omp_get_max_threads();
    
    UnpaddedData *unpadded = (UnpaddedData*)calloc(n_threads, sizeof(UnpaddedData));
    PaddedData *padded = (PaddedData*)calloc(n_threads, sizeof(PaddedData));

    printf("%-20s %s\n", "Configuration", "Time (s)");
    printf("----------------------------------------\n");

    double s1 = omp_get_wtime();
    #pragma omp parallel num_threads(n_threads)
    {
        int tid = omp_get_thread_num();
        for (long long i = 0; i < iterations; i++) {
            unpadded[tid].value += 1.0;
        }
    }
    double e1 = omp_get_wtime();
    printf("%-20s %.6fs\n", "False Sharing:", e1 - s1);

    double s2 = omp_get_wtime();
    #pragma omp parallel num_threads(n_threads)
    {
        int tid = omp_get_thread_num();
        for (long long i = 0; i < iterations; i++) {
            padded[tid].value += 1.0;
        }
    }
    double e2 = omp_get_wtime();
    printf("%-20s %.6fs\n", "Padded (Fixed):", e2 - s2);

    free(unpadded);
    free(padded);

    return 0;
}