import pandas as pd
import numpy as np

PATH = "../data/cleaned/surgical_operations_cleaned.csv"
df = pd.read_csv(PATH)

# AI impact by department
impact = df.groupby(['department', 'dashboard_type']).agg(
    avg_delay=('delay_minutes', 'mean'),
    complication_rate=('complication_flag', 'mean'),
    avg_satisfaction=('patient_satisfaction_score', 'mean'),
    avg_duration=('actual_duration_min', 'mean')
).round(2).reset_index()

pivot = impact.pivot(index='department', columns='dashboard_type', values='avg_delay')
pivot['delay_reduction_pct'] = ((pivot['Standard'] - pivot['AI-Assisted']) / pivot['Standard'] * 100).round(1)
print("=== AI Delay Reduction by Department ===")
print(pivot.sort_values('delay_reduction_pct', ascending=False))

# Efficiency scoring for resource allocation
dept_scores = df.groupby('department').agg(
    avg_delay=('delay_minutes', 'mean'),
    complication_rate=('complication_flag', 'mean'),
    avg_utilization=('or_utilization_rate', 'mean'),
    avg_satisfaction=('patient_satisfaction_score', 'mean')
).reset_index()

dept_scores['priority_score'] = (
    dept_scores['avg_delay'].rank(pct=True) * 0.30 +
    dept_scores['complication_rate'].rank(pct=True) * 0.30 +
    (1 - dept_scores['avg_utilization'].rank(pct=True)) * 0.20 +
    (1 - dept_scores['avg_satisfaction'].rank(pct=True)) * 0.20
).round(3)

dept_scores['ai_recommendation'] = pd.cut(
    dept_scores['priority_score'],
    bins=[-1, 0.33, 0.66, 2],
    labels=['Low Priority', 'Monitor', 'High Priority - Expand AI']
)
print("\n=== Department AI Priority Scoring ===")
print(dept_scores[['department', 'priority_score', 'ai_recommendation']].sort_values('priority_score', ascending=False))
