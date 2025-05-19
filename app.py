import streamlit as st
from PIL import Image

# inject paper tab CSS
st.markdown("""
    <style>
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

tab1, tab2, tab3 = st.tabs(["Home", "Case 1", "Case 2"])

with tab1:

    # title
    col1a, col2a, col3a = st.columns([0.75, 2, 1])
    with col2a:
        # Title Logo
        st.image("assets/then_blue_crop.png", width=500)
    
    # text
    col1b, col2b, col3b = st.columns([0.75, 2, 1])
    with col2b:
        # Blurb
        st.markdown("<p style='font-size:40px; text-align: center;'>I Spy</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:40px; text-align: center;'>with</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:40px; text-align: center;'>My</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:40px; text-align: center;'>Little</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:40px; text-align: center;'>Eye...</p>", unsafe_allow_html=True)
    
    # image of magnfying glass
    col1c, col2c, col3c = st.columns([1, 2, 1])
    with col2c:
        # Blurb
        # Magnifying glass + text
        st.image("assets/criminal.png",use_container_width=True)
    
    # video
    col1d, col2d, col3d = st.columns([1, 2, 1])
    with col2d:
    
        # path to video file
        video_file = open('assets/thenvideo.mp4', 'rb')
        video_bytes = video_file.read()
        
        # display video
        st.video(video_bytes)

with tab2:
    st.write('Case 1')

with tab3:
    st.write('Case 2')




