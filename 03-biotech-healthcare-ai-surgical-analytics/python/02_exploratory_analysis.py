import pandas as pd

PATH = "../data/cleaned/surgical_operations_cleaned.csv"
df = pd.read_csv(PATH)

# Department summary
dept = df.groupby('department').agg(
    total_surgeries=('surgery_id', 'count'),
    avg_duration=('actual_duration_min', 'mean'),
    avg_delay=('delay_minutes', 'mean'),
    complication_rate=('complication_flag', 'mean'),
    readmission_rate=('readmission_30day', 'mean'),
    avg_satisfaction=('patient_satisfaction_score', 'mean'),
    avg_cost=('estimated_cost_usd', 'mean')
).round(2).reset_index()
print("=== Department KPIs ===")
print(dept.sort_values('avg_delay', ascending=False))

# AI vs Standard
ai_comp = df.groupby('dashboard_type').agg(
    total_surgeries=('surgery_id', 'count'),
    avg_delay=('delay_minutes', 'mean'),
    complication_rate=('complication_flag', 'mean'),
    readmission_rate=('readmission_30day', 'mean'),
    avg_satisfaction=('patient_satisfaction_score', 'mean')
).round(2).reset_index()
print("\n=== AI vs Standard ===")
print(ai_comp)
