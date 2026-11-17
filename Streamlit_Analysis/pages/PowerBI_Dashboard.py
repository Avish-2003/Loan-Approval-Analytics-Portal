import os
import streamlit as st

st.title("📈 Power BI Executive Report Dashboard")
st.markdown("Explore the 4 core analytical pages of the Power BI report exported as high-resolution visuals.")
st.divider()

# Resolve image directory relative to this page file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Assuming images are stored in a folder named 'assets' inside Streamlit_Analysis
ASSETS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "assets"))

pages_dict = {
    "1. Executive Summary": "page_1.png",
    "2. Credit Risk Health": "page_2.png",
    "3. Loan Purpose & Demographics": "page_3.png",
    "4. Applicant Profile": "page_4.png"
}

selected_tab = st.selectbox("Select Report Page to View:", list(pages_dict.keys()))

img_filename = pages_dict[selected_tab]
img_path = os.path.join(ASSETS_DIR, img_filename)

if os.path.exists(img_path):
    st.image(img_path, caption=f"Power BI Report - {selected_tab}", use_column_width=True)
else:
    st.warning(f"Image not found at `{img_path}`.")
    st.info(
        "**Setup Instructions:**\n"
        "1. Create an `assets` folder inside your `Streamlit_Analysis` directory.\n"
        "2. Place your exported PNG images (`page_1.png`, `page_2.png`, etc.) inside that folder."
    )