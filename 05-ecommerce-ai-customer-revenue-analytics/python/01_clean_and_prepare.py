import pandas as pd
import numpy as np

df = pd.read_csv('../data/raw/E-commerce_Customer_Behavior_-_Sheet1.csv')
df.columns = df.columns.str.strip()

df['spend_per_item'] = (df['Total Spend'] / df['Items Purchased']).round(2)
df['is_high_spender'] = (df['Total Spend'] > df['Total Spend'].median()).astype(int)
df['is_active'] = (df['Days Since Last Purchase'] < 30).astype(int)
df['discount_flag'] = df['Discount Applied'].map({'TRUE':1,'FALSE':0,True:1,False:0}).fillna(0).astype(int)

df['recency_score'] = pd.qcut(df['Days Since Last Purchase'], 3, labels=['Recent','Mid','Dormant'])
df['frequency_score'] = pd.qcut(df['Items Purchased'], 3, labels=['Low','Mid','High'], duplicates='drop')
df['monetary_score'] = pd.qcut(df['Total Spend'], 3, labels=['Low','Mid','High'])

df['ai_personalization_score'] = (
    df['Total Spend'].rank(pct=True) * 0.30
    + df['Items Purchased'].rank(pct=True) * 0.25
    + df['Average Rating'].rank(pct=True) * 0.20
    + (1 - df['Days Since Last Purchase'].rank(pct=True)) * 0.15
    + df['discount_flag'] * 0.10
).round(4)

df['ai_recommendation'] = pd.cut(df['ai_personalization_score'], bins=[-1,0.33,0.66,2],
    labels=['Low priority','Nurture','VIP — personalize heavily'])

df['ltv_proxy'] = (df['Total Spend'] * (df['Items Purchased']/df['Items Purchased'].mean()) * (df['Average Rating']/5)).round(2)

df.to_csv('../data/cleaned/ecommerce_cleaned.csv', index=False)
print(f"Saved {len(df)} rows")
