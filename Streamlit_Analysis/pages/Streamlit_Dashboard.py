import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv(r"D:/#Cronus_Project/Raw_DataSet/loan_approval_analysis_400_rows_v2.csv")
    
    # Missing Value Imputation
    df['Gender'] = df['Gender'].fillna('Unknown')
    df['Self_Employed'] = df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])
    df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])
    df['Dependents'] = df['Dependents'].fillna(df['Dependents'].median())
    df['Employment_Tenure_Years'] = df['Employment_Tenure_Years'].fillna(df['Employment_Tenure_Years'].median())
    df['Collateral_Value_INR'] = df['Collateral_Value_INR'].fillna(0.0)
    
    # Date Parsing (YYYY-MM-DD)
    df['Application_Date'] = pd.to_datetime(df['Application_Date'], errors='coerce')
    df['Application_Month'] = df['Application_Date'].dt.to_period('M').astype(str)
    
    # Feature Engineering (Mentor-Requested Indicators)
    df['Loan_to_InHand_Cash_Ratio'] = np.where(
        df['Monthly_Savings_INR'] > 0, df['Loan_Amount_INR'] / df['Monthly_Savings_INR'], 0
    )
    df['Residential_Status'] = np.where(
        (df['Collateral_Value_INR'] > 0) | (df['Bank_Relationship_Years'] >= 5),
        'Permanent', 'Rented / Temporary'
    )
    df['Vehicle_Status'] = np.where(
        (df['Loan_Purpose'] == 'Vehicle') | ((df['Loan_Purpose'] != 'Home') & (df['Collateral_Value_INR'] > 0)),
        'Yes (Vehicle Linked)', 'No / Unspecified'
    )
    df['Children_Dependents'] = df['Dependents'].astype(int).astype(str) + ' Children'
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

COLOR_MAP = {'Approved': '#2ecc71', 'Rejected': '#e74c3c'}

# --- SIDEBAR FILTERS ---
st.sidebar.header("🔍 Filter Dashboard")

loan_status_filter = st.sidebar.multiselect(
    "Select Loan Status:", options=df["Loan_Status"].dropna().unique(), default=df["Loan_Status"].dropna().unique()
)
property_area_filter = st.sidebar.multiselect(
    "Select Property Area:", options=df["Property_Area"].dropna().unique(), default=df["Property_Area"].dropna().unique()
)
loan_purpose_filter = st.sidebar.multiselect(
    "Select Loan Purpose:", options=df["Loan_Purpose"].dropna().unique(), default=df["Loan_Purpose"].dropna().unique()
)
residential_filter = st.sidebar.multiselect(
    "Select Residential Status:", options=df["Residential_Status"].unique(), default=df["Residential_Status"].unique()
)

min_score, max_score = int(df["Credit_Score"].min()), int(df["Credit_Score"].max())
credit_score_filter = st.sidebar.slider(
    "Select Credit Score Range:", min_value=min_score, max_value=max_score, value=(min_score, max_score)
)

filtered_df = df[
    (df["Loan_Status"].isin(loan_status_filter)) &
    (df["Property_Area"].isin(property_area_filter)) &
    (df["Loan_Purpose"].isin(loan_purpose_filter)) &
    (df["Residential_Status"].isin(residential_filter)) &
    (df["Credit_Score"] >= credit_score_filter[0]) &
    (df["Credit_Score"] <= credit_score_filter[1])
]

# --- HEADER & KPIS ---
st.title("📊 Interactive Streamlit Loan Analytics Dashboard")
st.divider()

col1, col2, col3, col4, col5 = st.columns(5)
total_apps = len(filtered_df)
approval_rate = (filtered_df['Loan_Status'] == 'Approved').mean() * 100 if total_apps > 0 else 0
avg_income = filtered_df['Household_Income_Monthly_INR'].mean() if total_apps > 0 else 0
avg_loan = filtered_df['Loan_Amount_INR'].mean() if total_apps > 0 else 0
avg_dti = filtered_df['Debt_To_Income_Ratio'].mean() if total_apps > 0 else 0

col1.metric("Total Applications", f"{total_apps}")
col2.metric("Approval Rate", f"{approval_rate:.1f}%")
col3.metric("Avg Monthly Income", f"₹{avg_income:,.0f}")
col4.metric("Avg Loan Amount", f"₹{avg_loan:,.0f}")
col5.metric("Avg DTI Ratio", f"{avg_dti:.2f}")
st.divider()

if total_apps == 0:
    st.warning("No records match your selected filters.")
    st.stop()

# --- 4 ANALYTICAL TABS ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 1. Executive Summary",
    "🛡️ 2. Credit Risk & Financial Health",
    "🏠 3. Loan Purpose & Demographics",
    "👤 4. Applicant Profile & Correlations"
])

with tab1:
    c1, c2 = st.columns(2)
    with c1:
        fig_status = px.pie(
            filtered_df, names='Loan_Status', title='Loan Status Distribution',
            color='Loan_Status', color_discrete_map=COLOR_MAP, hole=0.45
        )
        st.plotly_chart(fig_status, use_container_width=True)
    with c2:
        area_vol = filtered_df.groupby('Property_Area', as_index=False)['Loan_Amount_INR'].sum().sort_values(by='Loan_Amount_INR', ascending=False)
        area_vol['Loan_Volume_Millions'] = area_vol['Loan_Amount_INR'] / 1e6
        fig_area = px.bar(
            area_vol, x='Property_Area', y='Loan_Volume_Millions', color='Property_Area',
            title='Total Loan Volume by Property Area (INR Millions)', text_auto='.2f'
        )
        fig_area.update_layout(showlegend=False)
        st.plotly_chart(fig_area, use_container_width=True)

    monthly_trend = (
        filtered_df[filtered_df['Application_Month'] != 'NaT']
        .groupby('Application_Month', as_index=False).size()
        .rename(columns={'size': 'Applications'}).sort_values('Application_Month')
    )
    fig_trend = px.area(monthly_trend, x='Application_Month', y='Applications', markers=True, title='Application Volume Over Time')
    fig_trend.update_traces(line_color='#2980b9', fillcolor='rgba(52, 152, 219, 0.25)')
    st.plotly_chart(fig_trend, use_container_width=True)

with tab2:
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        fig_credit = px.histogram(
            filtered_df, x='Credit_Score', color='Loan_Status', nbins=25, marginal='box',
            title='Credit Score Distribution by Loan Status', color_discrete_map=COLOR_MAP, barmode='overlay'
        )
        st.plotly_chart(fig_credit, use_container_width=True)
    with r1c2:
        fig_dti = px.box(
            filtered_df, x='Loan_Status', y='Debt_To_Income_Ratio', color='Loan_Status',
            title='Debt-to-Income (DTI) Ratio vs. Loan Status', color_discrete_map=COLOR_MAP
        )
        st.plotly_chart(fig_dti, use_container_width=True)

    r2c1, r2c2 = st.columns(2)
    with r2c1:
        fig_savings = px.scatter(
            filtered_df, x='Monthly_Savings_INR', y='Loan_Amount_INR', color='Loan_Status',
            size='Debt_To_Income_Ratio', hover_data=['Application_ID', 'Loan_to_InHand_Cash_Ratio'],
            title='In-Hand Monthly Savings vs. Requested Loan Amount', color_discrete_map=COLOR_MAP
        )
        st.plotly_chart(fig_savings, use_container_width=True)
    with r2c2:
        ct_credit = pd.crosstab(filtered_df['Credit_History'], filtered_df['Loan_Status'], normalize='index') * 100
        ct_credit.index = [f"Credit History: {int(i)} ({'Good' if i == 1 else 'Bad'})" for i in ct_credit.index]
        fig_ch_heat = px.imshow(ct_credit.round(1), text_auto=True, color_continuous_scale='YlGnBu', aspect='auto', title='Approval Rate (%) by Credit History')
        st.plotly_chart(fig_ch_heat, use_container_width=True)

with tab3:
    d1c1, d1c2 = st.columns(2)
    with d1c1:
        purpose_avg = filtered_df.groupby(['Loan_Purpose', 'Loan_Status'], as_index=False)['Loan_Amount_INR'].mean()
        fig_purpose = px.bar(
            purpose_avg, y='Loan_Purpose', x='Loan_Amount_INR', color='Loan_Status',
            barmode='group', orientation='h', title='Average Loan Amount by Purpose & Status', color_discrete_map=COLOR_MAP
        )
        st.plotly_chart(fig_purpose, use_container_width=True)
    with d1c2:
        emp_counts = filtered_df.groupby(['Employment_Type', 'Loan_Status'], as_index=False).size().rename(columns={'size': 'Count'})
        fig_emp = px.bar(
            emp_counts, x='Employment_Type', y='Count', color='Loan_Status',
            barmode='group', title='Applications by Employment Type', color_discrete_map=COLOR_MAP
        )
        st.plotly_chart(fig_emp, use_container_width=True)

    fig_collateral = px.scatter(
        filtered_df, x='Collateral_Value_INR', y='Loan_Amount_INR', color='Loan_Status',
        hover_data=['Application_ID', 'Loan_Purpose', 'Property_Area'],
        title='Collateral Value vs. Requested Loan Amount', color_discrete_map=COLOR_MAP
    )
    st.plotly_chart(fig_collateral, use_container_width=True)

with tab4:
    p1c1, p1c2 = st.columns(2)
    with p1c1:
        income_split = (
            filtered_df.groupby('Loan_Status', as_index=False)[['Applicant_Income_Monthly_INR', 'Coapplicant_Income_Monthly_INR']]
            .mean().melt(id_vars='Loan_Status', var_name='Income_Source', value_name='Monthly_Income_INR')
        )
        income_split['Income_Source'] = income_split['Income_Source'].replace({
            'Applicant_Income_Monthly_INR': 'Primary Applicant Income',
            'Coapplicant_Income_Monthly_INR': 'Co-Applicant Income'
        })
        fig_inc_split = px.bar(
            income_split, x='Loan_Status', y='Monthly_Income_INR', color='Income_Source',
            barmode='stack', title='Average Primary vs. Co-Applicant Monthly Income', color_discrete_sequence=['#34495e', '#1abc9c']
        )
        st.plotly_chart(fig_inc_split, use_container_width=True)
    with p1c2:
        fig_tenure = px.box(
            filtered_df, x='Loan_Status', y='Employment_Tenure_Years', color='Loan_Status',
            title='Last Company Tenure (Years) by Loan Status', color_discrete_map=COLOR_MAP
        )
        st.plotly_chart(fig_tenure, use_container_width=True)

    p2c1, p2c2 = st.columns(2)
    with p2c1:
        res_counts = filtered_df.groupby(['Residential_Status', 'Loan_Status'], as_index=False).size().rename(columns={'size': 'Count'})
        fig_res = px.bar(
            res_counts, x='Residential_Status', y='Count', color='Loan_Status',
            barmode='group', title='Permanent vs. Temporary Residential Status', color_discrete_map=COLOR_MAP
        )
        st.plotly_chart(fig_res, use_container_width=True)
    with p2c2:
        child_order = ['0 Children', '1 Children', '2 Children', '3 Children', '4 Children']
        child_counts = filtered_df.groupby(['Children_Dependents', 'Loan_Status'], as_index=False).size().rename(columns={'size': 'Count'})
        fig_child = px.bar(
            child_counts, x='Children_Dependents', y='Count', color='Loan_Status',
            barmode='group', category_orders={'Children_Dependents': child_order},
            title='Loan Approvals by Number of Children / Dependents', color_discrete_map=COLOR_MAP
        )
        st.plotly_chart(fig_child, use_container_width=True)

    p3c1, p3c2 = st.columns([1, 2])
    with p3c1:
        veh_counts = filtered_df.groupby(['Vehicle_Status', 'Loan_Status'], as_index=False).size().rename(columns={'size': 'Count'})
        fig_veh = px.bar(
            veh_counts, x='Vehicle_Status', y='Count', color='Loan_Status',
            barmode='group', title='Vehicle Ownership / Financing Status', color_discrete_map=COLOR_MAP
        )
        st.plotly_chart(fig_veh, use_container_width=True)
    with p3c2:
        num_cols = [
            'Age', 'Household_Income_Monthly_INR', 'Employment_Tenure_Years',
            'Credit_Score', 'Existing_EMI_Monthly_INR', 'Monthly_Savings_INR',
            'Debt_To_Income_Ratio', 'Loan_Amount_INR', 'Collateral_Value_INR', 'Bank_Relationship_Years'
        ]
        corr_matrix = filtered_df[num_cols].corr().round(2)
        fig_corr = px.imshow(
            corr_matrix, text_auto=True, color_continuous_scale='RdBu_r', zmin=-1, zmax=1,
            aspect='auto', title='Correlation Matrix of Numerical Financial Features'
        )
        st.plotly_chart(fig_corr, use_container_width=True)

st.divider()
st.subheader("📑 Data Exploration & Export")
st.dataframe(filtered_df, use_container_width=True)

csv_data = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(label="📥 Download Filtered Data as CSV", data=csv_data, file_name="filtered_loan_data.csv", mime="text/csv")