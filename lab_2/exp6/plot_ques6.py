import matplotlib.pyplot as plt
import numpy as np

# Results from both implementations
impl1_names = ['False Sharing\n(Struct)', 'Padded\n(Struct)']
impl1_times = [1.229, 0.381]

impl2_names = ['Unpadded\n(Array)', 'Padded\n(Array)']
impl2_times = [1.698, 0.332]

# Combined data
all_configs = ['Struct\nFalse Sharing', 'Struct\nPadded', 'Array\nUnpadded', 'Array\nPadded']
all_times = [1.229, 0.381, 1.698, 0.332]

# Calculate speedups
speedup1 = impl1_times[0] / impl1_times[1]  # 3.23x
speedup2 = impl2_times[0] / impl2_times[1]  # 5.11x

# Create comprehensive visualization
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# 1. Implementation 1 Comparison
colors1 = ['red', 'green']
bars1 = ax1.bar(impl1_names, impl1_times, color=colors1, edgecolor='black', linewidth=1.5)
ax1.set_ylabel('Execution Time (seconds)', fontsize=11)
ax1.set_title('Implementation 1: Struct-based (100M iterations)', fontsize=12, fontweight='bold')
ax1.grid(True, alpha=0.3, axis='y')

for bar, time in zip(bars1, impl1_times):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'{time:.3f}s', ha='center', va='bottom', fontsize=10, fontweight='bold')
ax1.text(0.5, max(impl1_times)*0.8, f'{speedup1:.2f}x faster', 
         ha='center', fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat'))

# 2. Implementation 2 Comparison
colors2 = ['red', 'green']
bars2 = ax2.bar(impl2_names, impl2_times, color=colors2, edgecolor='black', linewidth=1.5)
ax2.set_ylabel('Execution Time (seconds)', fontsize=11)
ax2.set_title('Implementation 2: Array-based (100M iterations)', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3, axis='y')

for bar, time in zip(bars2, impl2_times):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'{time:.3f}s', ha='center', va='bottom', fontsize=10, fontweight='bold')
ax2.text(0.5, max(impl2_times)*0.8, f'{speedup2:.2f}x faster', 
         ha='center', fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat'))

# 3. All Configurations Comparison
colors_all = ['red', 'green', 'red', 'green']
bars_all = ax3.bar(all_configs, all_times, color=colors_all, alpha=0.7, edgecolor='black', linewidth=1.5)
ax3.set_ylabel('Execution Time (seconds)', fontsize=11)
ax3.set_title('False Sharing Impact: All Implementations', fontsize=12, fontweight='bold')
ax3.grid(True, alpha=0.3, axis='y')
ax3.axhline(y=0.4, color='gray', linestyle='--', alpha=0.5, label='Optimal threshold')

for bar, time in zip(bars_all, all_times):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height,
            f'{time:.2f}s', ha='center', va='bottom', fontsize=9, fontweight='bold')

# 4. Speedup Comparison
implementations = ['Struct\nImplementation', 'Array\nImplementation']
speedups = [speedup1, speedup2]
colors_speedup = ['orange', 'purple']

bars_speedup = ax4.bar(implementations, speedups, color=colors_speedup, edgecolor='black', linewidth=1.5)
ax4.set_ylabel('Speedup Factor', fontsize=11)
ax4.set_title('Speedup: Padded vs Unpadded', fontsize=12, fontweight='bold')
ax4.grid(True, alpha=0.3, axis='y')
ax4.axhline(y=1, color='red', linestyle='--', linewidth=1, label='No improvement')

for bar, speedup in zip(bars_speedup, speedups):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
            f'{speedup:.2f}x', ha='center', va='bottom', fontsize=12, fontweight='bold')

ax4.legend()

plt.tight_layout()
plt.savefig('false_sharing_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("False sharing analysis plot saved as 'false_sharing_analysis.png'")

# Individual detailed plots
# Overhead comparison
plt.figure(figsize=(10, 6))
overhead = ['Struct', 'Array']
overhead_pct = [(impl1_times[0] - impl1_times[1]) / impl1_times[1] * 100,
                (impl2_times[0] - impl2_times[1]) / impl2_times[1] * 100]

bars = plt.bar(overhead, overhead_pct, color=['coral', 'tomato'], edgecolor='black', linewidth=2)
plt.ylabel('Overhead (%)', fontsize=12)
plt.title('False Sharing Overhead Percentage', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')

for bar, pct in zip(bars, overhead_pct):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{pct:.1f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('false_sharing_overhead.png', dpi=300, bbox_inches='tight')
plt.show()

# Time savings visualization
plt.figure(figsize=(10, 6))
time_saved1 = impl1_times[0] - impl1_times[1]
time_saved2 = impl2_times[0] - impl2_times[1]

labels = ['Struct Implementation', 'Array Implementation']
saved = [time_saved1, time_saved2]
colors = ['lightgreen', 'mediumseagreen']

bars = plt.bar(labels, saved, color=colors, edgecolor='black', linewidth=2)
plt.ylabel('Time Saved (seconds)', fontsize=12)
plt.title('Performance Improvement with Padding', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')

for bar, save in zip(bars, saved):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{save:.3f}s\nsaved', ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('time_savings.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nAll plots saved:")
print("- false_sharing_analysis.png (comprehensive view)")
print("- false_sharing_overhead.png (overhead percentage)")
print("- time_savings.png (time saved with padding)")
