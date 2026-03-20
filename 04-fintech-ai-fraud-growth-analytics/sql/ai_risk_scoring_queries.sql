-- AI-assisted risk scoring and intervention prioritization
WITH risk_scored AS (
    SELECT
        TransactionID,
        CustomerID,
        Amount,
        Category,
        FraudIndicator,
        AnomalyScore,
        SuspiciousFlag,
        AccountBalance,
        ai_risk_score,
        ai_risk_level,
        ai_intervention
    FROM fintech_transactions
),
intervention_summary AS (
    SELECT
        ai_intervention,
        COUNT(*) AS total_flagged,
        SUM(FraudIndicator) AS actual_fraud,
        ROUND(SUM(FraudIndicator) * 1.0 / NULLIF(COUNT(*), 0), 4) AS precision_rate,
        ROUND(AVG(Amount), 2) AS avg_flagged_amount
    FROM risk_scored
    GROUP BY ai_intervention
)
SELECT
    ai_intervention,
    total_flagged,
    actual_fraud,
    precision_rate,
    avg_flagged_amount
FROM intervention_summary
ORDER BY precision_rate DESC;
