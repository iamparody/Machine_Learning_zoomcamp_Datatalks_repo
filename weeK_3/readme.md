Lead Scoring Project

Project Overview: This project focuses on lead scoring, which is the process of assigning a numerical score to each lead to determine their likelihood of becoming a paying customer. The goal is to identify the most promising leads for follow-up, optimizing marketing and sales efforts.

Breakdown of Steps
Data Loading and Initial Exploration

  Loaded a dataset containing information about potential leads, including their source, industry, viewing habits, income, employment status, location, and interaction count, along with a target variable indicating whether they converted ('converted').
  Displayed the first few rows to get a glimpse of the data.

Data Preparation

  Handled missing values by replacing them with 'NA' for categorical features and 0.0 for numerical features.

Exploratory Data Analysis (EDA)

  Performed basic EDA, including:
    
      Finding the most frequent observation for the 'industry' column.
      Calculating the correlation matrix for numerical features.
      Calculating mutual information scores between categorical features and the target variable to understand their relationship.
    
  

Data Splitting

  Split the data into training (60%), validation (20%), and test (20%) sets to prepare for model development and evaluation.

Feature Engineering

  Applied one-hot encoding to the categorical features to convert them into a numerical format suitable for the logistic regression model.

Model Training and Evaluation

  Trained a baseline logistic regression model using all features on the training set and evaluated its accuracy on the validation set.
  Performed a feature elimination analysis by removing specific features ('industry', 'employment_status', 'lead_score') one by one, retraining the model, and observing the change in accuracy to understand the importance of each feature.
  Trained regularized logistic regression models with different values of the regularization parameter (C) to find the optimal value that provides the best accuracy on the validation set.
