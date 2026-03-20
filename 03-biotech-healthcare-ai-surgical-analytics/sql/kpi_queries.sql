-- 1. Department KPI Summary
SELECT
    department,
    COUNT(*) AS total_surgeries,
    ROUND(AVG(actual_duration_min), 1) AS avg_duration,
    ROUND(AVG(delay_minutes), 1) AS avg_delay,
    ROUND(AVG(complication_flag) * 100, 2) AS complication_pct,
    ROUND(AVG(readmission_30day) * 100, 2) AS readmission_pct,
    ROUND(AVG(patient_satisfaction_score), 1) AS avg_satisfaction,
    ROUND(AVG(estimated_cost_usd), 0) AS avg_cost
FROM surgical_operations
GROUP BY department
ORDER BY avg_delay DESC;

-- 2. AI-Assisted vs Standard Dashboard Comparison
SELECT
    dashboard_type,
    COUNT(*) AS total_surgeries,
    ROUND(AVG(delay_minutes), 1) AS avg_delay,
    ROUND(AVG(complication_flag) * 100, 2) AS complication_pct,
    ROUND(AVG(readmission_30day) * 100, 2) AS readmission_pct,
    ROUND(AVG(patient_satisfaction_score), 1) AS avg_satisfaction,
    ROUND(AVG(actual_duration_min), 1) AS avg_duration,
    ROUND(AVG(estimated_cost_usd), 0) AS avg_cost
FROM surgical_operations
GROUP BY dashboard_type;

-- 3. Surgeon Performance Ranking
SELECT
    surgeon,
    COUNT(*) AS total_surgeries,
    ROUND(AVG(actual_duration_min), 1) AS avg_duration,
    ROUND(AVG(delay_minutes), 1) AS avg_delay,
    ROUND(AVG(complication_flag) * 100, 2) AS complication_pct,
    ROUND(AVG(patient_satisfaction_score), 1) AS avg_satisfaction
FROM surgical_operations
GROUP BY surgeon
ORDER BY avg_satisfaction DESC;

-- 4. Monthly Trend — Delays and Complications
SELECT
    DATE_TRUNC('month', surgery_date) AS surgery_month,
    dashboard_type,
    COUNT(*) AS surgeries,
    ROUND(AVG(delay_minutes), 1) AS avg_delay,
    ROUND(AVG(complication_flag) * 100, 2) AS complication_pct,
    ROUND(AVG(patient_satisfaction_score), 1) AS avg_satisfaction
FROM surgical_operations
GROUP BY 1, 2
ORDER BY 1, 2;

-- 5. Operating Room Utilization
SELECT
    operating_room,
    COUNT(*) AS total_surgeries,
    ROUND(AVG(or_utilization_rate), 3) AS avg_utilization,
    ROUND(AVG(delay_minutes), 1) AS avg_delay,
    ROUND(AVG(actual_duration_min), 1) AS avg_duration
FROM surgical_operations
GROUP BY operating_room
ORDER BY avg_utilization DESC;

-- 6. High-Risk Patients: Outcome Analysis
SELECT
    patient_risk_level,
    COUNT(*) AS total,
    ROUND(AVG(complication_flag) * 100, 2) AS complication_pct,
    ROUND(AVG(readmission_30day) * 100, 2) AS readmission_pct,
    ROUND(AVG(patient_satisfaction_score), 1) AS avg_satisfaction,
    ROUND(AVG(delay_minutes), 1) AS avg_delay
FROM surgical_operations
GROUP BY patient_risk_level
ORDER BY complication_pct DESC;

-- 7. AI Impact on High-Risk Patients (Window Function)
SELECT
    patient_risk_level,
    dashboard_type,
    COUNT(*) AS surgeries,
    ROUND(AVG(complication_flag) * 100, 2) AS complication_pct,
    ROUND(AVG(delay_minutes), 1) AS avg_delay,
    ROUND(AVG(patient_satisfaction_score), 1) AS avg_satisfaction,
    RANK() OVER (PARTITION BY patient_risk_level ORDER BY AVG(complication_flag)) AS rank_by_complication
FROM surgical_operations
GROUP BY patient_risk_level, dashboard_type
ORDER BY patient_risk_level, rank_by_complication;
