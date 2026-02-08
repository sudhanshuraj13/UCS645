import matplotlib.pyplot as plt

# Data from your results
threads = [1, 2, 3, 4, 5, 6, 7, 8, 9]
time = [0.372, 0.174, 0.164, 0.168, 0.182, 0.189, 0.173, 0.168, 0.168]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(threads, time, marker='o', linewidth=2, markersize=8, color='blue')
plt.xlabel('Number of Threads', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.title('OpenMP Vector Addition Performance vs Number of Threads', fontsize=14)
plt.grid(True, alpha=0.3)
plt.xticks(threads)

# Add value labels on each point
for i, (t, val) in enumerate(zip(threads, time)):
    plt.text(t, val + 0.01, f'{val:.3f}s', ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('thread_performance.png', dpi=300)
plt.show()

print("Plot saved as 'thread_performance.png'")