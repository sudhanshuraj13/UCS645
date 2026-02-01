import matplotlib.pyplot as plt

threads = [2, 3, 4, 5, 6, 7, 8, 9]
times = [0.032, 0.020, 0.021, 0.016, 0.012, 0.015, 0.012, 0.016]

T1 = times[0] * 2
speedup = [T1 / t for t in times]

plt.figure(figsize=(10, 6))
plt.plot(threads, speedup, marker='o', linewidth=2, markersize=8, color='purple', label='Actual Speedup')
plt.plot(threads, threads, linestyle='--', color='red', label='Ideal Speedup')

plt.xlabel('Number of Threads', fontsize=12)
plt.ylabel('Speedup', fontsize=12)
plt.title('Speedup vs Number of Threads (Pi Calculation)', fontsize=14)
plt.xticks(threads)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.tight_layout()
plt.savefig('speedup_ques3.png', dpi=150)
plt.show()

print("Graph saved as speedup_ques3.png")
