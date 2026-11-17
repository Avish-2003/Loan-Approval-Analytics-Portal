import os
import streamlit as st

st.set_page_config(
    page_title="Loan Analytics Portal",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Resolve absolute directory paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STREAMLIT_PAGE_PATH = os.path.join(BASE_DIR, "pages", "Streamlit_Dashboard.py")
GALLERY_PAGE_PATH = os.path.join(BASE_DIR, "pages", "PowerBI_Dashboard.py")

def home_page():
    st.title("🏦 Loan Approval Analytics & Risk Intelligence Portal")
    st.markdown("### Unified Business Intelligence & Exploratory Data Science Platform")
    st.divider()

    st.markdown(
        """
        Welcome to the **Loan Approval Analysis Portal**. This application brings together two complementary 
        analytics environments built on the **400-applicant Loan Approval dataset** (`loan_approval_analysis_400_rows_v2.csv`), 
        complete with automated missing-value imputation and domain feature engineering.
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info("### 📊 Page 1: Interactive Streamlit & Plotly Dashboard")
        st.markdown(
            """
            * **Dynamic Filtering:** Slice data in real time by Loan Status, Property Area, Loan Purpose, Residential Status, and Credit Score.
            * **4 Analytical Tabs:** Mirrors the executive summary, credit risk health, loan purpose demographics, and applicant profiles.
            * **Engineered Features:** Inspect calculated metrics like *Loan-to-In-Hand Cash Ratio*, *Residential Status*, and *Vehicle Status*.
            * **Data Export:** Filter records and export clean CSV subsets directly.
            """
        )
        if st.button("🚀 Open Streamlit Dashboard", use_container_width=True):
            st.switch_page(streamlit_dash_page)

    with col2:
        st.success("### 🖼️ Page 2: Power BI Executive Report Dashboard")
        st.markdown(
            """
            * **High-Resolution Visuals:** Explore the 4 core analytical Power BI pages (*Executive Summary*, *Credit Risk*, *Loan & Demographics*, and *Applicant Profile*).
            * **Seamless Navigation:** Switch between report sections instantly right inside your browser portal.
            """
        )
        if st.button("📈 Open Power BI Gallery", use_container_width=True):
            st.switch_page(gallery_page)

    st.divider()
    st.caption("College Internship Project • Built with Python, Pandas, NumPy, Plotly, Streamlit & Microsoft Power BI")

# Define page objects for routing
overview_page = st.Page(home_page, title="Home / Overview", icon="🏠", default=True)
streamlit_dash_page = st.Page(STREAMLIT_PAGE_PATH, title="Streamlit Dashboard", icon="📊")
gallery_page = st.Page(GALLERY_PAGE_PATH, title="Power BI Dashboard", icon="🖼️")

# Multi-page navigation router
pg = st.navigation([overview_page, streamlit_dash_page, gallery_page])
pg.run()