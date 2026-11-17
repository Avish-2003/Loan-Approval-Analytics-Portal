# 🏦 Loan Approval Analytics & Risk Intelligence Portal

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Desktop%20%2F%20Gallery-yellow?style=for-the-badge&logo=powerbi&logoColor=white)](https://powerbi.microsoft.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-orange?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-blueviolet?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/python/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

An enterprise-grade, multi-platform business intelligence and exploratory data science application built for automated loan approval risk assessment, financial health tracking, and portfolio performance insights.

[Explore Live Dashboard](#-installation--local-setup) • [View Architecture](#-project-architecture) • [Report Bug](https://github.com/Avish-2003/Loan-Approval-Analytics-Portal/issues)

</div>

---

## 🌟 Executive Summary

Navigating credit risk requires a blend of rigorous statistical data cleaning, domain-specific feature engineering, and high-impact visual storytelling. This repository houses an end-to-end data platform built on a **400-applicant loan approval dataset** (`loan_approval_analysis_400_rows_v2.csv`). 

It bridges the gap between Python-based data science workflows and corporate Business Intelligence by unifying a **multi-page Streamlit application** with an **interactive Power BI report gallery**.

---

## 🚀 Core Features & Capabilities

* **Multi-Page Streamlit Navigation (`app.py`)**: Seamless runtime routing between the home overview, interactive analytics suite, and executive report gallery.
* **Interactive Streamlit Dashboard (`pages/Streamlit_Dashboard.py`)**:
  * 🎛️ **Dynamic Global Slicing:** Real-time filtering across Loan Status, Property Area, Loan Purpose, Residential Status, and Credit Score ranges.
  * 📊 **4 Analytical Tabs:** Deep dives into Executive Summaries, Credit Risk Health, Loan Purpose Demographics, and Applicant Profile Correlations.
  * 📥 **Self-Service Export:** Instant CSV data extraction of custom filtered subsets.
* **Power BI Executive Report Gallery (`pages/3_PowerBI_Gallery.py`)**:
  * 🖼️ High-resolution visual showcase across 4 core report pages (*Executive Summary*, *Credit Risk*, *Loan & Demographics*, and *Applicant Profile*).
  * 🔍 **Interactive Zoom Integration (`streamlit-image-zoom`)**: Smooth cursor-tracking and scroll-zoom inspection for granular metric analysis.
* **Automated Data Hygiene & Preprocessing**:
  * Robust missing-value handling via median/mode imputation for attributes like `Gender`, `Self_Employed`, `Credit_History`, `Dependents`, `Employment_Tenure_Years`, and `Collateral_Value_INR`.
* **Advanced Domain Feature Engineering**:
  * `Loan_to_InHand_Cash_Ratio`: Quantifies applicant liquidity coverage relative to requested loan sizing.
  * `Residential_Status`: Dynamically evaluates housing stability based on collateral weight and banking longevity.
  * `Vehicle_Status`: Tracks asset collateralization and automobile financing links.
  * `Children_Dependents`: Formats dependent load classifications for accurate risk scoring.

---

## 📂 Project Architecture

```text
D:\#Cronus_Project\
│
├── Raw_DataSet\
│   └── loan_approval_analysis_400_rows_v2.csv
│
├── Streamlit_Analysis\
│   ├── assets\                         # Exported Power BI report page visuals
│   │   ├── page_1.png
│   │   ├── page_2.png
│   │   ├── page_3.png
│   │   └── page_4.png
│   │
│   ├── pages\                          # Multi-page application views
│   │   ├── Streamlit_Dashboard.py
│   │   └── 3_PowerBI_Gallery.py
│   │
│   ├── app.py                          # Main Streamlit application router
│   └── requirements.txt                # Project dependency specifications
│
├── .gitignore
└── README.md
