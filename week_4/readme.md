# Lead Scoring Classification Project

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## Overview

This project focuses on building a **Logistic Regression** model to predict whether a lead will convert on a platform. The dataset contains various features like `lead_source`, `industry`, `annual_income`, etc., and the goal is to predict the binary target variable **converted**.

We apply various machine learning techniques, including data preprocessing, model training, evaluation, and hyperparameter tuning to optimize the model's performance.

---

## Key Steps

1. **Data Preprocessing**: 
   - Handle missing values.
   - Perform one-hot encoding for categorical features.
   - Split the data into training, validation, and test sets.

2. **Model Training**:
   - Train a **Logistic Regression** model using the training data.
   - Evaluate the model using **AUC** (Area Under the ROC Curve) on the validation set.

3. **Model Evaluation**:
   - Evaluate the model's performance using **Precision**, **Recall**, and **F1-Score** at different thresholds.

4. **Hyperparameter Tuning**:
   - Use **5-fold Cross-Validation** to evaluate different values of the regularization parameter `C` in **Logistic Regression**.

---

## Technologies Used

- **Python**
- **Pandas**: For data manipulation.
- **Scikit-learn**: For machine learning models, evaluation metrics, and cross-validation.
- **NumPy**: For numerical operations.
- **Matplotlib**: For plotting the precision-recall curve.

---

## Results

- **Best Logistic Regression Model**: Found using hyperparameter tuning, the optimal `C` value was **1**, yielding the best AUC score.
- **Precision and Recall Curves**: The curves intersected around a threshold of **0.59**.

---

## How to Run

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the Python script to train the model and view the results.

---

## Future Work

- Explore additional machine learning models for comparison (e.g., Random Forest, XGBoost).
- Experiment with more advanced feature engineering techniques.

---

## License

MIT License - see [LICENSE](LICENSE) for details.

