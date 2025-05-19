import streamlit as st
from PIL import Image

# style CSS
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Shadows+Into+Light&display=swap" rel="stylesheet">

    <style>
    /* Background everywhere */
    html, body, [data-testid="stApp"], [data-testid="stAppViewContainer"], .main, .block-container {
        background-image: url("https://www.transparenttextures.com/patterns/paper-fibers.png");
        background-color: #fdf6e3;
        background-repeat: repeat;
        background-attachment: fixed;
        color: #333333; /* pencil grey */
    }

    /* Override ALL text to pencil-grey */
    html, body, div, h1, h2, h3, h4, h5, h6, p, span, li, label {
        color: #333333 !important;
    }

    /* Tabs wrapper */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #fdf6e3;
        border-bottom: 3px solid #ccc;
        padding-left: 1rem;
        margin-top: -40px;  /* pull tabs up to hide top strip */
    }

    /* Individual tabs styled like folder dividers */
    .stTabs [data-baseweb="tab"] {
        background-color: #f5deb3;
        color: #333333 !important;
        padding: 0.75rem 1.5rem;
        margin-right: -0.5rem;
        border-top-left-radius: 12px;
        border-top-right-radius: 12px;
        border: 1px solid #ccc;
        border-bottom: none;
        font-weight: bold;
        box-shadow: 3px -2px 5px rgba(0,0,0,0.15);
        transform: translateY(2px);
        position: relative;
        z-index: 1;
    }

    /* Active tab pops forward */
    .stTabs [aria-selected="true"] {
        background-color: #ffffff;
        z-index: 2;
        top: 2px;
    }

    /* Clean container padding */
    .block-container {
        padding: 2rem;
    }

    /* Sidebar matching */
    [data-testid="stSidebar"] {
        background-color: #fdf6e3;
        color: #333333;
    }

    /* Remove Streamlit's default header spacing/padding */
    header[data-testid="stHeader"] {
        background: none;
        height: 0;
    }

    /* Clean up video border if needed */
    video {
        border: 1px solid #aaa;
        border-radius: 8px;
    }

    /* Handwritten font for large headings */
    .handwritten {
        font-family: 'Shadows Into Light', cursive;
        font-size: 40px;
        text-align: center;
        color: #333333;
    }

    /* Torn edge effect on top of main area */
    [data-testid="stAppViewContainer"] > .main::before {
        content: "";
        display: block;
        width: 100%;
        height: 50px;
        background: url('https://www.transparenttextures.com/patterns/rip-paper.png') repeat-x;
        background-size: contain;
        margin-bottom: -30px;
        z-index: 10;
        position: relative;
    }
    
    /* Optional: torn bottom as well */
    [data-testid="stAppViewContainer"] > .main::after {
        content: "";
        display: block;
        width: 100%;
        height: 50px;
        background: url('https://www.transparenttextures.com/patterns/rip-paper.png') repeat-x;
        background-size: contain;
        margin-top: -20px;
        z-index: 10;
        position: relative;
        transform: rotate(180deg);
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
        st.markdown("<p class='handwritten'; style='font-size:40px; text-align: center;>I Spy</p>", unsafe_allow_html=True)
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
