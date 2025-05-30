import streamlit as st
from PIL import Image

# Add vertical space above the tabs using custom HTML
st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

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

    .dossier-container {
        font-family: 'Shadows Into Light', cursive;
        color: #333333;
        background: #fdf6e3;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.1);
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    
    </style>
""", unsafe_allow_html=True)


# Tabs
tab1, tab2, tab3 = st.tabs(["Home", "Case 1", "Case 2"])

with tab1:
    
    col1a, col2a, col3a = st.columns([0.75, 2, 1])
    with col2a:
        st.image("assets/then.png", width=500)

    # col1b, col2b, col3b = st.columns([0.75, 2, 1])
    # with col2b:
        # st.markdown("<p style='font-size:40px; text-align: center;'>I Spy</p>", unsafe_allow_html=True)
        # st.markdown("<p style='font-size:40px; text-align: center;'>with</p>", unsafe_allow_html=True)
        # st.markdown("<p style='font-size:40px; text-align: center;'>My</p>", unsafe_allow_html=True)
        # st.markdown("<p style='font-size:40px; text-align: center;'>Little</p>", unsafe_allow_html=True)
        # st.markdown("<p style='font-size:40px; text-align: center;'>Eye...</p>", unsafe_allow_html=True)

    # col1c, col2c, col3c = st.columns([1, 2, 1])
    # with col2c:
        # st.image("assets/criminal.png", use_container_width=True)

    col1d, col2d, col3d = st.columns([1, 2, 1])
    with col2d:
        video_file = open('assets/thenvideo.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)


with tab2:
    st.markdown("""
        <div style="font-family: 'Shadows Into Light', cursive; color: #333333; background: #fdf6e3; padding: 2rem; border-radius: 12px; box-shadow: 3px 3px 10px rgba(0,0,0,0.1);">
            <h2 style="text-align:center;">🕵️‍♂️ Case File: The Missing Cardigan</h2>
            <p><strong>DATE:</strong> May 19, 2025</p>
            <p><strong>LOCATION:</strong> Lincoln Elementary School</p>
            <p><strong>DETECTIVE:</strong> You (aka The Little Eye)</p>
            <hr>
            <h4>Summary:</h4>
            <p>A beloved cardigan belonging to Emily has mysteriously vanished from the classroom cloakroom during recess. The school is abuzz with whispers and suspicion. Can you find the missing sweater before the day ends?</p>
            <h4>Victim:</h4>
            <p>Emily's favorite soft, light blue cardigan with pearl buttons.</p>
            <h4>Suspects:</h4>
            <ul>
                <li><strong>Tommy:</strong> Known for borrowing classmates' things without asking.</li>
                <li><strong>Sarah:</strong> Loves fashion and might want a new look.</li>
                <li><strong>Jake:</strong> Was seen near the cloakroom right before recess.</li>
            </ul>
            <h4>Clues:</h4>
            <ol>
                <li>The cardigan was last seen hanging on the third hook from the left.</li>
                <li>A faint trace of blue thread was found near the art supplies.</li>
                <li>Tommy’s locker was found unlocked.</li>
                <li>Sarah was spotted wearing a new cardigan after recess.</li>
                <li>Jake claims he was helping the teacher organize books.</li>
            </ol>
            <h4>Investigation Steps:</h4>
            <ul>
                <li>Interview suspects carefully.</li>
                <li>Check for any blue fibers on clothing.</li>
                <li>Search lockers and backpacks.</li>
                <li>Review classroom surveillance (if available).</li>
            </ul>
            <h4>Goal:</h4>
            <p>Use your little eye and detective skills to solve this cozy mystery!</p>
            <hr>
            <p style="font-style: italic;">Remember: every detail matters. Good luck, Detective!</p>
        </div>
        """, unsafe_allow_html=True)


with tab3:
    st.markdown("""
    <div style="
        font-family: 'Shadows Into Light', cursive;
        color: #333333;
        background: #fdf6e3;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.1);
        margin-top: 1rem;
        margin-bottom: 1rem;
    ">
        <h2 style="text-align: center;">🦎 Case File: The Angry Class Pet</h2>
        <p><strong>Location:</strong> Year 3 Classroom, Room 12B</p>
        <p><strong>Date:</strong> Thursday Morning</p>
        <p><strong>Reporting Officer:</strong> Detective Dotty</p>
        <hr style="margin: 1rem 0;" />
        <p><strong>Summary:</strong></p>
        <p>The class pet — a usually calm and contented bearded dragon named Ziggy — was found in an extremely agitated state after morning recess. Witnesses report hissing, tail-whipping, and aggressive glass tapping.</p>
        <p><strong>Suspected Cause:</strong> Possible unauthorized handling or environmental disturbance.</p>
        <p><strong>Clues:</strong></p>
        <ul>
            <li>An overturned water dish inside the terrarium</li>
            <li>A trail of lettuce leaves from the habitat to Leo's desk</li>
            <li>Missing 'Quiet Time' sign from the tank</li>
            <li>Finger smudges on the inside glass</li>
        </ul>
        <p><strong>Interviews:</strong></p>
        <ul>
            <li><em>Leo:</em> Claims he only "checked if Ziggy wanted to play chase".</li>
            <li><em>Ms. Barker:</em> Noticed Ziggy's heating lamp was unplugged.</li>
            <li><em>Amira:</em> Said she saw Leo giggling at the terrarium before recess ended.</li>
        </ul>
        <p><strong>Next Steps:</strong></p>
        <ol>
            <li>Review classroom CCTV (if available)</li>
            <li>Check lamp cord and outlet location</li>
            <li>Assign Ziggy some calm enrichment activities</li>
        </ol>
        <p><strong>Status:</strong> 🕵️‍♀️ Under investigation. Leo placed on "observe only" pet duty.</p>
    </div>
    """, unsafe_allow_html=True)
