import pandas as pd

df = pd.read_csv('../data/cleaned/operations_cleaned.csv')

print("=== Carrier KPIs ===")
print(df.groupby('Carrier').agg(shipments=('Order ID','count'),
    late_rate=('is_late','mean'), avg_tpt=('TPT','mean')).round(4))

print("\n=== Service Level KPIs ===")
print(df.groupby('Service Level').agg(shipments=('Order ID','count'),
    late_rate=('is_late','mean'), on_time=('on_time','mean')).round(4))

print("\n=== Delay Severity ===")
print(df['delay_severity'].value_counts())
