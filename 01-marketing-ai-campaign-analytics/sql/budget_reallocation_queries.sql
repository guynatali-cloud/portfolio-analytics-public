-- AI-assisted budget reallocation base query
WITH platform_summary AS (
    SELECT
        platform,
        SUM(ad_spend) AS current_budget,
        SUM(revenue) * 1.0 / NULLIF(SUM(ad_spend),0) AS roas,
        SUM(conversions) * 1.0 / NULLIF(SUM(clicks),0) AS conversion_rate,
        SUM(clicks) * 1.0 / NULLIF(SUM(impressions),0) AS ctr,
        SUM(ad_spend) * 1.0 / NULLIF(SUM(conversions),0) AS cpa
    FROM marketing_campaigns
    GROUP BY platform
),
scored AS (
    SELECT
        platform,
        current_budget,
        roas,
        conversion_rate,
        ctr,
        cpa,
        (roas * 0.60) + (conversion_rate * 100 * 0.30) + (ctr * 100 * 0.10) AS ai_score
    FROM platform_summary
)
SELECT
    platform,
    ROUND(current_budget, 2) AS current_budget,
    ROUND(ai_score, 2) AS ai_score
FROM scored
ORDER BY ai_score DESC;
