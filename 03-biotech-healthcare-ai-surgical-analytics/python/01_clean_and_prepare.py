import pandas as pd
import numpy as np

RAW_PATH = "../data/raw/surgical_operations_raw.csv"
OUT_PATH = "../data/cleaned/surgical_operations_cleaned.csv"

df = pd.read_csv(RAW_PATH)
df['surgery_date'] = pd.to_datetime(df['surgery_date'])
df['month'] = df['surgery_date'].dt.to_period('M').astype(str)
df['year'] = df['surgery_date'].dt.year
df['day_of_week'] = df['surgery_date'].dt.day_name()
df['duration_variance_min'] = df['actual_duration_min'] - df['scheduled_duration_min']
df['duration_efficiency'] = np.where(df['scheduled_duration_min'] > 0, df['actual_duration_min'] / df['scheduled_duration_min'], 0)
df['cost_per_minute'] = np.where(df['actual_duration_min'] > 0, df['estimated_cost_usd'] / df['actual_duration_min'], 0)
df['delay_flag'] = (df['delay_minutes'] > 0).astype(int)
df['high_risk_flag'] = df['patient_risk_level'].isin(['High', 'Critical']).astype(int)

df['ai_efficiency_score'] = (
    (1 - df['duration_efficiency'].rank(pct=True)) * 0.25 +
    (1 - df['delay_minutes'].rank(pct=True)) * 0.25 +
    df['patient_satisfaction_score'].rank(pct=True) * 0.20 +
    (1 - df['complication_flag'].rank(pct=True)) * 0.15 +
    (1 - df['readmission_30day'].rank(pct=True)) * 0.15
)
df['ai_efficiency_score'] = df['ai_efficiency_score'].round(3)
df['ai_recommendation'] = pd.cut(df['ai_efficiency_score'], bins=[-1, 0.33, 0.66, 2], labels=['Needs Improvement', 'Monitor', 'Efficient'])

df.to_csv(OUT_PATH, index=False)
print(f"Saved cleaned file: {len(df)} rows, {len(df.columns)} columns")
