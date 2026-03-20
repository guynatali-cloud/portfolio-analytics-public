-- 1. Membership performance comparison
SELECT membership_type, COUNT(*) AS customers,
    ROUND(AVG(total_spend),2) AS avg_spend, ROUND(AVG(ltv_proxy),2) AS avg_ltv,
    ROUND(AVG(items_purchased),1) AS avg_items, ROUND(AVG(average_rating),2) AS avg_rating,
    ROUND(AVG(days_since_last_purchase),0) AS avg_recency
FROM ecommerce_customers GROUP BY membership_type ORDER BY avg_spend DESC;

-- 2. AI recommendation tier analysis
SELECT ai_recommendation, COUNT(*) AS customers,
    ROUND(AVG(total_spend),2) AS avg_spend, ROUND(AVG(ltv_proxy),2) AS avg_ltv,
    ROUND(AVG(ai_personalization_score),4) AS avg_score,
    ROUND(SUM(CASE WHEN satisfaction_level='Satisfied' THEN 1 ELSE 0 END)*1.0/COUNT(*),4) AS satisfaction_rate
FROM ecommerce_customers GROUP BY ai_recommendation ORDER BY avg_ltv DESC;

-- 3. Satisfaction vs spending
SELECT satisfaction_level, COUNT(*) AS customers,
    ROUND(AVG(total_spend),2) AS avg_spend, ROUND(AVG(ltv_proxy),2) AS avg_ltv,
    ROUND(AVG(items_purchased),1) AS avg_items
FROM ecommerce_customers GROUP BY satisfaction_level ORDER BY avg_spend DESC;

-- 4. City performance ranking
SELECT city, COUNT(*) AS customers, ROUND(AVG(total_spend),2) AS avg_spend,
    ROUND(AVG(ltv_proxy),2) AS avg_ltv
FROM ecommerce_customers GROUP BY city ORDER BY avg_spend DESC LIMIT 10;

-- 5. Discount impact on spend and satisfaction
SELECT discount_applied, COUNT(*) AS customers,
    ROUND(AVG(total_spend),2) AS avg_spend, ROUND(AVG(ltv_proxy),2) AS avg_ltv,
    ROUND(SUM(CASE WHEN satisfaction_level='Satisfied' THEN 1 ELSE 0 END)*1.0/COUNT(*),4) AS satisfaction_rate
FROM ecommerce_customers GROUP BY discount_applied;

-- 6. Age group segmentation
SELECT CASE WHEN age<25 THEN '18-24' WHEN age<35 THEN '25-34' WHEN age<45 THEN '35-44' ELSE '45+' END AS age_group,
    COUNT(*) AS customers, ROUND(AVG(total_spend),2) AS avg_spend, ROUND(AVG(ltv_proxy),2) AS avg_ltv
FROM ecommerce_customers GROUP BY age_group ORDER BY avg_spend DESC;

-- 7. VIP customers — high LTV + high personalization score
SELECT customer_id, city, membership_type, total_spend, ltv_proxy,
    ai_personalization_score, ai_recommendation, satisfaction_level
FROM ecommerce_customers WHERE ai_recommendation = 'VIP — personalize heavily'
ORDER BY ltv_proxy DESC LIMIT 20;
