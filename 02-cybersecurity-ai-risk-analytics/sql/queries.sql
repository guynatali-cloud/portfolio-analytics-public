-- 01_overview.sql
SELECT COUNT(*) AS total_vulnerabilities
FROM kev_cleaned;

-- 02_vendor_risk.sql
SELECT vendorProject,
       COUNT(*) AS vulnerability_count,
       SUM(CASE WHEN LOWER(knownRansomwareCampaignUse) = 'known' THEN 1 ELSE 0 END) AS ransomware_linked_count
FROM kev_cleaned
GROUP BY vendorProject
ORDER BY vulnerability_count DESC
LIMIT 20;

-- 03_monthly_trend.sql
SELECT strftime('%Y-%m', dateAdded) AS month,
       COUNT(*) AS vulnerabilities_added
FROM kev_cleaned
GROUP BY month
ORDER BY month;

-- 04_days_to_due.sql
SELECT cveID,
       vendorProject,
       product,
       dateAdded,
       dueDate,
       CAST(julianday(dueDate) - julianday(dateAdded) AS INTEGER) AS days_to_due
FROM kev_cleaned
ORDER BY days_to_due ASC;

-- 05_cwe_analysis.sql
SELECT cwes,
       COUNT(*) AS count_cves
FROM kev_cleaned
GROUP BY cwes
ORDER BY count_cves DESC
LIMIT 20;
