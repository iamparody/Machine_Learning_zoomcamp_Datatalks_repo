# Car Fuel Efficiency Prediction

Predicting car fuel efficiency using Decision Trees, Random Forests, and XGBoost.

[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.2.2-orange?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/xgboost-1.7.6-red?logo=xgboost&logoColor=white)](https://xgboost.readthedocs.io/)

## Overview
This project explores regression models to predict the fuel efficiency (`fuel_efficiency_mpg`) of cars based on attributes like weight, model year, origin, and fuel type.

## Dataset
The dataset is sourced from [Alexey Grigorev's GitHub](https://github.com/alexeygrigorev/datasets/blob/master/car_fuel_efficiency.csv).

## Features
- vehicle_weight  
- model_year  
- origin  
- fuel_type  
- ...and more

## Models
- Decision Tree Regressor  
- Random Forest Regressor  
- XGBoost Regressor  

## Key Findings
- `vehicle_weight` is the most important feature in tree-based models.  
- Lower `eta` in XGBoost (0.1) improved RMSE on the validation set.  
- Random Forest with sufficient `n_estimators` stabilizes RMSE around 0.435.

## How to Run
1. Install dependencies:
```bash
pip install pandas numpy scikit-learn xgboost matplotlib
