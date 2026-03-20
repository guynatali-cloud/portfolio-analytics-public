import pandas as pd

df = pd.read_csv('../data/cleaned/operations_cleaned.csv')

tier_eval = df.groupby('ai_recommendation').agg(
    shipments=('Order ID','count'), late_rate=('is_late','mean'),
    avg_tpt=('TPT','mean'), avg_quantity=('Unit quantity','mean'),
    avg_score=('ai_efficiency_score','mean')
).round(4).reset_index()

print("=== AI Efficiency Tier Evaluation ===")
print(tier_eval)

high = df[df['ai_recommendation']=='High efficiency']
low = df[df['ai_recommendation']=='Needs improvement']
print(f"\nHigh efficiency late rate: {high['is_late'].mean():.1%}")
print(f"Needs improvement late rate: {low['is_late'].mean():.1%}")

tier_eval.to_csv('../outputs/ai_efficiency_kpis.csv', index=False)
