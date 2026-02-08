import matplotlib.pyplot as plt
import numpy as np

# Experimental results
methods = ['Critical\nSection', 'Reduction']
times = [0.289, 0.004]
overhead_factor = 72.25

# Create figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 1. Execution Time Comparison
colors = ['red', 'green']
bars = ax1.bar(methods, times, color=colors, edgecolor='black', linewidth=1.5, width=0.6)
ax1.set_ylabel('Execution Time (seconds)', fontsize=12)
ax1.set_title('Synchronization Method Performance Comparison', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3, axis='y')

# Add value labels
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.3f}s', ha='center', va='bottom', fontsize=11, fontweight='bold')

# 2. Overhead Factor Visualization
ax2.barh(['Reduction', 'Critical Section'], [1, overhead_factor], 
         color=['green', 'red'], edgecolor='black', linewidth=1.5)
ax2.set_xlabel('Relative Performance (Reduction = 1x)', fontsize=12)
ax2.set_title('Overhead Factor: Critical Section vs Reduction', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3, axis='x')
ax2.text(overhead_factor/2, 1, f'{overhead_factor:.2f}x slower', 
         ha='center', va='center', fontsize=12, fontweight='bold', color='white')
ax2.text(0.5, 0, '1x (baseline)', ha='center', va='center', 
         fontsize=11, fontweight='bold', color='white')

plt.tight_layout()
plt.savefig('sync_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("Synchronization comparison plot saved as 'sync_comparison.png'")

# Individual plot - Execution Time
plt.figure(figsize=(10, 6))
bars = plt.bar(methods, times, color=colors, edgecolor='black', linewidth=2, width=0.5)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.title('Synchronization Overhead: Critical Section vs Reduction', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')

# Add value labels
for i, (bar, time) in enumerate(zip(bars, times)):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{time:.3f}s', ha='center', va='bottom', fontsize=13, fontweight='bold')
    
    # Add percentage label
    if i == 0:
        pct = 100
    else:
        pct = (times[1] / times[0]) * 100
    plt.text(bar.get_x() + bar.get_width()/2., height/2,
            f'{pct:.1f}%', ha='center', va='center', fontsize=11, color='white', fontweight='bold')

plt.tight_layout()
plt.savefig('execution_time_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# Overhead Factor Visualization
plt.figure(figsize=(10, 6))
categories = ['Reduction\n(Baseline)', 'Critical Section\n(72.25x slower)']
values = [1, overhead_factor]
colors_bar = ['green', 'red']

bars = plt.bar(categories, values, color=colors_bar, edgecolor='black', linewidth=2, width=0.6)
plt.ylabel('Relative Performance Factor', fontsize=12)
plt.title('Performance Overhead: How Many Times Slower?', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')
plt.axhline(y=1, color='gray', linestyle='--', linewidth=1, label='Baseline (Reduction)')

# Add value labels
for bar, val in zip(bars, values):
    height = bar.get_height()
    if val == 1:
        label = 'Baseline\n1.00x'
    else:
        label = f'{val:.2f}x\nslower'
    plt.text(bar.get_x() + bar.get_width()/2., height,
            label, ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.legend(fontsize=11)
plt.tight_layout()
plt.savefig('overhead_factor.png', dpi=300, bbox_inches='tight')
plt.show()

# Speedup visualization
plt.figure(figsize=(10, 6))
speedup = times[0] / times[1]
labels = ['Critical\nSection', 'Reduction']
speedup_values = [1, speedup]
colors_speedup = ['red', 'green']

bars = plt.bar(labels, speedup_values, color=colors_speedup, edgecolor='black', linewidth=2, width=0.5)
plt.ylabel('Speedup Factor', fontsize=12)
plt.title('Reduction Speedup vs Critical Section', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')

for bar, val in zip(bars, speedup_values):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{val:.2f}x', ha='center', va='bottom', fontsize=13, fontweight='bold')

plt.tight_layout()
plt.savefig('speedup_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nAll plots saved:")
print("- sync_comparison.png")
print("- execution_time_comparison.png")
print("- overhead_factor.png")
print("- speedup_comparison.png")
