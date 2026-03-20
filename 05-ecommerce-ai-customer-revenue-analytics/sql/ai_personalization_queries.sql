-- AI personalization effectiveness evaluation
WITH tier_summary AS (
    SELECT ai_recommendation,
        COUNT(*) AS customers,
        ROUND(AVG(total_spend),2) AS avg_spend,
        ROUND(AVG(ltv_proxy),2) AS avg_ltv,
        ROUND(AVG(items_purchased),1) AS avg_items,
        ROUND(SUM(CASE WHEN satisfaction_level='Satisfied' THEN 1 ELSE 0 END)*1.0/COUNT(*),4) AS satisfaction_rate,
        ROUND(SUM(CASE WHEN is_active=1 THEN 1 ELSE 0 END)*1.0/COUNT(*),4) AS active_rate
    FROM ecommerce_customers GROUP BY ai_recommendation
)
SELECT * FROM tier_summary ORDER BY avg_ltv DESC;
