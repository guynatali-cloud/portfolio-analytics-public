-- 1. Carrier performance comparison
SELECT carrier, COUNT(*) AS shipments,
    ROUND(AVG(tpt),1) AS avg_transit_time,
    ROUND(SUM(is_late)*1.0/COUNT(*),4) AS late_rate,
    ROUND(SUM(on_time)*1.0/COUNT(*),4) AS on_time_rate,
    ROUND(AVG(unit_quantity),0) AS avg_quantity,
    ROUND(AVG(ai_efficiency_score),4) AS avg_efficiency
FROM operations_shipments GROUP BY carrier ORDER BY late_rate DESC;

-- 2. Service level analysis
SELECT service_level, COUNT(*) AS shipments,
    ROUND(AVG(tpt),1) AS avg_transit_time,
    ROUND(SUM(is_late)*1.0/COUNT(*),4) AS late_rate,
    ROUND(SUM(on_time)*1.0/COUNT(*),4) AS on_time_rate
FROM operations_shipments GROUP BY service_level ORDER BY late_rate DESC;

-- 3. Delay severity breakdown
SELECT delay_severity, COUNT(*) AS shipments,
    ROUND(AVG(ship_late_days),1) AS avg_late_days,
    ROUND(AVG(tpt),1) AS avg_transit_time,
    ROUND(AVG(weight),1) AS avg_weight
FROM operations_shipments GROUP BY delay_severity ORDER BY avg_late_days DESC;

-- 4. Origin port bottleneck analysis
SELECT origin_port, COUNT(*) AS shipments,
    ROUND(SUM(is_late)*1.0/COUNT(*),4) AS late_rate,
    ROUND(AVG(tpt),1) AS avg_transit_time,
    ROUND(AVG(ai_efficiency_score),4) AS avg_efficiency
FROM operations_shipments GROUP BY origin_port ORDER BY late_rate DESC LIMIT 10;

-- 5. Plant throughput and efficiency
SELECT plant_code, COUNT(*) AS shipments,
    ROUND(SUM(unit_quantity),0) AS total_units,
    ROUND(AVG(tpt),1) AS avg_transit_time,
    ROUND(SUM(is_late)*1.0/COUNT(*),4) AS late_rate
FROM operations_shipments GROUP BY plant_code ORDER BY total_units DESC LIMIT 15;

-- 6. Monthly operational trend
SELECT month, COUNT(*) AS shipments,
    ROUND(SUM(is_late)*1.0/COUNT(*),4) AS late_rate,
    ROUND(SUM(unit_quantity),0) AS total_units,
    ROUND(AVG(ai_efficiency_score),4) AS avg_efficiency
FROM operations_shipments GROUP BY month ORDER BY month;

-- 7. AI efficiency tier evaluation
SELECT ai_recommendation, COUNT(*) AS shipments,
    ROUND(SUM(is_late)*1.0/COUNT(*),4) AS late_rate,
    ROUND(AVG(tpt),1) AS avg_transit_time,
    ROUND(AVG(unit_quantity),0) AS avg_quantity,
    ROUND(AVG(ai_efficiency_score),4) AS avg_score
FROM operations_shipments GROUP BY ai_recommendation ORDER BY avg_score DESC;
