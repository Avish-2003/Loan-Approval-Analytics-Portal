# 🏦 Loan Approval Analytics & Risk Intelligence Portal

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red.svg)](https://streamlit.io/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Desktop%20%2F%20Gallery-yellow.svg)](https://powerbi.microsoft.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-orange.svg)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Visualizations-blueviolet.svg)](https://plotly.com/python/)

An enterprise-grade, multi-platform business intelligence and exploratory data science application built for loan approval risk assessment, financial health tracking, and portfolio performance analysis. 

Developed as part of a college internship project using the **400-applicant Loan Approval dataset** (`loan_approval_analysis_400_rows_v2.csv`).

---

## 🚀 Key Features

* **Multi-Page Streamlit Portal (`app.py`)**: Unified navigation hub linking interactive Python visualizations with an executive Power BI report gallery.
* **Interactive Streamlit Dashboard (`pages/Streamlit_Dashboard.py`)**:
  * **Dynamic Global Filtering:** Real-time slicing by Loan Status, Property Area, Loan Purpose, Residential Status, and Credit Score range.
  * **4 Analytical Tabs:** Executive Summary, Credit Risk Health, Loan Purpose & Demographics, and Applicant Profile Correlations.
  * **Data Export:** Instant CSV data download of filtered subsets.
* **Power BI Executive Report Gallery (`pages/3_PowerBI_Gallery.py`)**:
  * High-resolution visual showcase of 4 core Power BI pages (*Executive Summary*, *Credit Risk*, *Loan & Demographics*, and *Applicant Profile*).
  * Integrated **interactive image zoom** (`streamlit-image-zoom`) for deep-dive metric inspection.
* **Automated Data Hygiene & Preprocessing**:
  * Median and Mode imputation for missing values across demographic and financial attributes (`Gender`, `Self_Employed`, `Credit_History`, `Dependents`, `Employment_Tenure_Years`, `Collateral_Value_INR`).
* **Domain Feature Engineering**:
  * `Loan_to_InHand_Cash_Ratio`: Measures liquidity coverage against requested loan amounts.
  * `Residential_Status`: Evaluates stability based on collateral and banking relationship longevity.
  * `Vehicle_Status`: Tracks asset linking and vehicle financing categories.
  * `Children_Dependents`: Categorizes dependent loads for risk modeling.

---

## 📂 Project Architecture

```text
D:\#Cronus_Project\
│
├── Raw_DataSet\
│   └── loan_approval_analysis_400_rows_v2.csv
│
├── Streamlit_Analysis\
│   ├── assets\                         # Exported Power BI report screenshots
│   │   ├── page_1.png
│   │   ├── page_2.png
│   │   ├── page_3.png
│   │   └── page_4.png
│   │
│   ├── pages\                          # Multi-page application scripts
│   │   ├── Streamlit_Dashboard.py
│   │   └── 3_PowerBI_Gallery.py
│   │
│   ├── app.py                          # Main navigation entry point
│   └── requirements.txt                # Python project dependencies
│
├── .gitignore
└── README.md
