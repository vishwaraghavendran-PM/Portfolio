```mermaid
flowchart LR
  A[Loan Application] --> B[Data Ingestion]
  B --> C[Feature Engineering]
  C --> D[Risk Model Scoring]
  D --> E[Decision Engine]
  E --> F{Approve / Decline / Review}
  F --> G[Underwriter Dashboard]
  F --> H[Customer Notification]
  G --> I[Feedback Loop]
  H --> I
  I --> C
