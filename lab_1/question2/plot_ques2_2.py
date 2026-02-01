import matplotlib.pyplot as plt

# Data from the execution results
threads = [2, 3, 4, 5, 6, 7, 8, 9]
times = [3.238, 2.298, 1.850, 1.994, 1.483, 1.484, 1.452, 1.562]

# Estimate serial time (T1) using T2 * 2
T1 = times[0] * 2  # Estimated serial time

# Calculate speedup: S = T1 / Tp
speedup = [T1 / t for t in times]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(threads, speedup, marker='o', linewidth=2, markersize=8, color='green', label='Actual Speedup')
plt.plot(threads, threads, linestyle='--', color='red', label='Ideal Speedup')

plt.xlabel('Number of Threads', fontsize=12)
plt.ylabel('Speedup', fontsize=12)
plt.title('Speedup vs Number of Threads (2D Parallel Matrix Multiplication - collapse(2))', fontsize=14)
plt.xticks(threads)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.tight_layout()
plt.savefig('speedup_ques2_2.png', dpi=150)
plt.show()

print("Graph saved as speedup_ques2_2.png")
