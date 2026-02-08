import matplotlib.pyplot as plt

# Data from program output
threads = [2, 3, 4, 5, 6, 7, 8, 9]

# Speedup values (scaled between 0.0 to 1.0)
# Thread 2 = 1.0 (baseline), decreasing as threads increase due to overhead
speedup = [1.0, 0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25]

# Create Speedup vs Threads plot (similar to reference image)
plt.figure(figsize=(10, 6))
plt.plot(threads, speedup, 'b-o', linewidth=2, markersize=8)

plt.xlabel('Threads', fontsize=12)
plt.ylabel('Speedup', fontsize=12)
plt.title('Q1 DAXPY Speedup vs Threads', fontsize=14)
plt.grid(True, alpha=0.3)
plt.xticks([2, 3, 4, 5, 6, 7, 8, 9])
plt.ylim(0.0, 1.1)

plt.tight_layout()
plt.savefig('ques1_speedup.png', dpi=150)
plt.show()

print("Graph saved as 'ques1_speedup.png'")
