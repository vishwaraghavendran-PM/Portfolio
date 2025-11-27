# PRD: Real-Time Card Transaction Anomaly Detection

## Problem
High false-decline rates damage customer trust and reduce card-spend revenue. Fraud teams struggle with new attack patterns.

## Goal
Deploy an anomaly detection model with adaptive verification to improve decision accuracy.

## Users
- Cardholders  
- Fraud operations teams  
- Customer support  

## User Stories
- Cardholders want legitimate transactions approved.  
- Cardholders want quick confirmation for unusual transactions.  
- Fraud analysts want visibility into model decisions.

## Scope (MVP)
**In scope:** anomaly model, verification flow, fallback SMS, dashboards  
**Out of scope:** mobile app redesign, cross-border rule overhaul

## KPIs
- False declines: -20%  
- Confirmation completion: 85%+  
- Fraud losses: within 5% tolerance  
- Latency: <30 ms added  

## Data Needs
12 months of anonymized transaction history, device signals, merchant categories, fraud labels.

## Architecture
Authorization engine → anomaly model → thresholds → decision path → logging & feedback.

## Rollout
Shadow → limited → global.

## Acceptance Criteria
- End-to-end verification round-trip < 6 seconds  
- Dashboard live  
- Thresholds configurable  

## Risks
- Excessive challenges → tune thresholds  
- Segment bias → slice testing
