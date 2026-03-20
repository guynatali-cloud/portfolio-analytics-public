-- Suggested SQL schema for marketing campaign analysis
CREATE TABLE marketing_campaigns (
    campaign_date DATE,
    platform VARCHAR(50),
    campaign_type VARCHAR(50),
    industry VARCHAR(50),
    country VARCHAR(50),
    impressions INT,
    clicks INT,
    ctr DECIMAL(10,4),
    cpc DECIMAL(10,2),
    ad_spend DECIMAL(12,2),
    conversions INT,
    cpa DECIMAL(10,2),
    revenue DECIMAL(12,2),
    roas DECIMAL(10,2)
);
