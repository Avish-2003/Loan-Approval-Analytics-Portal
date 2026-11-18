import streamlit as st
import pandas as pd

st.title("📂 Dataset Upload & Preprocessing Portal")
st.markdown("""
Upload your custom loan dataset (CSV format) below. It will be stored automatically in your active session 
so you can immediately explore it on the **Streamlit Dashboard** page.
""")
st.divider()

# Show active dataset status at the top
if 'uploaded_df' in st.session_state and st.session_state['uploaded_df'] is not None:
    st.success(f"✅ Active Custom Dataset Loaded in Session: **{st.session_state.get('uploaded_filename', 'Custom CSV')}** ({st.session_state['uploaded_df'].shape[0]} rows)")
    if st.button("🗑️ Clear Uploaded Dataset (Revert to Default)"):
        del st.session_state['uploaded_df']
        if 'uploaded_filename' in st.session_state:
            del st.session_state['uploaded_filename']
        st.rerun()

# --- FILE UPLOADER WIDGET ---
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        
        # Immediately save to session_state so switching pages keeps the data
        st.session_state['uploaded_df'] = df
        st.session_state['uploaded_filename'] = uploaded_file.name

        st.success(f"Successfully loaded **{uploaded_file.name}** into the dashboard session!")

        # --- DATA SUMMARY & METRICS ---
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Rows", f"{df.shape[0]:,}")
        col2.metric("Total Columns", f"{df.shape[1]}")
        col3.metric("Missing Values", f"{df.isna().sum().sum():,}")
        col4.metric("Duplicate Rows", f"{df.duplicated().sum():,}")

        st.divider()

        # --- RAW DATA PREVIEW ---
        st.subheader("🔍 Raw Data Preview (First 5 Rows)")
        st.dataframe(df.head(), use_container_width=True)

        # --- DATA QUALITY & TYPES INSPECTION ---
        st.subheader("🛠️ Column Data Types & Null Counts")
        buffer_df = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Non-Null Count": df.notnull().sum(),
            "Null Count": df.isnull().sum()
        }).reset_index(drop=True)
        st.dataframe(buffer_df, use_container_width=True)

    except Exception as e:
        st.error(f"Error processing the uploaded file: {e}")
elif 'uploaded_df' not in st.session_state:
    st.info("ℹ️ Awaiting CSV upload. If no file is uploaded here, the default project dataset will be used.")

    with st.expander("📋 View Expected Dataset Schema / Columns Guide"):
        st.markdown("""
        Your dataset should ideally include columns matching the project schema:
        * `Application_ID`, `Loan_Status`, `Credit_Score`, `Loan_Amount_INR`
        * `Household_Income_Monthly_INR`, `Monthly_Savings_INR`, `Debt_To_Income_Ratio`
        * `Property_Area`, `Loan_Purpose`, `Employment_Type`, `Collateral_Value_INR`
        """)