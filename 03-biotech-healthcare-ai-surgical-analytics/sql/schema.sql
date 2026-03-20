-- Schema for Biotech Healthcare AI Surgical Analytics
CREATE TABLE surgical_operations (
    surgery_id VARCHAR(10) PRIMARY KEY,
    surgery_date DATE,
    department VARCHAR(50),
    procedure_name VARCHAR(100),
    surgeon VARCHAR(50),
    operating_room VARCHAR(10),
    shift VARCHAR(20),
    dashboard_type VARCHAR(20),
    patient_risk_level VARCHAR(20),
    anesthesia_type VARCHAR(20),
    scheduled_duration_min INT,
    actual_duration_min INT,
    delay_minutes INT,
    complication_flag INT,
    readmission_30day INT,
    patient_satisfaction_score INT,
    staff_count INT,
    or_utilization_rate DECIMAL(5,2),
    estimated_cost_usd DECIMAL(12,2)
);
