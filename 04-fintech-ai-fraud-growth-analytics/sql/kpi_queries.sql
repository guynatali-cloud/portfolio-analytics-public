-- 1. Fraud rate by transaction category
SELECT
    Category,
    COUNT(*) AS total_transactions,
    SUM(FraudIndicator) AS fraud_count,
    ROUND(SUM(FraudIndicator) * 1.0 / COUNT(*), 4) AS fraud_rate,
    ROUND(AVG(Amount), 2) AS avg_amount,
    ROUND(AVG(AnomalyScore), 4) AS avg_anomaly_score
FROM fintech_transactions
GROUP BY Category
ORDER BY fraud_rate DESC;

-- 2. Risk level distribution and fraud capture
SELECT
    ai_risk_level,
    COUNT(*) AS transactions,
    SUM(FraudIndicator) AS fraud_count,
    ROUND(SUM(FraudIndicator) * 1.0 / COUNT(*), 4) AS fraud_rate,
    ROUND(AVG(ai_risk_score), 4) AS avg_risk_score,
    ROUND(SUM(Amount), 2) AS total_amount
FROM fintech_transactions
GROUP BY ai_risk_level
ORDER BY avg_risk_score DESC;

-- 3. AI intervention recommendations with fraud accuracy
SELECT
    ai_intervention,
    COUNT(*) AS transactions,
    SUM(FraudIndicator) AS actual_fraud,
    ROUND(SUM(FraudIndicator) * 1.0 / COUNT(*), 4) AS fraud_rate,
    ROUND(AVG(AnomalyScore), 4) AS avg_anomaly
FROM fintech_transactions
GROUP BY ai_intervention
ORDER BY fraud_rate DESC;

-- 4. Fraud patterns by hour of day
SELECT
    Hour,
    COUNT(*) AS transactions,
    SUM(FraudIndicator) AS fraud_count,
    ROUND(SUM(FraudIndicator) * 1.0 / COUNT(*), 4) AS fraud_rate
FROM fintech_transactions
GROUP BY Hour
ORDER BY fraud_rate DESC
LIMIT 10;

-- 5. High-risk customers with multiple fraud indicators
SELECT
    CustomerID,
    Name,
    Age,
    AccountBalance,
    COUNT(*) AS total_transactions,
    SUM(FraudIndicator) AS fraud_count,
    ROUND(AVG(ai_risk_score), 4) AS avg_risk_score,
    SuspiciousFlag
FROM fintech_transactions
WHERE ai_risk_level = 'High Risk'
GROUP BY CustomerID, Name, Age, AccountBalance, SuspiciousFlag
ORDER BY fraud_count DESC, avg_risk_score DESC
LIMIT 20;

-- 6. Merchant risk analysis
SELECT
    MerchantName,
    Location,
    COUNT(*) AS transactions,
    SUM(FraudIndicator) AS fraud_count,
    ROUND(SUM(FraudIndicator) * 1.0 / COUNT(*), 4) AS fraud_rate,
    ROUND(AVG(AnomalyScore), 4) AS avg_anomaly
FROM fintech_transactions
GROUP BY MerchantName, Location
HAVING SUM(FraudIndicator) > 0
ORDER BY fraud_rate DESC;

-- 7. Monthly fraud trend
SELECT
    Month,
    COUNT(*) AS transactions,
    SUM(FraudIndicator) AS fraud_count,
    ROUND(SUM(FraudIndicator) * 1.0 / COUNT(*), 4) AS fraud_rate,
    ROUND(SUM(Amount), 2) AS total_amount
FROM fintech_transactions
GROUP BY Month
ORDER BY Month;
