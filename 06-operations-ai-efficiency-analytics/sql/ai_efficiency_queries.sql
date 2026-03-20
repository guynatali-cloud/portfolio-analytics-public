-- AI bottleneck detection: which routes have worst efficiency?
WITH route_performance AS (
    SELECT origin_port, destination_port, carrier,
        COUNT(*) AS shipments,
        ROUND(SUM(is_late)*1.0/COUNT(*),4) AS late_rate,
        ROUND(AVG(tpt),1) AS avg_transit,
        ROUND(AVG(ai_efficiency_score),4) AS avg_efficiency
    FROM operations_shipments GROUP BY origin_port, destination_port, carrier
    HAVING COUNT(*) >= 10
)
SELECT * FROM route_performance WHERE late_rate > 0.05 ORDER BY late_rate DESC LIMIT 20;
