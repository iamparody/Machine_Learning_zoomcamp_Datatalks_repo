# 🏦 Loan Default Prediction System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Machine Learning](https://img.shields.io/badge/ML-XGBoost-orange)
![API](https://img.shields.io/badge/API-FastAPI-green)
![Deployment](https://img.shields.io/badge/Deployment-Docker-lightblue)
![License](https://img.shields.io/badge/License-MIT-yellow)

An end-to-end machine learning system for predicting loan defaults in financial institutions. This project demonstrates a complete ML pipeline from data exploration to deployed web service.

## 📊 Business Problem

**Objective**: Reduce non-performing loans by predicting customer defaults with 76% recall and balanced precision.

**Impact**: 
- Catch 76% of bad loans before disbursement
- Reduce manual review costs by 64%
- Net positive business value through targeted risk management




## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Docker (for container deployment)

### Option 1: Local Development

1. **Clone & Setup**
```bash
git clone <repository-url>
cd loan-default-prediction
pip install -r requirements.txt
Test Model Deployment


python deploy_model.py
Run Web Service



python loan_default_predictor.py
Access API

curl http://localhost:8000/health
Option 2: Docker Deployment
Build Image


docker build -t loan-predictor .
Run Container


docker run -d -p 8000:8000 --name loan-api loan-predictor
Verify Deployment

curl http://localhost:8000/health
Option 3: Docker Compose (Recommended for Production)
Create docker-compose.yml



services:
  loan-predictor:
    build: .
    ports:
      - "8000:8000"
    environment:
      - MODEL_PATH=/app/models/xgboost_loan_model.pkl
      - ENCODERS_PATH=/app/models/label_encoders.pkl
    volumes:
      - ./models:/app/models
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
Deploy with Compose


docker-compose up -d
Check Status


docker-compose ps
📈 Model Performance
Key Metrics
Metric	Value	Business Impact
Recall	76.3%	Catch 76% of bad loans
Precision	25.9%	26% of flagged loans are actually bad
F1-Score	38.7%	Balanced performance
Threshold	0.45	Optimal decision boundary
Feature Importance (Top 10)
Loan Amount Volatility (prev_loan_amount_std) - 29.6%

Previous Loan Count - 10.1%

Geographic Location (GPS coordinates) - 9.4%

Customer Age - 8.7%

Employment Status - 8.6%

Bank Account Type - 7.8%

Average Total Due - 6.9%

Average Term Days - 5.6%

Average Loan Amount - 5.4%

🔌 API Documentation
Base URL

http://localhost:8000
Endpoints
🟢 Health Check

GET /health
Response:

{
  "status": "healthy",
  "model_loaded": true
}
🔍 Single Prediction

POST /predict
Request:


{
  "customerid": "8a858e42570314e001570584d48641dc",
  "bank_account_type": "Savings",
  "longitude_gps": 3.45,
  "latitude_gps": 6.52,
  "bank_name_clients": "GT Bank",
  "employment_status_clients": "Permanent",
  "birthdate": "1985-08-23",
  "prev_loan_count": 3.0,
  "prev_loan_amount_mean": 15000.0,
  "prev_loan_amount_max": 20000.0,
  "prev_loan_amount_min": 10000.0,
  "prev_loan_amount_std": 5000.0,
  "prev_total_due_mean": 18000.0,
  "prev_term_days_mean": 30.0,
  "prev_max_loannumber": 3.0
}
Response:


{
  "customerid": "8a858e42570314e001570584d48641dc",
  "prediction": 0,
  "probability": 0.2345,
  "risk_level": "Low",
  "recommendation": "Approve"
}
📦 Batch Predictions

POST /batch_predict
Request: Array of loan applications

🛠️ Development
Data Sources
The system integrates three data sources:

Demographics: Customer background information

Performance: Current loan details + target variable

Previous Loans: Historical loan performance

Feature Engineering
Temporal Features: Loan sequence, payment patterns

Demographic Features: Age groups, employment stability

Behavioral Features: Loan amount volatility, frequency

Geographic Features: Location-based risk clustering

Model Selection
Algorithm: XGBoost with class weighting

Imbalance Handling: scale_pos_weight for class balance

Optimization: Grid search for hyperparameter tuning

Threshold: 0.45 for balanced precision/recall

🧪 Testing
Model Testing

python deploy_model.py
API Testing

# Health check
curl http://localhost:8000/health

# Single prediction
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "customerid": "test123",
    "bank_account_type": "Savings",
    "longitude_gps": 3.45,
    "latitude_gps": 6.52,
    "bank_name_clients": "GT Bank",
    "employment_status_clients": "Permanent",
    "birthdate": "1985-08-23",
    "prev_loan_count": 3.0,
    "prev_loan_amount_mean": 15000.0,
    "prev_loan_amount_max": 20000.0,
    "prev_loan_amount_min": 10000.0,
    "prev_loan_amount_std": 5000.0,
    "prev_total_due_mean": 18000.0,
    "prev_term_days_mean": 30.0,
    "prev_max_loannumber": 3.0
  }'
🔧 Configuration
Model Configuration
Threshold: 0.45 (balanced strategy)

Risk Levels:

Low: < 0.3 (Approve)

Medium: 0.3-0.6 (Review)

High: > 0.6 (Reject)

Environment Variables

export MODEL_PATH="./models/xgboost_loan_model.pkl"
export ENCODERS_PATH="./models/label_encoders.pkl"
export API_PORT=8000
🚢 Deployment
Production Deployment
Build optimized Docker image


docker build -t loan-predictor:prod .
Run with environment variables


docker run -d \
  -p 8000:8000 \
  -e MODEL_PATH="/app/models/xgboost_loan_model.pkl" \
  -e ENCODERS_PATH="/app/models/label_encoders.pkl" \
  --name loan-predictor-prod \
  loan-predictor:prod
Docker Compose (Recommended)


docker-compose up -d
Monitoring
API health: GET /health

Model performance: Logged predictions

Business metrics: Default rate tracking

📊 Business Integration
Recommended Workflow
Pre-screening: Run all applications through API

Risk Tiers:

Low risk: Auto-approve

Medium risk: Manual review

High risk: Auto-reject or senior review

Continuous Learning: Retrain model quarterly with new data
