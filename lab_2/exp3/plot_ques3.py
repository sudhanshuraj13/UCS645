import matplotlib.pyplot as plt

# STRONG SCALING DATA (from your results - you'll need to update these)
strong_cores = [1, 4, 8, 12, 16, 20]
strong_time = [2.5, 0.7, 0.4, 0.3, 0.25, 0.22]  # Replace with actual values
strong_speedup = [1.0, 3.57, 6.25, 8.33, 10.0, 11.36]  # Replace with actual values

# WEAK SCALING DATA (from your results - you'll need to update these)
weak_cores = [1, 4, 8, 12, 16, 20]
weak_time = [0.5, 0.52, 0.54, 0.56, 0.58, 0.60]  # Replace with actual values
weak_efficiency = [100, 96.15, 92.59, 89.29, 86.21, 83.33]  # Replace with actual values

# Create figure with 2x2 subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# 1. Strong Scaling: Execution Time vs Cores
ax1.plot(strong_cores, strong_time, marker='o', linewidth=2, markersize=8, color='blue')
ax1.set_xlabel('Number of Cores', fontsize=11)
ax1.set_ylabel('Execution Time (seconds)', fontsize=11)
ax1.set_title('Strong Scaling: Execution Time vs Cores', fontsize=12, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.set_xticks(strong_cores)

# 2. Strong Scaling: Speedup vs Cores
ax2.plot(strong_cores, strong_speedup, marker='s', linewidth=2, markersize=8, color='green', label='Actual Speedup')
ax2.plot(strong_cores, strong_cores, '--', color='red', alpha=0.5, label='Ideal Speedup')
ax2.set_xlabel('Number of Cores', fontsize=11)
ax2.set_ylabel('Speedup', fontsize=11)
ax2.set_title('Strong Scaling: Speedup vs Cores', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.set_xticks(strong_cores)

# 3. Weak Scaling: Execution Time vs Cores
ax3.plot(weak_cores, weak_time, marker='^', linewidth=2, markersize=8, color='purple')
ax3.set_xlabel('Number of Cores', fontsize=11)
ax3.set_ylabel('Execution Time (seconds)', fontsize=11)
ax3.set_title('Weak Scaling: Execution Time vs Cores', fontsize=12, fontweight='bold')
ax3.grid(True, alpha=0.3)
ax3.set_xticks(weak_cores)

# 4. Weak Scaling: Efficiency vs Cores
ax4.plot(weak_cores, weak_efficiency, marker='d', linewidth=2, markersize=8, color='orange')
ax4.axhline(y=100, color='red', linestyle='--', alpha=0.5, label='100% Efficiency')
ax4.set_xlabel('Number of Cores', fontsize=11)
ax4.set_ylabel('Efficiency (%)', fontsize=11)
ax4.set_title('Weak Scaling: Efficiency vs Cores', fontsize=12, fontweight='bold')
ax4.grid(True, alpha=0.3)
ax4.legend()
ax4.set_xticks(weak_cores)

plt.tight_layout()
plt.savefig('scaling_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("Scaling analysis plot saved as 'scaling_analysis.png'")

# Individual plots
# Strong Scaling - Time
plt.figure(figsize=(10, 6))
plt.plot(strong_cores, strong_time, marker='o', linewidth=2, markersize=8, color='blue')
plt.xlabel('Number of Cores', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.title('Strong Scaling: Execution Time vs Cores', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.xticks(strong_cores)
for i, (c, t) in enumerate(zip(strong_cores, strong_time)):
    plt.text(c, t + 0.05, f'{t:.2f}s', ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('strong_time_vs_cores.png', dpi=300)
plt.show()

# Strong Scaling - Speedup
plt.figure(figsize=(10, 6))
plt.plot(strong_cores, strong_speedup, marker='s', linewidth=2, markersize=8, color='green', label='Actual Speedup')
plt.plot(strong_cores, strong_cores, '--', color='red', alpha=0.5, label='Ideal Speedup')
plt.xlabel('Number of Cores', fontsize=12)
plt.ylabel('Speedup', fontsize=12)
plt.title('Strong Scaling: Speedup vs Cores', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.xticks(strong_cores)
for i, (c, s) in enumerate(zip(strong_cores, strong_speedup)):
    plt.text(c, s + 0.2, f'{s:.2f}x', ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('strong_speedup_vs_cores.png', dpi=300)
plt.show()

# Weak Scaling - Time
plt.figure(figsize=(10, 6))
plt.plot(weak_cores, weak_time, marker='^', linewidth=2, markersize=8, color='purple')
plt.xlabel('Number of Cores', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.title('Weak Scaling: Execution Time vs Cores', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.xticks(weak_cores)
for i, (c, t) in enumerate(zip(weak_cores, weak_time)):
    plt.text(c, t + 0.01, f'{t:.2f}s', ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('weak_time_vs_cores.png', dpi=300)
plt.show()

# Weak Scaling - Efficiency
plt.figure(figsize=(10, 6))
plt.plot(weak_cores, weak_efficiency, marker='d', linewidth=2, markersize=8, color='orange')
plt.axhline(y=100, color='red', linestyle='--', alpha=0.5, label='100% Efficiency')
plt.xlabel('Number of Cores', fontsize=12)
plt.ylabel('Efficiency (%)', fontsize=12)
plt.title('Weak Scaling: Efficiency vs Cores', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.xticks(weak_cores)
for i, (c, e) in enumerate(zip(weak_cores, weak_efficiency)):
    plt.text(c, e + 1.5, f'{e:.1f}%', ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('weak_efficiency_vs_cores.png', dpi=300)
plt.show()

print("\nIndividual plots saved:")
print("- strong_time_vs_cores.png")
print("- strong_speedup_vs_cores.png")
print("- weak_time_vs_cores.png")
print("- weak_efficiency_vs_cores.png")
