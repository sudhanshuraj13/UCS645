import matplotlib.pyplot as plt
import numpy as np

# Experimental results
cores = [1, 2, 3, 4, 5, 6, 7, 8]
time = [0.838, 0.208, 0.174, 0.177, 0.171, 0.176, 0.173, 0.170]
bandwidth = [2.86, 11.54, 13.79, 13.56, 14.04, 13.64, 13.87, 14.12]
speedup = [1.00, 4.03, 4.82, 4.73, 4.90, 4.76, 4.84, 4.93]

# Create figure with 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

# 1. Execution Time vs Cores
ax1.plot(cores, time, 'o-', color='red', linewidth=2, markersize=8, label='Execution Time')
ax1.set_xlabel('Number of Cores', fontsize=12)
ax1.set_ylabel('Execution Time (seconds)', fontsize=12)
ax1.set_title('Execution Time vs Number of Cores', fontsize=13, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.set_xticks(cores)

# Add value labels
for i, (c, t) in enumerate(zip(cores, time)):
    ax1.text(c, t + 0.02, f'{t:.3f}s', ha='center', fontsize=9)

# 2. Memory Bandwidth vs Cores
ax2.plot(cores, bandwidth, 'o-', color='blue', linewidth=2, markersize=8, label='Bandwidth')
ax2.axhline(y=max(bandwidth), color='green', linestyle='--', alpha=0.5, label=f'Peak: {max(bandwidth):.2f} GB/s')
ax2.set_xlabel('Number of Cores', fontsize=12)
ax2.set_ylabel('Bandwidth (GB/s)', fontsize=12)
ax2.set_title('Memory Bandwidth vs Number of Cores', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=10)
ax2.set_xticks(cores)

# Add value labels
for i, (c, bw) in enumerate(zip(cores, bandwidth)):
    ax2.text(c, bw + 0.3, f'{bw:.2f}', ha='center', fontsize=9)

# 3. Speedup vs Cores
ax3.plot(cores, speedup, 'o-', color='green', linewidth=2, markersize=8, label='Actual Speedup')
ax3.plot(cores, cores, '--', color='gray', linewidth=1.5, label='Ideal Linear Speedup')
ax3.set_xlabel('Number of Cores', fontsize=12)
ax3.set_ylabel('Speedup', fontsize=12)
ax3.set_title('Speedup vs Number of Cores', fontsize=13, fontweight='bold')
ax3.grid(True, alpha=0.3)
ax3.legend(fontsize=10)
ax3.set_xticks(cores)

# Add value labels
for i, (c, s) in enumerate(zip(cores, speedup)):
    ax3.text(c, s + 0.15, f'{s:.2f}x', ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('triad_benchmark_results.png', dpi=300, bbox_inches='tight')
plt.show()

print("Combined plot saved as 'triad_benchmark_results.png'")

# Individual detailed plots
# 1. Execution Time
plt.figure(figsize=(10, 6))
plt.plot(cores, time, 'o-', color='red', linewidth=3, markersize=10)
plt.fill_between(cores, 0, time, alpha=0.3, color='lightcoral')
plt.xlabel('Number of Cores', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.title('Execution Time vs Number of Cores (Triad Kernel)', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.xticks(cores)

for c, t in zip(cores, time):
    plt.text(c, t + 0.02, f'{t:.3f}s', ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('execution_time_vs_cores.png', dpi=300, bbox_inches='tight')
plt.show()

# 2. Memory Bandwidth
plt.figure(figsize=(10, 6))
plt.plot(cores, bandwidth, 'o-', color='blue', linewidth=3, markersize=10)
plt.fill_between(cores, 0, bandwidth, alpha=0.3, color='skyblue')
plt.axhline(y=max(bandwidth), color='red', linestyle='--', linewidth=2, 
            label=f'Peak Bandwidth: {max(bandwidth):.2f} GB/s')
plt.xlabel('Number of Cores', fontsize=12)
plt.ylabel('Memory Bandwidth (GB/s)', fontsize=12)
plt.title('Memory Bandwidth Scaling', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.xticks(cores)

for c, bw in zip(cores, bandwidth):
    plt.text(c, bw + 0.4, f'{bw:.2f}\nGB/s', ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('bandwidth_vs_cores.png', dpi=300, bbox_inches='tight')
plt.show()

# 3. Speedup Analysis
plt.figure(figsize=(10, 6))
plt.plot(cores, speedup, 'o-', color='green', linewidth=3, markersize=10, label='Actual Speedup')
plt.plot(cores, cores, '--', color='red', linewidth=2, alpha=0.7, label='Ideal Linear Speedup')
plt.fill_between(cores, speedup, alpha=0.3, color='lightgreen')
plt.xlabel('Number of Cores', fontsize=12)
plt.ylabel('Speedup Factor', fontsize=12)
plt.title('Speedup vs Number of Cores (Strong Scaling)', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.xticks(cores)

for c, s in zip(cores, speedup):
    plt.text(c, s + 0.2, f'{s:.2f}x', ha='center', fontsize=10, fontweight='bold')

# Add efficiency annotations
efficiency_2 = (speedup[1] / 2) * 100
efficiency_8 = (speedup[-1] / 8) * 100
plt.text(2, speedup[1] - 0.5, f'Efficiency: {efficiency_2:.1f}%', ha='center', fontsize=9, 
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
plt.text(8, speedup[-1] - 0.5, f'Efficiency: {efficiency_8:.1f}%', ha='center', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
plt.savefig('speedup_vs_cores.png', dpi=300, bbox_inches='tight')
plt.show()

# Efficiency plot
plt.figure(figsize=(10, 6))
efficiency = [(s / c) * 100 for s, c in zip(speedup, cores)]
colors = ['green' if e >= 60 else 'orange' if e >= 50 else 'red' for e in efficiency]

bars = plt.bar(cores, efficiency, color=colors, edgecolor='black', linewidth=1.5)
plt.axhline(y=100, color='blue', linestyle='--', linewidth=1, label='100% Efficiency (Ideal)')
plt.xlabel('Number of Cores', fontsize=12)
plt.ylabel('Parallel Efficiency (%)', fontsize=12)
plt.title('Parallel Efficiency vs Number of Cores', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')
plt.legend(fontsize=11)
plt.xticks(cores)

for bar, eff in zip(bars, efficiency):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{eff:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('efficiency_vs_cores.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nAll individual plots saved:")
print("- execution_time_vs_cores.png")
print("- bandwidth_vs_cores.png")
print("- speedup_vs_cores.png")
print("- efficiency_vs_cores.png")
