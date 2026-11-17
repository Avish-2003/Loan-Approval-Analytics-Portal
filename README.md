# Loan Approval Analytics & Risk Intelligence Portal

## Project Overview
This project analyzes loan application data, applicant credit profiles, and approval trends using Python, Streamlit, and Microsoft Power BI.

The objective is to evaluate credit risk, understand applicant financial health, and provide an interactive multi-page analytics portal for data-driven lending decisions.

## Objectives
- Clean and preprocess raw loan application data using automated median and mode imputation.
- Engineer domain-specific financial indicators (`Loan_to_InHand_Cash_Ratio`, `Residential_Status`, `Vehicle_Status`, and `Children_Dependents`).
- Analyze approval rates across credit scores, debt-to-income (DTI) ratios, loan purposes, and property areas.
- Build an interactive multi-page Streamlit web application with Plotly visualizations and dynamic filtering.
- Develop a 4-page Power BI executive dashboard integrated into the portal via an interactive zoomable gallery.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib & Seaborn
- Plotly
- Streamlit & `streamlit-image-zoom`
- Power BI
- Jupyter Notebook

## Dataset
The dataset (`loan_approval_analysis_400_rows_v2.csv`, 400 rows and 25 variables) contains:
- Application ID & Application Date
- Applicant & Co-Applicant Monthly Income
- Household Income, Monthly Savings & Existing EMI
- Credit Score & Credit History
- Debt-to-Income (DTI) Ratio
- Loan Amount, Loan Purpose & Collateral Value
- Employment Type & Employment Tenure
- Gender, Age, Dependents & Property Area
- Loan Approval Status

## Project Workflow
1. Data Collection & Inspection
2. Data Cleaning & Missing Value Imputation
3. Domain Feature Engineering
4. Exploratory Data Analysis (Jupyter Notebook)
5. Power BI Dashboard Development (4 Executive Pages)
6. Multi-Page Streamlit Portal & Gallery Integration
7. Business & Risk Insights

## Installation

Install the required libraries:

```bash
pip install streamlit pandas numpy matplotlib seaborn plotly pillow streamlit-image-zoom
