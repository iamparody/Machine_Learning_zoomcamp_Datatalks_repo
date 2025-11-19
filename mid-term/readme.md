
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

## 🏗️ Project Architecture



notebooks/
└── loan_default_analysis.ipynb  # EDA & Model Development

src/
├── loan_default_predictor.py    # FastAPI Web Service
├── xgboost_loan_model.pkl       # Trained Model
├── label_encoders.pkl           # Feature Encoders
├── model_config.pkl            # Configuration
└── requirements.txt            # Dependencies

deployment/
├── Dockerfile
├── deploy_model.py
└── docker-compose.yml

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
```

2. **Test Model Deployment**
```bash
python deploy_model.py
```

3. **Run Web Service**
```bash
python loan_default_predictor.py
```

4. **Access API**
```bash
curl http://localhost:8000/health
```

