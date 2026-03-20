import pandas as pd

df = pd.read_csv('../data/cleaned/ecommerce_cleaned.csv')

print("=== Membership KPIs ===")
print(df.groupby('Membership Type').agg(
    customers=('Customer ID','count'), avg_spend=('Total Spend','mean'),
    avg_ltv=('ltv_proxy','mean'), avg_rating=('Average Rating','mean')
).round(2))

print("\n=== AI Tier KPIs ===")
print(df.groupby('ai_recommendation').agg(
    customers=('Customer ID','count'), avg_spend=('Total Spend','mean'),
    avg_ltv=('ltv_proxy','mean')
).round(2))

print("\n=== Satisfaction Analysis ===")
print(df.groupby('Satisfaction Level').agg(
    customers=('Customer ID','count'), avg_spend=('Total Spend','mean')
).round(2))
