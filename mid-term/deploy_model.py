
"""
Loan Default Prediction Deployment Script
Usage: python deploy_model.py
"""

import joblib
import pandas as pd
import numpy as np

def deploy_model():
    """Deploy the trained model with all assets"""
    print("🚀 DEPLOYING LOAN DEFAULT PREDICTION MODEL")
    print("="*50)
    
    # Load model assets
    try:
        model = joblib.load('xgboost_loan_model.pkl')
        encoders = joblib.load('label_encoders.pkl') 
        config = joblib.load('model_config.pkl')
        
        print("✅ Model assets loaded successfully:")
        print(f"   - Model: xgboost_loan_model.pkl")
        print(f"   - Encoders: {len(encoders)} categorical encoders")
        print(f"   - Features: {len(config['feature_columns'])} features")
        print(f"   - Threshold: {config['optimal_threshold']}")
        
        # Test prediction with sample data
        print("\n🧪 TESTING MODEL WITH SAMPLE DATA...")
        
        # Create sample input
        sample_input = {
            'bank_account_type': 'Savings',
            'longitude_gps': 3.45,
            'latitude_gps': 6.52,
            'bank_name_clients': 'GT Bank', 
            'employment_status_clients': 'Permanent',
            'birthdate_missing': 0,
            'age': 35,
            'age_group': '26-35',
            'prev_loan_count': 3.0,
            'prev_loan_amount_mean': 15000.0,
            'prev_loan_amount_max': 20000.0,
            'prev_loan_amount_min': 10000.0,
            'prev_loan_amount_std': 5000.0,
            'prev_total_due_mean': 18000.0,
            'prev_term_days_mean': 30.0,
            'prev_max_loannumber': 3.0,
            'has_loan_history': 1,
            'loan_count_category': 'Low'
        }
        
        # Encode sample input
        encoded_input = []
        for feature in config['feature_columns']:
            value = sample_input[feature]
            if feature in encoders:
                value = encoders[feature].transform([str(value)])[0]
            encoded_input.append(value)
        
        # Make prediction
        probability = model.predict_proba([encoded_input])[0, 1]
        prediction = 1 if probability >= config['optimal_threshold'] else 0
        
        print(f"✅ SAMPLE PREDICTION:")
        print(f"   - Default Probability: {probability:.3f}")
        print(f"   - Prediction: {'BAD' if prediction == 1 else 'GOOD'}")
        print(f"   - Risk Level: {'High' if probability > 0.6 else 'Medium' if probability > 0.3 else 'Low'}")
        
        print("\n🎉 DEPLOYMENT SUCCESSFUL!")
        print("Next: Run the FastAPI server with: python loan_default_predictor.py")
        
    except Exception as e:
        print(f"❌ Deployment failed: {e}")

if __name__ == "__main__":
    deploy_model()
