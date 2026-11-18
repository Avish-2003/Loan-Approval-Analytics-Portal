import os
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Loan Analytics Portal",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Resolve absolute directory paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_PAGE_PATH = os.path.join(BASE_DIR, "pages", "Upload_Dataset.py")
STREAMLIT_PAGE_PATH = os.path.join(BASE_DIR, "pages", "Streamlit_Dashboard.py")
GALLERY_PAGE_PATH = os.path.join(BASE_DIR, "pages", "PowerBI_Dashboard.py")

def home_page():
    st.title("🏦 Loan Approval Analytics & Risk Intelligence Portal")
    st.markdown("### Unified Business Intelligence & Exploratory Data Science Platform")
    st.divider()

    st.markdown(
        """
        Welcome to the **Loan Approval Analysis Portal**. This application brings together dynamic dataset uploading, 
        exploratory data analysis, and executive Power BI reporting built on loan approval datasets, 
        complete with automated missing-value imputation and domain feature engineering.
        """
    )

    # --- QUICK UPLOAD WIDGET ON HOME PAGE ---
    with st.expander("📂 Quick Upload Custom Dataset (Optional)", expanded=False):
        st.markdown("Upload your custom CSV dataset here to cache it into the session instantly across all pages:")
        home_uploaded_file = st.file_uploader("Choose a loan CSV file", type=["csv"], key="home_uploader")
        
        if home_uploaded_file is not None:
            try:
                df_home = pd.read_csv(home_uploaded_file)
                st.session_state['uploaded_df'] = df_home
                st.session_state['uploaded_filename'] = home_uploaded_file.name
                st.success(f"✅ Successfully cached **{home_uploaded_file.name}** ({df_home.shape[0]:,} rows) into session memory!")
            except Exception as e:
                st.error(f"Error loading file: {e}")
                
        if 'uploaded_df' in st.session_state and st.session_state['uploaded_df'] is not None:
            st.info(f"📌 Currently Active Custom Dataset: **{st.session_state.get('uploaded_filename', 'Custom CSV')}**")
            if st.button("🗑️ Clear Custom Dataset (Revert to Default)"):
                del st.session_state['uploaded_df']
                if 'uploaded_filename' in st.session_state:
                    del st.session_state['uploaded_filename']
                st.rerun()

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.warning("### 📂 Page 1: Dataset Upload Portal")
        st.markdown(
            """
- **Custom CSV Upload:** Upload your own loan portfolios dynamically.
- **Data Health Checks:** Inspect missing values, row/column counts, and data types instantly.
- **Session Caching:** Seamlessly load your data into the session memory for live analysis.
            """
        )
        if st.button("🚀 Open Upload Portal", use_container_width=True):
            st.switch_page(upload_page)

    with col2:
        st.info("### 📊 Page 2: Interactive Streamlit Dashboard")
        st.markdown(
            """
- **Dynamic Filtering:** Slice data in real time by Loan Status, Property Area, Loan Purpose, and Credit Score.
- **4 Analytical Tabs:** Executive summary, credit risk health, loan purpose demographics, and applicant profiles.
- **Engineered Features:** Inspect calculated metrics like *Loan-to-In-Hand Cash Ratio*, *Residential Status*, and *Vehicle Status*.
            """
        )
        if st.button("🚀 Open Streamlit Dashboard", use_container_width=True):
            st.switch_page(streamlit_dash_page)

    with col3:
        st.success("### 🖼️ Page 3: Power BI Executive Report")
        st.markdown(
            """
- **High-Resolution Visuals:** Explore the core analytical Power BI report sections.
- **Seamless Navigation:** Switch between report components instantly right inside your browser portal.
            """
        )
        if st.button("📈 Open Power BI Gallery", use_container_width=True):
            st.switch_page(gallery_page)

    st.divider()
    st.caption("College Internship Project • Built with Python, Pandas, NumPy, Plotly, Streamlit & Microsoft Power BI")

# Define page objects for routing
overview_page = st.Page(home_page, title="Home / Overview", icon="🏠", default=True)
upload_page = st.Page(UPLOAD_PAGE_PATH, title="Upload Dataset", icon="📂")
streamlit_dash_page = st.Page(STREAMLIT_PAGE_PATH, title="Streamlit Dashboard", icon="📊")
gallery_page = st.Page(GALLERY_PAGE_PATH, title="Power BI Dashboard", icon="🖼️")

# Multi-page navigation router
pg = st.navigation([overview_page, upload_page, streamlit_dash_page, gallery_page])
pg.run()