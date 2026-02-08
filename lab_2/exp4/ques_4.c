#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

void work(int i) {
    double dummy = 0;
    long long limit = (i + 1) * 50000; 
    for (long long j = 0; j < limit; ++j) {
        dummy += sin(j) * cos(j);
    }
}

void measure_imbalance(const char* schedule_name, int schedule_type, int n_threads, int N) {
    double *thread_times = (double*)calloc(n_threads, sizeof(double));
    
    #pragma omp parallel num_threads(n_threads)
    {
        int tid = omp_get_thread_num();
        double start_thread = omp_get_wtime();
        
        if (schedule_type == 0) {
            #pragma omp for schedule(static) nowait
            for (int i = 0; i < N; i++) work(i);
        } else if (schedule_type == 1) {
            #pragma omp for schedule(dynamic, 4) nowait
            for (int i = 0; i < N; i++) work(i);
        } else if (schedule_type == 2) {
            #pragma omp for schedule(guided) nowait
            for (int i = 0; i < N; i++) work(i);
        }
        
        double end_thread = omp_get_wtime();
        thread_times[tid] = end_thread - start_thread;
    }
    
    double t_max = 0.0;
    double t_sum = 0.0;
    for (int i = 0; i < n_threads; i++) {
        if (thread_times[i] > t_max) t_max = thread_times[i];
        t_sum += thread_times[i];
    }
    double t_avg = t_sum / n_threads;
    double imbalance = (t_max - t_avg) / t_avg;
    
    printf("%-15s %-11.4fs %-11.4fs %.2f%%\n", 
           schedule_name, t_max, t_avg, imbalance * 100);
    
    free(thread_times);
}

int main() {
    int N = 1000;
    int n_threads = omp_get_max_threads();
    
    printf("Running on %d threads...\n", n_threads);
    printf("%-15s %-12s %-12s %s\n", "Schedule", "T_max", "T_avg", "Imbalance (%)");
    printf("-------------------------------------------------------\n");
    
    measure_imbalance("static", 0, n_threads, N);
    measure_imbalance("dynamic,4", 1, n_threads, N);
    measure_imbalance("guided", 2, n_threads, N);
    
    return 0;
}