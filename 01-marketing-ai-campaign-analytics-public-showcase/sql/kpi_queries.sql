-- 1. Platform KPI summary
SELECT
    platform,
    SUM(impressions) AS impressions,
    SUM(clicks) AS clicks,
    ROUND(SUM(clicks) * 1.0 / NULLIF(SUM(impressions),0), 4) AS ctr,
    ROUND(SUM(ad_spend), 2) AS ad_spend,
    ROUND(SUM(ad_spend) * 1.0 / NULLIF(SUM(clicks),0), 2) AS cpc,
    SUM(conversions) AS conversions,
    ROUND(SUM(conversions) * 1.0 / NULLIF(SUM(clicks),0), 4) AS conversion_rate,
    ROUND(SUM(ad_spend) * 1.0 / NULLIF(SUM(conversions),0), 2) AS cpa,
    ROUND(SUM(revenue), 2) AS revenue,
    ROUND(SUM(revenue) * 1.0 / NULLIF(SUM(ad_spend),0), 2) AS roas,
    ROUND(SUM(revenue) - SUM(ad_spend), 2) AS profit
FROM marketing_campaigns
GROUP BY platform
ORDER BY roas DESC;

-- 2. Campaign type performance
SELECT
    campaign_type,
    SUM(impressions) AS impressions,
    SUM(clicks) AS clicks,
    ROUND(SUM(clicks) * 1.0 / NULLIF(SUM(impressions),0), 4) AS ctr,
    ROUND(SUM(ad_spend), 2) AS ad_spend,
    SUM(conversions) AS conversions,
    ROUND(SUM(conversions) * 1.0 / NULLIF(SUM(clicks),0), 4) AS conversion_rate,
    ROUND(SUM(revenue), 2) AS revenue,
    ROUND(SUM(revenue) * 1.0 / NULLIF(SUM(ad_spend),0), 2) AS roas
FROM marketing_campaigns
GROUP BY campaign_type
ORDER BY conversion_rate DESC;

-- 3. Monthly trend
SELECT
    DATE_TRUNC('month', campaign_date) AS campaign_month,
    platform,
    ROUND(SUM(ad_spend), 2) AS ad_spend,
    ROUND(SUM(revenue), 2) AS revenue,
    SUM(conversions) AS conversions
FROM marketing_campaigns
GROUP BY 1, 2
ORDER BY 1, 2;
