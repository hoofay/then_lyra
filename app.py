import streamlit as st
from PIL import Image

# Inject CSS for paper-style tabs and background texture
st.markdown("""
    <style>
    /* Background texture using a subtle paper pattern */
    body {
        background-image: url("https://www.transparenttextures.com/patterns/paper-fibers.png");
        background-repeat: repeat;
        background-color: #fdf6e3;
    }

    /* Main container background */
    [data-testid="stAppViewContainer"] > .main {
        background-color: transparent;
        padding: 2rem;
    }

    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #fdf6e3;
    }

    /* Remove shadows */
    section.main > div {
        box-shadow: none !important;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* Tab bar styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #fdf6e3;
        border-bottom: 3px solid #ccc;
        padding-left: 1rem;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: #f5deb3;
        color: black;
        padding: 0.75rem 1.5rem;
        margin-right: 0.5rem;
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
        border: 1px solid #ccc;
        border-bottom: none;
        font-weight: bold;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }

    .stTabs [aria-selected="true"] {
        background-color: #ffffff;
        color: black;
        border-bottom: none;
        position: relative;
        top: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["Home", "Case 1", "Case 2"])

with tab1:
    col1a, col2a, col3a = st.columns([0.75, 2, 1])
    with col2a:
        st.image("assets/then_blue_crop.png", width=500)

    col1b, col2b, col3b = st.columns([0.75, 2, 1])
    with col2b:
        st.markdown("<p style='font-size:40px; text-align: center;'>I Spy</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:40px; text-align: center;'>with</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:40px; text-align: center;'>My</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:40px; text-align: center;'>Little</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:40px; text-align: center;'>Eye...</p>", unsafe_allow_html=True)

    col1c, col2c, col3c = st.columns([1, 2, 1])
    with col2c:
        st.image("assets/criminal.png", use_container_width=True)

    col1d, col2d, col3d = st.columns([1, 2, 1])
    with col2d:
        video_file = open('assets/thenvideo.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

with tab2:
    st.write("Case 1")

with tab3:
    st.write("Case 2")
