import pandas as pd
import numpy as np

df = pd.read_excel('../data/raw/Supply_chain_logisitcs_problem.xlsx')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['month'] = df['Order Date'].dt.to_period('M').astype(str)
df['day_of_week'] = df['Order Date'].dt.day_name()
df['is_late'] = (df['Ship Late Day count'] > 0).astype(int)
df['is_early'] = (df['Ship ahead day count'] > 0).astype(int)
df['on_time'] = ((df['Ship Late Day count']==0) & (df['Ship ahead day count']==0)).astype(int)
df['weight_per_unit'] = (df['Weight'] / df['Unit quantity']).round(4)
df['delay_severity'] = pd.cut(df['Ship Late Day count'], bins=[-1,0,2,5,999],
    labels=['On time','Minor delay','Moderate delay','Severe delay'])

df['ai_efficiency_score'] = (
    (1 - df['Ship Late Day count'].clip(0,10).rank(pct=True)) * 0.35
    + df['Ship ahead day count'].rank(pct=True) * 0.20
    + (1 - df['TPT'].rank(pct=True)) * 0.25
    + df['Unit quantity'].rank(pct=True) * 0.20
).round(4)

df['ai_recommendation'] = pd.cut(df['ai_efficiency_score'], bins=[-1,0.33,0.66,2],
    labels=['Needs improvement','Monitor','High efficiency'])

df.to_csv('../data/cleaned/operations_cleaned.csv', index=False)
print(f"Saved {len(df)} rows")
