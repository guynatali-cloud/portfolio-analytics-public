# Cybersecurity AI Risk Analytics

## Industry
Cybersecurity

## Research Question
How can AI-assisted analytics help identify high-risk cybersecurity patterns and improve threat prioritization and incident response?

## Business Goal
Analyze the CISA Known Exploited Vulnerabilities (KEV) catalog to identify vendor concentration, ransomware-linked exposure, and remediation prioritization patterns that can support faster, more risk-based decision-making.

## Public Showcase Scope
This public version includes:
- project summary
- selected screenshots
- sample data
- output tables
- dashboard plan
- AI assistance disclosure

It does **not** include the full private working files, full Python workflow, or full transformation pipeline.

## Dataset
**Source:** CISA KEV data (via official `cisagov/kev-data` mirror)  
**Primary file used:** `known_exploited_vulnerabilities.csv`

## Tools Used
- Excel
- SQL
- Python
- Power BI
- AI-assisted analysis support

## Recommended Dashboard
Power BI

## Key Analytical Angles
1. Which vendors and products appear most often in the KEV catalog?
2. Which vulnerabilities are flagged for known ransomware campaign use?
3. How quickly should teams prioritize remediation based on due date and active exploitation?
4. What trends appear over time in vulnerabilities added to the catalog?

## Suggested KPIs
- Total KEVs
- KEVs with known ransomware use
- Top vendors by KEV count
- Average remediation window (dateAdded to dueDate)
- Year-over-year additions

## Files in This Folder
- `sample/` – portfolio-safe sample data
- `outputs/` – exported summary tables
- `screenshots/` – visuals for portfolio presentation

## AI Assistance Used
AI was used to support project structuring, README drafting, KPI brainstorming, and analytics workflow planning. Final project organization and validation were reviewed manually.
