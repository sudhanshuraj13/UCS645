#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define N 1000

int main(int argc, char* argv[]) {

    static double A[N][N], B[N][N], C[N][N];

    // Initialize matrices A and B
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) {
            A[i][j] = 1.0;
            B[i][j] = 1.0;
        }

    // Loop from 2 threads to 9 threads
    for (int threads = 2; threads <= 9; threads++) {
        // Reset matrix C for each iteration
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                C[i][j] = 0.0;

        double start = omp_get_wtime();

        #pragma omp parallel for collapse(2) num_threads(threads)
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                for (int k = 0; k < N; k++)
                    C[i][j] += A[i][k] * B[k][j];

        double end = omp_get_wtime();

        printf("2D Threads is: %d  Time is: %f seconds\n", threads, end - start);
    }

    return 0;
}