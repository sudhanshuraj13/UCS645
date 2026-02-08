#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main() {
    
    int N = 1 << 16;  
    
    double *X = malloc(N * sizeof(double));
    double *Y = malloc(N * sizeof(double));
    double a = 3.0;
    
    for (int i = 0; i < N; i++) {
        X[i] = 1.0;
        Y[i] = 2.0;
    }
    
    double start_seq = omp_get_wtime();
    for (int i = 0; i < N; i++) {
        X[i] = a * X[i] + Y[i];
    }
    double end_seq = omp_get_wtime();
    double time_seq = end_seq - start_seq;
    
    for (int threads = 2; threads <= 9; threads++) {
        for (int i = 0; i < N; i++) {
            X[i] = 1.0;
            Y[i] = 2.0;
        }
        
        double start = omp_get_wtime();
        
        #pragma omp parallel for num_threads(threads)
        for (int i = 0; i < N; i++) {
            X[i] = a * X[i] + Y[i];
        }
        
        double end = omp_get_wtime();
        double time_parallel = end - start;
        double speedup = time_seq / time_parallel;
        
        printf("Threads: %d  Time: %f seconds\n", threads, time_parallel, speedup);
    }
    
    free(X);
    free(Y);
    
    return 0;
}

