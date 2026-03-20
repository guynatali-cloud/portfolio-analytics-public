import pandas as pd

df = pd.read_csv('../data/cleaned/ecommerce_cleaned.csv')

tier_eval = df.groupby('ai_recommendation').agg(
    customers=('Customer ID','count'),
    avg_spend=('Total Spend','mean'),
    avg_ltv=('ltv_proxy','mean'),
    avg_items=('Items Purchased','mean'),
    satisfaction_rate=('Satisfaction Level', lambda x: (x=='Satisfied').mean()),
    active_rate=('is_active','mean'),
    avg_score=('ai_personalization_score','mean')
).round(4).reset_index()

print("=== AI Personalization Tier Evaluation ===")
print(tier_eval)

vip = df[df['ai_recommendation']=='VIP — personalize heavily']
low = df[df['ai_recommendation']=='Low priority']
print(f"\nVIP avg LTV: ${vip['ltv_proxy'].mean():.2f}")
print(f"Low priority avg LTV: ${low['ltv_proxy'].mean():.2f}")
print(f"LTV uplift: {((vip['ltv_proxy'].mean()/low['ltv_proxy'].mean())-1)*100:.1f}%")

tier_eval.to_csv('../outputs/ai_tier_kpis.csv', index=False)
