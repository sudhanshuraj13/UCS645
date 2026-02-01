#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main(int argc, char* argv[]) {

    long n = 10000000;
    double s = 1.0 / n;

    for (int t = 2; t <= 9; t++) {
        double sum = 0.0;

        double start = omp_get_wtime();

        #pragma omp parallel for num_threads(t) reduction(+:sum)
        for (long i = 0; i < n; i++) {
            double x = (i + 0.5) * s;
            sum += 4.0 / (1.0 + x * x);
        }

        double pi = s * sum;
        double end = omp_get_wtime();

        printf("Threads: %d  Pi: %.10f  Time: %f seconds\n", t, pi, end - start);
    }

    return 0;
}