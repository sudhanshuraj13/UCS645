import matplotlib.pyplot as plt

# Data from Experiment 2
threads = [1, 2, 3, 4, 5, 6, 7, 8, 9]
time = [0.372, 0.174, 0.164, 0.168, 0.182, 0.189, 0.173, 0.168, 0.168]
speedup = [1.00, 2.14, 2.27, 2.21, 2.04, 1.97, 2.15, 2.21, 2.21]
efficiency = [100.00, 107.00, 75.67, 55.25, 40.80, 32.83, 30.71, 27.63, 24.56]
throughput = [268.8, 574.7, 609.8, 595.2, 549.5, 529.1, 578.0, 595.2, 595.2]

# Create figure with 2x2 subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# 1. Speedup vs Threads
ax1.plot(threads, speedup, marker='o', linewidth=2, markersize=8, color='blue', label='Speedup')
ax1.plot(threads, threads, '--', color='red', alpha=0.5, label='Ideal Speedup')
ax1.set_xlabel('Number of Threads', fontsize=11)
ax1.set_ylabel('Speedup S(p)', fontsize=11)
ax1.set_title('Speedup vs Number of Threads', fontsize=12, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_xticks(threads)

# 2. Parallel Efficiency vs Threads
ax2.plot(threads, efficiency, marker='s', linewidth=2, markersize=8, color='green')
ax2.axhline(y=100, color='red', linestyle='--', alpha=0.5, label='100% Efficiency')
ax2.set_xlabel('Number of Threads', fontsize=11)
ax2.set_ylabel('Efficiency E(p) (%)', fontsize=11)
ax2.set_title('Parallel Efficiency vs Number of Threads', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.set_xticks(threads)

# 3. Throughput vs Threads
ax3.plot(threads, throughput, marker='^', linewidth=2, markersize=8, color='purple')
ax3.set_xlabel('Number of Threads', fontsize=11)
ax3.set_ylabel('Throughput (M ops/s)', fontsize=11)
ax3.set_title('Throughput vs Number of Threads', fontsize=12, fontweight='bold')
ax3.grid(True, alpha=0.3)
ax3.set_xticks(threads)

# 4. Execution Time vs Threads
ax4.plot(threads, time, marker='d', linewidth=2, markersize=8, color='orange')
ax4.set_xlabel('Number of Threads', fontsize=11)
ax4.set_ylabel('Execution Time (seconds)', fontsize=11)
ax4.set_title('Execution Time vs Number of Threads', fontsize=12, fontweight='bold')
ax4.grid(True, alpha=0.3)
ax4.set_xticks(threads)

plt.tight_layout()
plt.savefig('performance_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("Performance analysis plots saved as 'performance_analysis.png'")

# Create individual plots as well
# Speedup plot
plt.figure(figsize=(10, 6))
plt.plot(threads, speedup, marker='o', linewidth=2, markersize=8, color='blue', label='Actual Speedup')
plt.plot(threads, threads, '--', color='red', alpha=0.5, label='Ideal Speedup')
plt.xlabel('Number of Threads', fontsize=12)
plt.ylabel('Speedup S(p)', fontsize=12)
plt.title('Speedup vs Number of Threads', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.xticks(threads)
for i, (t, s) in enumerate(zip(threads, speedup)):
    plt.text(t, s + 0.05, f'{s:.2f}', ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('speedup_vs_threads.png', dpi=300)
plt.show()

# Efficiency plot
plt.figure(figsize=(10, 6))
plt.plot(threads, efficiency, marker='s', linewidth=2, markersize=8, color='green')
plt.axhline(y=100, color='red', linestyle='--', alpha=0.5, label='100% Efficiency')
plt.xlabel('Number of Threads', fontsize=12)
plt.ylabel('Efficiency E(p) (%)', fontsize=12)
plt.title('Parallel Efficiency vs Number of Threads', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.xticks(threads)
for i, (t, e) in enumerate(zip(threads, efficiency)):
    plt.text(t, e + 2, f'{e:.1f}%', ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('efficiency_vs_threads.png', dpi=300)
plt.show()

# Throughput plot
plt.figure(figsize=(10, 6))
plt.plot(threads, throughput, marker='^', linewidth=2, markersize=8, color='purple')
plt.xlabel('Number of Threads', fontsize=12)
plt.ylabel('Throughput (M ops/s)', fontsize=12)
plt.title('Throughput vs Number of Threads', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.xticks(threads)
for i, (t, th) in enumerate(zip(threads, throughput)):
    plt.text(t, th + 10, f'{th:.1f}', ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('throughput_vs_threads.png', dpi=300)
plt.show()

print("Individual plots saved:")
print("- speedup_vs_threads.png")
print("- efficiency_vs_threads.png")
print("- throughput_vs_threads.png")
