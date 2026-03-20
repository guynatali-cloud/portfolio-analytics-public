import pandas as pd
import numpy as np

# Load all raw CSV files
transactions = pd.read_csv('../data/raw/transaction_records.csv')
metadata = pd.read_csv('../data/raw/transaction_metadata.csv')
customers = pd.read_csv('../data/raw/customer_data.csv')
accounts = pd.read_csv('../data/raw/account_activity.csv')
fraud = pd.read_csv('../data/raw/fraud_indicators.csv')
suspicious = pd.read_csv('../data/raw/suspicious_activity.csv')
amounts = pd.read_csv('../data/raw/amount_data.csv')
anomaly = pd.read_csv('../data/raw/anomaly_scores.csv')
merchants = pd.read_csv('../data/raw/merchant_data.csv')
categories = pd.read_csv('../data/raw/transaction_category_labels.csv')

# Merge into master dataset
df = transactions.merge(metadata, on='TransactionID')
df = df.merge(fraud, on='TransactionID')
df = df.merge(amounts, on='TransactionID')
df = df.merge(anomaly, on='TransactionID')
df = df.merge(categories, on='TransactionID')
df = df.merge(customers, on='CustomerID')
df = df.merge(accounts, on='CustomerID')
df = df.merge(suspicious, on='CustomerID')
df = df.merge(merchants, on='MerchantID')

# Clean and enrich
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Month'] = df['Timestamp'].dt.to_period('M').astype(str)
df['DayOfWeek'] = df['Timestamp'].dt.day_name()
df['Hour'] = df['Timestamp'].dt.hour
df['Amount'] = df['Amount'].round(2)
df['TransactionAmount'] = df['TransactionAmount'].round(2)
df['AnomalyScore'] = df['AnomalyScore'].round(4)
df['AccountBalance'] = df['AccountBalance'].round(2)

# AI risk scoring model
df['ai_risk_score'] = (
    df['AnomalyScore'].rank(pct=True) * 0.40
    + df['FraudIndicator'] * 0.30
    + df['SuspiciousFlag'] * 0.20
    + (1 - df['AccountBalance'].rank(pct=True)) * 0.10
)
df['ai_risk_score'] = df['ai_risk_score'].round(4)

df['ai_risk_level'] = pd.cut(df['ai_risk_score'], bins=[-1, 0.3, 0.6, 2],
                              labels=['Low Risk', 'Medium Risk', 'High Risk'])

df['ai_intervention'] = pd.cut(df['ai_risk_score'], bins=[-1, 0.3, 0.6, 2],
                                labels=['No action', 'Monitor', 'Immediate review'])

df.to_csv('../data/cleaned/fintech_fraud_cleaned.csv', index=False)
print(f"Saved {len(df)} rows to cleaned dataset")
