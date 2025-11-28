# Evaluation Narrative  
## Lending Risk Scoring Model

### Objective
Evaluate predictive performance, fairness, stability, and business impact for the lending risk score model.

### Data Quality
Bureau data, income reports, and transaction histories evaluated for missingness and anomalies. No structural gaps found.

### Predictive Metrics
- AUC: 0.82  
- KS: 0.49  
- Precision at high-risk threshold: 0.71  
- False decline reduction: 9%  

### Threshold Testing
Low-risk threshold chosen for PD < 2%.  
High-risk threshold set for PD > 8%.  
Mid-band: approx. 18% of cases.

### Fairness
No significant error-rate deviations across demographic groups.  
Explainers aligned with reason-code requirements.

### Stress Testing
Historical recession datasets used. Model remained stable under adverse conditions.

### Business Impact Forecast
- 15% lower expected losses  
- 8% higher approvals  
- 22% fewer manual reviews  
