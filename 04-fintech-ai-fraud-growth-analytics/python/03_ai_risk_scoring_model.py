import pandas as pd

df = pd.read_csv('../data/cleaned/fintech_fraud_cleaned.csv')

# Evaluate AI risk scoring precision
intervention_eval = df.groupby('ai_intervention').agg(
    transactions=('TransactionID', 'count'),
    actual_fraud=('FraudIndicator', 'sum'),
    fraud_rate=('FraudIndicator', 'mean'),
    avg_risk=('ai_risk_score', 'mean'),
    avg_anomaly=('AnomalyScore', 'mean')
).round(4).reset_index()

print("=== AI Intervention Evaluation ===")
print(intervention_eval)

# Calculate precision of "Immediate review" tier
high_risk = df[df['ai_intervention'] == 'Immediate review']
if len(high_risk) > 0:
    precision = high_risk['FraudIndicator'].mean()
    print(f"\nImmediate Review precision: {precision:.1%}")
    print(f"Transactions flagged: {len(high_risk)}")
    print(f"Actual fraud caught: {high_risk['FraudIndicator'].sum()}")

# Overall fraud detection coverage
total_fraud = df['FraudIndicator'].sum()
fraud_in_high = df[df['ai_risk_level'] == 'High Risk']['FraudIndicator'].sum()
fraud_in_med = df[df['ai_risk_level'] == 'Medium Risk']['FraudIndicator'].sum()

print(f"\nTotal fraud: {total_fraud}")
print(f"Caught by High Risk: {fraud_in_high} ({fraud_in_high/total_fraud:.1%})")
print(f"Caught by Medium+High: {fraud_in_high+fraud_in_med} ({(fraud_in_high+fraud_in_med)/total_fraud:.1%})")

intervention_eval.to_csv('../outputs/intervention_summary.csv', index=False)
print("\nSaved intervention summary")
