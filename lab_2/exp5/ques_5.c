#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

void test_sync_methods(long long N) {
    double sum_critical = 0.0;
    double sum_reduction = 0.0;
    
    double start = omp_get_wtime();
    #pragma omp parallel for
    for (long long i = 0; i < N; i++) {
        #pragma omp critical
        {
            sum_critical += 1.0; 
        }
    }
    double end = omp_get_wtime();
    double time_critical = end - start;
    
    start = omp_get_wtime();
    #pragma omp parallel for reduction(+:sum_reduction)
    for (long long i = 0; i < N; i++) {
        sum_reduction += 1.0;
    }
    end = omp_get_wtime();
    double time_reduction = end - start;
    
    printf("%-20s %s\n", "Method", "Time (s)");
    printf("------------------------------------\n");
    printf("%-20s %.6fs\n", "Critical Section", time_critical);
    printf("%-20s %.6fs\n", "Reduction", time_reduction);
    
    if (time_reduction > 0) {
        printf("\nOverhead Factor: %.2fx slower\n", time_critical / time_reduction);
    }
}

int main() {
    test_sync_methods(10000000); 
    return 0;
}