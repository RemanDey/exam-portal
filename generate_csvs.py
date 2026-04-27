import numpy as np
import pandas as pd
import os

np.random.seed(42)

script_dir = os.path.dirname(os.path.abspath(__file__))

print("Generating CSV files for Hypothesis Testing Exam...\n")


print("1. Generating api_response.csv...")
api_response_times = np.random.normal(loc=210, scale=15, size=250) 
api_df = pd.DataFrame({'Response Time ms': api_response_times})
api_csv_path = os.path.join(script_dir, 'api_response.csv')
api_df.to_csv(api_csv_path, index=False)
print(f"   ✓ Created {api_csv_path}")
print(f"   - 250 samples, mean={api_response_times.mean():.2f}ms, std={api_response_times.std():.2f}ms\n")

print("2. Generating cluster_latency.csv...")
alpha_latency = np.random.normal(loc=45, scale=8, size=30)   
beta_latency = np.random.normal(loc=50, scale=12, size=35)   
cluster_df = pd.DataFrame({
    'Alpha Latency ms': alpha_latency,
    'Beta Latency ms': np.concatenate([beta_latency, [np.nan]*(30-len(beta_latency))])
    if len(beta_latency) < 30 else beta_latency[:30]
})

max_len = max(len(alpha_latency), len(beta_latency))
cluster_df = pd.DataFrame({
    'Alpha Latency ms': np.concatenate([alpha_latency, [np.nan]*(max_len-len(alpha_latency))]),
    'Beta Latency ms': np.concatenate([beta_latency, [np.nan]*(max_len-len(beta_latency))])
})
cluster_csv_path = os.path.join(script_dir, 'cluster_latency.csv')
cluster_df.to_csv(cluster_csv_path, index=False)
print(f"   ✓ Created {cluster_csv_path}")
print(f"   - Alpha: mean={alpha_latency.mean():.2f}ms, std={alpha_latency.std():.2f}ms")
print(f"   - Beta: mean={beta_latency.mean():.2f}ms, std={beta_latency.std():.2f}ms\n")



print("3. Generating network_packets.csv...")
total_packets = 500
packet_types = np.random.choice(
    ['HTTP', 'HTTPS', 'DNS', 'Other'],
    size=total_packets,
    p=[0.45, 0.33, 0.15, 0.07]  # Slightly different from expected
)
network_df = pd.DataFrame({'Packet Type': packet_types})
network_csv_path = os.path.join(script_dir, 'network_packets.csv')
network_df.to_csv(network_csv_path, index=False)
unique, counts = np.unique(packet_types, return_counts=True)
print(f"   ✓ Created {network_csv_path}")
print(f"   - Total packets: {total_packets}")
for ptype, count in zip(unique, counts):
    print(f"   - {ptype}: {count} ({count/total_packets*100:.1f}%)")
print()


print("4. Generating recovery_times.csv...")
standard_recovery = np.random.normal(loc=12, scale=2.5, size=40)  # Standard treatment
new_recovery = np.random.normal(loc=10.5, scale=2.2, size=40)     # New treatment (faster)

recovery_data = []
for days in standard_recovery:
    recovery_data.append({'Recovery Days': days, 'Treatment': 'Standard'})
for days in new_recovery:
    recovery_data.append({'Recovery Days': days, 'Treatment': 'New'})

recovery_df = pd.DataFrame(recovery_data)
recovery_csv_path = os.path.join(script_dir, 'recovery_times.csv')
recovery_df.to_csv(recovery_csv_path, index=False)
print(f"   ✓ Created {recovery_csv_path}")
print(f"   - Standard: {len(standard_recovery)} samples, mean={standard_recovery.mean():.2f} days, std={standard_recovery.std():.2f}")
print(f"   - New: {len(new_recovery)} samples, mean={new_recovery.mean():.2f} days, std={new_recovery.std():.2f}")
print(f"   - Total rows: {len(recovery_df)}\n")


print("5. Generating battery_life.csv...")
supplier_x = np.random.normal(loc=240, scale=18, size=50)  
supplier_y = np.random.normal(loc=255, scale=20, size=50)  
supplier_z = np.random.normal(loc=245, scale=22, size=50)  
battery_data = []
for hours in supplier_x:
    battery_data.append({'Supplier': 'X', 'Battery Life Hours': hours})
for hours in supplier_y:
    battery_data.append({'Supplier': 'Y', 'Battery Life Hours': hours})
for hours in supplier_z:
    battery_data.append({'Supplier': 'Z', 'Battery Life Hours': hours})

battery_df = pd.DataFrame(battery_data)
battery_csv_path = os.path.join(script_dir, 'battery_life.csv')
battery_df.to_csv(battery_csv_path, index=False)
print(f"   ✓ Created {battery_csv_path}")
print(f"   - Supplier X: {len(supplier_x)} samples, mean={supplier_x.mean():.2f} hours, std={supplier_x.std():.2f}")
print(f"   - Supplier Y: {len(supplier_y)} samples, mean={supplier_y.mean():.2f} hours, std={supplier_y.std():.2f}")
print(f"   - Supplier Z: {len(supplier_z)} samples, mean={supplier_z.mean():.2f} hours, std={supplier_z.std():.2f}")
print(f"   - Total rows: {len(battery_df)}\n")


print("=" * 70)
print("✓ All CSV files generated successfully!")
print("=" * 70)
print("\nGenerated files:")
print("  1. api_response.csv         (Q1 - One-Sample Z/T Test)")
print("  2. cluster_latency.csv      (Q2 - Two-Sample Welch T-Test)")
print("  3. network_packets.csv      (Q3 - Chi-Square Goodness-of-Fit)")
print("  4. recovery_times.csv       (Q4 - Bootstrap Permutation Test)")
print("  5. battery_life.csv         (Q6 - One-Way ANOVA)")
print("\nLocation:", script_dir)
