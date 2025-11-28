# Architecture Diagram Specification  
## Lending Risk Scoring System

### Components
1. Data Sources  
   - Credit Bureau  
   - KYC & Identity  
   - Bank Transactions  
   - Loan Applications  
   - Repayment Records  

2. Data Ingestion  
3. Feature Engineering  
4. Model Training  
5. Model Registry  
6. Real-Time Scoring  
7. Decision Engine  
8. Underwriter Dashboard  
9. Monitoring + Drift Detection  
10. Feedback Loop  

### End-to-End Flow
Application → Data Ingestion → Feature Engineering → ML Scoring → Decision Engine → Approve/Decline/Review → Monitoring → Feedback → Retraining.
