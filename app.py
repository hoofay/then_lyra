import streamlit as st
from PIL import Image

#st.set_page_config(page_title="T.H.E.N.", layout="centered")

col1a, col2a, col3a = st.columns([0.75, 2, 1])
with col2a:
    # Title Logo
    st.image("assets/then_blue_crop.png", width=500)


col1b, col2b, col3b = st.columns([0.75, 2, 1])
with col2b:
    # Blurb
    st.markdown("<p style='font-size:40px; text-align: center;'>I Spy</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:40px; text-align: center;'>with</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:40px; text-align: center;'>My</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:40px; text-align: center;'>Little</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:40px; text-align: center;'>Eye...</p>", unsafe_allow_html=True)

col1c, col2c, col3c = st.columns([1, 2, 1])
with col2c:
    # Blurb
    # Magnifying glass + text
    st.image("assets/criminal.png",use_container_width=True)





