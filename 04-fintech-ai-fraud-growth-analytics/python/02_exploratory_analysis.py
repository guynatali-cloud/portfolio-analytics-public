import pandas as pd

df = pd.read_csv('../data/cleaned/fintech_fraud_cleaned.csv')

# Category-level fraud analysis
cat_summary = df.groupby('Category').agg(
    transactions=('TransactionID', 'count'),
    total_amount=('Amount', 'sum'),
    avg_amount=('Amount', 'mean'),
    fraud_count=('FraudIndicator', 'sum'),
    fraud_rate=('FraudIndicator', 'mean'),
    avg_anomaly=('AnomalyScore', 'mean'),
    avg_risk=('ai_risk_score', 'mean')
).round(4).reset_index()

print("=== Category Fraud Summary ===")
print(cat_summary.sort_values('fraud_rate', ascending=False))

# Risk level analysis
risk_summary = df.groupby('ai_risk_level').agg(
    transactions=('TransactionID', 'count'),
    fraud_count=('FraudIndicator', 'sum'),
    fraud_rate=('FraudIndicator', 'mean'),
    avg_amount=('Amount', 'mean')
).round(4).reset_index()

print("\n=== Risk Level Summary ===")
print(risk_summary)

# Hourly fraud patterns
hour_summary = df.groupby('Hour').agg(
    transactions=('TransactionID', 'count'),
    fraud_count=('FraudIndicator', 'sum'),
    fraud_rate=('FraudIndicator', 'mean')
).round(4).reset_index()

print("\n=== Top Fraud Hours ===")
print(hour_summary.sort_values('fraud_rate', ascending=False).head(5))
