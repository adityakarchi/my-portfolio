import streamlit as st
import time
from datetime import datetime
from data import greetings, projects, skills, education_info, contact_info
import base64

# Configure the page
st.set_page_config(
    page_title="ADITYA KARCHI - Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css?family=Roboto:700');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box !important;
    }
    
    .stApp {
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        color: #f2f2f2;
        line-height: 1.6;
        position: relative;
        font-family: 'Roboto', sans-serif;
        overflow: hidden;
        min-height: 100vh;
    }
    
    /* Space Celestial Background */
    .space-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        overflow: hidden;
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
    }

    /* Stars */
    .stars {
        position: absolute;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, #eee, transparent),
            radial-gradient(2px 2px at 40px 70px, rgba(255,255,255,0.8), transparent),
            radial-gradient(1px 1px at 90px 40px, #fff, transparent),
            radial-gradient(1px 1px at 130px 80px, rgba(255,255,255,0.6), transparent),
            radial-gradient(2px 2px at 160px 30px, #ddd, transparent);
        background-repeat: repeat;
        background-size: 200px 100px;
        animation: sparkle 20s linear infinite;
    }

    @keyframes sparkle {
        from { transform: translateX(0); }
        to { transform: translateX(200px); }
    }

    /* Planets */
    .planet {
        position: absolute;
        border-radius: 50%;
        animation: orbit 60s linear infinite;
    }

    .planet1 {
        width: 80px;
        height: 80px;
        background: radial-gradient(circle at 30% 30%, #ff6b6b, #c92a2a);
        top: 20%;
        left: 10%;
        animation: orbit1 80s linear infinite;
        box-shadow: 0 0 20px rgba(255, 107, 107, 0.3);
    }

    .planet2 {
        width: 60px;
        height: 60px;
        background: radial-gradient(circle at 30% 30%, #4ecdc4, #20b2aa);
        top: 60%;
        right: 15%;
        animation: orbit2 100s linear infinite reverse;
        box-shadow: 0 0 15px rgba(78, 205, 196, 0.3);
    }

    .planet3 {
        width: 40px;
        height: 40px;
        background: radial-gradient(circle at 30% 30%, #ffd93d, #ff6b35);
        top: 80%;
        left: 70%;
        animation: orbit3 120s linear infinite;
        box-shadow: 0 0 10px rgba(255, 217, 61, 0.3);
    }

    @keyframes orbit1 {
        from { transform: rotate(0deg) translateX(100px) rotate(0deg); }
        to { transform: rotate(360deg) translateX(100px) rotate(-360deg); }
    }

    @keyframes orbit2 {
        from { transform: rotate(0deg) translateX(80px) rotate(0deg); }
        to { transform: rotate(360deg) translateX(80px) rotate(-360deg); }
    }

    @keyframes orbit3 {
        from { transform: rotate(0deg) translateX(60px) rotate(0deg); }
        to { transform: rotate(360deg) translateX(60px) rotate(-360deg); }
    }

    /* Shooting Stars */
    .shooting-star {
        position: absolute;
        height: 2px;
        background: linear-gradient(to right, rgba(255,255,255,0), rgba(255,255,255,1), rgba(255,255,255,0));
        border-radius: 2px;
        animation: shoot 8s linear infinite;
    }

    .shooting-star:nth-child(1) {
        width: 150px;
        top: 10%;
        left: -150px;
        animation-delay: 0s;
    }

    .shooting-star:nth-child(2) {
        width: 100px;
        top: 30%;
        left: -100px;
        animation-delay: 4s;
    }

    .shooting-star:nth-child(3) {
        width: 80px;
        top: 70%;
        left: -80px;
        animation-delay: 2s;
    }

    @keyframes shoot {
        0% { transform: translateX(0) translateY(0); }
        100% { transform: translateX(calc(100vw + 200px)) translateY(-200px); }
    }

    /* Nebula Effect */
    .nebula {
        position: absolute;
        width: 300px;
        height: 300px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(138, 43, 226, 0.1), rgba(75, 0, 130, 0.05), transparent);
        top: 40%;
        right: 20%;
        animation: pulse 15s ease-in-out infinite;
    }

    .nebula2 {
        position: absolute;
        width: 200px;
        height: 200px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(30, 144, 255, 0.1), rgba(0, 191, 255, 0.05), transparent);
        top: 10%;
        left: 60%;
        animation: pulse 20s ease-in-out infinite reverse;
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.3; }
        50% { transform: scale(1.2); opacity: 0.6; }
    }

    /* Asteroid Belt */
    .asteroid {
        position: absolute;
        background: #8b7d6b;
        border-radius: 50%;
        animation: float 30s linear infinite;
    }

    .asteroid1 {
        width: 4px;
        height: 4px;
        top: 25%;
        left: 30%;
        animation-delay: 0s;
    }

    .asteroid2 {
        width: 6px;
        height: 6px;
        top: 45%;
        left: 80%;
        animation-delay: 5s;
    }

    .asteroid3 {
        width: 3px;
        height: 3px;
        top: 75%;
        left: 20%;
        animation-delay: 10s;
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }
    
    /* Flip Text Animation Styles */
    #container {
        color: #989;
        text-transform: uppercase;
        font-size: 36px;
        font-weight: bold;
        padding-top: 50px;  
        position: relative;
        width: 100%;
        display: block;
        text-align: right;
        margin-bottom: 2rem;
    }

    #flip {
        height: 40px;
        overflow: hidden;
    }

    #flip > div > div {
        color: #fff;
        padding: 2px 10px;
        height: 50px;
        margin-bottom: 45px;git
        display: inline-block;
        border-radius: 8px;
        min-width: 100px;
        text-align: center;
    }

    #flip div:first-child {
        animation: showGreetings 10s linear infinite;
    }

    /* Different background colors for each greeting */
    #flip div:nth-child(1) div { background: #4ec7f3; } /* English - Blue */
    #flip div:nth-child(2) div { background: #ff6b6b; } /* Hindi - Red */
    #flip div:nth-child(3) div { background: #4ecdc4; } /* Tamil - Teal */
    #flip div:nth-child(4) div { background: #45b7d1; } /* Telugu - Sky Blue */
    #flip div:nth-child(5) div { background: #96ceb4; } /* Kannada - Mint */
    #flip div:nth-child(6) div { background: #ffeaa7; } /* Malayalam - Yellow */
    #flip div:nth-child(7) div { background: #dda0dd; } /* Bengali - Plum */
    #flip div:nth-child(8) div { background: #98d8c8; } /* Marathi - Seafoam */
    #flip div:nth-child(9) div { background: #f7dc6f; } /* Gujarati - Gold */
    #flip div:nth-child(10) div { background: #bb8fce; } /* Punjabi - Lavender */
    #flip div:nth-child(11) div { background: #85c1e9; } /* Odia - Light Blue */

    @keyframes showGreetings {
        0% { margin-top: -495px; }
        4.5% { margin-top: -450px; }
        9% { margin-top: -450px; }
        13.5% { margin-top: -405px; }
        18% { margin-top: -405px; }
        22.5% { margin-top: -360px; }
        27% { margin-top: -360px; }
        31.5% { margin-top: -315px; }
        36% { margin-top: -315px; }
        40.5% { margin-top: -270px; }
        45% { margin-top: -270px; }
        49.5% { margin-top: -225px; }
        54% { margin-top: -225px; }
        58.5% { margin-top: -180px; }
        63% { margin-top: -180px; }
        67.5% { margin-top: -135px; }
        72% { margin-top: -135px; }
        76.5% { margin-top: -90px; }
        81% { margin-top: -90px; }
        85.5% { margin-top: -45px; }
        90% { margin-top: -45px; }
        94.5% { margin-top: 0px; }
        99.99% { margin-top: 0px; }
        100% { margin-top: -495px; }
    }
    
    .main {
        padding: 2rem;
        max-width: 800px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
    }
    
    .greeting-container {
        font-size: 2rem;
        color: #14b8a6;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .name-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #f2f2f2;
        margin-bottom: 0.5rem;
    }
    
    .description {
        font-size: 1.1rem;
        color: #d1d5db;
        line-height: 1.6;
        margin-bottom: 2rem;
    }
    
    .contact-info {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin-bottom: 3rem;
        font-size: 0.9rem;
        color: #9ca3af;
    }
    
    .contact-item {
        display: flex;
        align-items: center;
        gap: 0.3rem;
    }
    
    .section-header {
        font-size: 1.3rem;
        font-weight: 600;
        color: #f2f2f2;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #14b8a6;
    }
    
    .project-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        border-left: 4px solid #14b8a6;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .project-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #f2f2f2;
        margin-bottom: 0.3rem;
    }
    
    .project-year {
        font-size: 0.9rem;
        color: #9ca3af;
        float: right;
        background: rgba(255, 255, 255, 0.1);
        padding: 0.2rem 0.6rem;
        border-radius: 15px;
    }
    
    .project-description {
        color: #d1d5db;
        margin-bottom: 1rem;
        font-style: italic;
    }
    
 @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap'); /* Changed weight to 700 for better impact */

.skill-tag {
    /* Base Style */
    display: inline-block;
    color: white;
    padding: 0.5rem 1.1rem; /* Slightly larger padding */
    margin: 0.4rem 0.5rem 0.4rem 0;
    border-radius: 30px; /* More rounded */
    font-size: 0.9rem;
    font-weight: 700; /* Bold text */
    font-family: 'Montserrat', sans-serif;
    letter-spacing: 1px;
    cursor: pointer;
    
    /* 3D-like Background and Border */
    background: linear-gradient(135deg, #FF7B6C, #E14434); /* Brighter start, deeper end */
    border: 2px solid rgba(255, 255, 255, 0.5); /* Inner highlight/shine */
    
    /* Stronger Shadow for Depth (The 'Floating' Effect) */
    box-shadow: 
        0 8px 15px rgba(0, 0, 0, 0.4), /* Deep, blurred drop shadow for elevation */
        inset 0 0 10px rgba(255, 255, 255, 0.3), /* Subtle inner light/shine */
        inset 0 -5px 5px rgba(0, 0, 0, 0.2); /* Inner bottom shadow for convexity */
    
    /* Animation Setup */
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); /* Smoother, more dynamic transition */
    
    /* Add 'perspective' if you want to use true 3D transforms on a parent container */
    /* transform-style: preserve-3d; */
}

/* --- */

/* Hover animation (The 'Pop-out' Effect) */
.skill-tag:hover {
    /* Scale and Translate for a strong "pop" */
    transform: 
        translateY(-5px) /* Lift higher */
        scale(1.1);    /* Scale up more dramatically */
        /* You could also try 'rotateX(5deg) rotateY(5deg)' for a tilt effect */

    /* Change Gradient on Hover for a 'Pulsing' Effect */
    background: linear-gradient(135deg, #FF998A, #F55D4E); /* Shift to a slightly different hue/brightness */

    /* Enhanced Shadow for 'Closer' Look */
    box-shadow: 
        0 15px 25px rgba(0, 0, 0, 0.5), /* Deeper shadow when lifted */
        inset 0 0 15px rgba(255, 255, 255, 0.4), /* Stronger inner light */
        inset 0 -8px 8px rgba(0, 0, 0, 0.3); /* Stronger inner shadow */
}

/* --- */

/* Optional: Adding a small press/active state for completeness */
.skill-tag:active {
    transform: translateY(0) scale(0.98);
    box-shadow: 
        0 2px 5px rgba(0, 0, 0, 0.3), /* Flat shadow when pressed */
        inset 0 0 5px rgba(0, 0, 0, 0.3);
}
    
    .education-item {
        background: rgba(255, 251, 222, 0.1);
        backdrop-filter: blur(10px);
        border-left: 4px solid #B6CEB4;
        padding: 1.2rem;
        margin-bottom: 1rem;
        border-radius: 0 8px 8px 0;
        border: 1px solid rgba(255, 251, 222, 0.1);
    }
    
    # .energy-emoji {
    #     font-size: 1.5rem;
    #     cursor: pointer;
    #     margin-left: 0.5rem;
    #     width: 3rem;
    #     height: 3rem;
    #     display: inline-flex;
    #     align-items: center;
    #     justify-content: center;
    #     border-radius: 50%;
    #     transition: transform 0.2s ease;
    # }
    
    @keyframes wipe-enter {
        0% {
            transform: scale(0);
        }
        50% {
            transform: scale(1.2);
        }
        100% {
            transform: scale(1);
        }
    }
    
    @media (prefers-reduced-motion: no-preference) {
        .emoji-animation {
            animation: wipe-enter 1s 1;
        }
    }
    
    .energy-emoji:hover {
        transform: scale(1.1);
    }
    
    .stButton button {
        background: #14b8a6;
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Add space celestial background
    st.markdown("""
    <div class="space-background">
        <!-- Stars -->
        <div class="stars"></div>
        
        <!-- Planets -->
        <div class="planet planet1"></div>
        <div class="planet planet2"></div>
        <div class="planet planet3"></div>
        
        <!-- Shooting Stars -->
        <div class="shooting-star"></div>
        <div class="shooting-star"></div>
        <div class="shooting-star"></div>
        
        <!-- Nebula Effects -->
        <div class="nebula"></div>
        <div class="nebula2"></div>
        
        <!-- Asteroids -->
        <div class="asteroid asteroid1"></div>
        <div class="asteroid asteroid2"></div>
        <div class="asteroid asteroid3"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state for greeting rotation and emoji
    if 'greeting_index' not in st.session_state:
        st.session_state.greeting_index = 0
    if 'emoji_index' not in st.session_state:
        st.session_state.emoji_index = 0
    if 'last_greeting_update' not in st.session_state:
        st.session_state.last_greeting_update = time.time()
    
    # Auto-rotate greetings every 3 seconds
    current_time = time.time()
    if current_time - st.session_state.last_greeting_update > 3:
        st.session_state.greeting_index = (st.session_state.greeting_index + 1) % len(greetings)
        st.session_state.last_greeting_update = current_time
        st.rerun()
    
    # Header Section
    render_header()
    
    # Main content
    render_education()
    render_projects()
    render_skills()
    render_contact()
    render_footer()

def render_header():
    # Add animated flip text with all languages
    # st.markdown("""
    # <div id="container">
    #     <div>Hello</div>
    #     <div id="flip">
    #         <div><div>English</div></div>
    #         <div><div>नमस्ते</div></div>
    #         <div><div>வணக்கம்</div></div>
    #         <div><div>నమస్కారం</div></div>
    #         <div><div>ನಮಸ್ಕಾರ</div></div>
    #         <div><div>നമസ്കാരം</div></div>
    #         <div><div>নমস্কার</div></div>
    #         <div><div>नमस्कार</div></div>
    #         <div><div>નમસ્તે</div></div>
    #         <div><div>ਸਤ ਸ੍ਰੀ ਅਕਾਲ</div></div>
    #         <div><div>ନମସ୍କାର</div></div>
    #     </div>
    # </div>
    # """, unsafe_allow_html=True)
    
    # Greeting with auto-rotation
    current_greeting = greetings[st.session_state.greeting_index]
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"""
        <div class="greeting-container">
            {current_greeting['text']} <span style="font-size: 0.7em; color: #64748b;">({current_greeting['lang']})</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Interactive emoji click
        energy_emojis = ["😄", "😎", "🙂", "😐", "😶", "😒", "😔", "😫", "😩", "😴"]
        
        col_name, col_emoji = st.columns([4, 1])
        with col_name:
            st.markdown('<div class="name-title">I\'m ADITYA K</div>', unsafe_allow_html=True)
            
        # with col_emoji:
        #     # Enhanced 3D-style avatar with CSS 3D transforms
        #     st.markdown("""
        #     <div style="text-align: center; margin-bottom: 1rem; perspective: 1000px;">
        #         <div class="avatar-3d" style="
        #             width: 80px; 
        #             height: 80px; 
        #             background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        #             border-radius: 50%;
        #             display: flex;
        #             align-items: center;
        #             justify-content: center;
        #             font-size: 2.5rem;
        #             box-shadow: 
        #                 0 8px 16px rgba(0,0,0,0.4),
        #                 0 0 0 4px #14b8a6,
        #                 0 0 0 8px rgba(20, 184, 166, 0.3);
        #             margin: 0 auto;
        #             animation: rotate3d 6s linear infinite;
        #             transform-style: inherit;
        #             position: relative;
        #         ">
        #             <div style="
        #                 position: absolute;
        #                 width: 100%;
        #                 height: 100%;
        #                 background: radial-gradient(circle at 30% 30%, rgba(255,255,255,1.0), transparent 25%);
        #                 border-radius: 50%;
        #                 pointer-events: none;
        #             "></div>
        #             ❤️
        #         </div>
        #     </div>
            
        #     <style>
        #         @keyframes rotate3d {
        #             0% { 
        #                 transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg);
        #                 box-shadow: 
        #                     0 8px 16px rgba(0,0,0,0.4),
        #                     0 0 0 4px #14b8a6,
        #                     0 0 0 8px rgba(20, 184, 166, 0.3);
        #             }
        #             25% { 
        #                 transform: rotateX(15deg) rotateY(90deg) rotateZ(0deg);
        #                 box-shadow: 
        #                     -8px 8px 16px rgba(0,0,0,0.4),
        #                     0 0 0 4px #ff6b6b,
        #                     0 0 0 8px rgba(255, 107, 107, 0.3);
        #             }
        #             50% { 
        #                 transform: rotateX(0deg) rotateY(180deg) rotateZ(15deg);
        #                 box-shadow: 
        #                     0 -8px 16px rgba(0,0,0,0.4),
        #                     0 0 0 4px #4ecdc4,
        #                     0 0 0 8px rgba(78, 205, 196, 0.3);
        #             }
        #             75% { 
        #                 transform: rotateX(-15deg) rotateY(270deg) rotateZ(0deg);
        #                 box-shadow: 
        #                     8px 8px 16px rgba(0,0,0,0.4),
        #                     0 0 0 4px #45b7d1,
        #                     0 0 0 8px rgba(69, 183, 209, 0.3);
        #             }
        #             100% { 
        #                 transform: rotateX(0deg) rotateY(360deg) rotateZ(0deg);
        #                 box-shadow: 
        #                     0 8px 16px rgba(0,0,0,0.4),
        #                     0 0 0 4px #14b8a6,
        #                     0 0 0 8px rgba(20, 184, 166, 0.3);
        #             }
        #         }
                
        #         .avatar-3d:hover {
        #             animation-duration: 3s;
        #             transform: scale(1.1);
        #         }
        #     </style>
        #     """, unsafe_allow_html=True)
            
            # Create animated emoji button
            current_emoji = energy_emojis[st.session_state.emoji_index]
            
            # Custom styled emoji button with animation
            # st.markdown(f"""
            # <style>
            #     .emoji-button {{
            #         font-size: 2rem;
            #         background: none;
            #         border: none;
            #         cursor: pointer;
            #         width: 3rem;
            #         height: 3rem;
            #         display: flex;
            #         align-items: center;
            #         justify-content: center;
            #         border-radius: 50%;
            #         transition: all 0.3s ease;
            #         animation: wipe-enter 1s ease-out;
            #     }}
            #     .emoji-button:hover {{
            #         transform: scale(1.2);
            #         background: rgba(20, 184, 166, 0.1);
            #     }}
            # </style>
            # <div style="text-align: center;">
            #     <span class="emoji-button emoji-animation">{current_emoji}</span>
            # </div>
            # """, unsafe_allow_html=True)
            
            # # # Hidden button for functionality
            # if st.button("Change Energy", key="emoji_btn", help="Click to change energy level"):
            #     st.session_state.emoji_index = (st.session_state.emoji_index + 1) % len(energy_emojis)
            #     st.rerun()
        
        st.markdown("""
        <div class="description">
            Third-year engineering student at BMS Institute of Technology and Management with strong interests in machine learning, deep learning, NLP, and generative AI. Experienced in projects such as gesture recognition,visual-try-on, showcasing both technical knowledge and practical application. Got an opportunity to participate in Khelo India to represent my district and college, reflecting discipline, commitment, and teamwork.
 Focused on continuous learning, skill development, and preparing for placements.
        </div>
        """, unsafe_allow_html=True)
        
        # Contact info
        st.markdown(f"""
        <div class="contact-info">
            <div class="contact-item">
                📧 <a href="mailto:{contact_info['email']}" style="text-decoration: none; color: #14b8a6;">{contact_info['email']}</a>
            </div>
            <div class="contact-item">
                📍 {contact_info['location']}
            </div>
            <div class="contact-item">
                🔗 <a href="{contact_info['github']}" style="text-decoration: linear; color: #14b8a6;" target="_blank">GitHub</a>
            </div>
            <div class="contact-item">
                🔗 <a href="{contact_info['linkden']}" style="text-decoration: bold; color: #14b8a6;" target="_blank">Linkden</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_education():
    st.markdown('<div class="section-header">🎓 Education</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="education-item">
        <h3 style="color: #f7f3f2; font-weight: 600; margin-bottom: 0.75rem;">{education_info['institution']}</h3>
        <p style="color: #EEEFE0; margin-bottom: 0.3rem;">{education_info['degree']}</p>
        <p style="color: #F2F2F2; font-size: 0.9rem;">{education_info['duration']}</p>
    </div>
    """, unsafe_allow_html=True)

def render_projects():
    st.markdown('<div class="section-header">💻 Projects</div>', unsafe_allow_html=True)
    
    for project in projects:
        tech_tags = ''.join([f'<span class="skill-tag">{tech}</span>' for tech in project['tech']])
        
        details_html = ''.join([f'<li style="margin-bottom: 0.5rem;">{detail}</li>' for detail in project['details']])
        
        st.markdown(f"""
        <div class="project-card">
            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
                <div class="project-title">{project['title']}</div>
                <div class="project-year">{project['year']}</div>
            </div>
            <div class="project-description">{project['description']}</div>
            <ul style="color: #475569; margin: 1rem 0; padding-left: 1.2rem;">
                {details_html}
            </ul>
            <div style="margin-top: 1rem;">
                {tech_tags}
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_skills():
    st.markdown('<div class="section-header">🛠️ Skills & Technologies</div>', unsafe_allow_html=True)
    
    # Group skills into categories
    programming_languages = ["C++","Python","SQL",]
    frameworks_tools = ["Open-CV", "Streamlit","Tensorflow"]
    concepts = ["Data Structures & Algorithms",
        "Data Preprocessing",
        "Data Visualization",
        "Deep Learning",
        "NLP",
        "Generative AI",
        "Terminal Applications",
        "Machine-Learning"]
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Programming Languages**")
        for skill in programming_languages:
            if skill in [s['name'] for s in skills]:
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("**Frameworks & Tools**")
        for skill in frameworks_tools:
            if skill in [s['name'] for s in skills]:
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    with col3:
        st.markdown("**Concepts & Others**")
        for skill in concepts:
            if skill in [s['name'] for s in skills]:
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

def render_contact():
    st.markdown('<div class="section-header">📬 Get In Touch</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: #154D71; padding: 2rem; border-radius: 10px; text-align: center;">
        <p style="color: #AE75DA; margin-bottom: 1.5rem; font-size: 1.1rem;">
            I'm always open to discussing new opportunities, interesting projects, or just having a chat about technology!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📧 Send me an Email", use_container_width=True):
            st.markdown(f'<meta http-equiv="refresh" content="0;url=mailto:{contact_info["email"]}">', unsafe_allow_html=True)

import streamlit as st
from datetime import datetime

# Initialize session state for the button click if it doesn't exist
if 'resume_download_clicked' not in st.session_state:
    st.session_state['resume_download_clicked'] = False

def render_footer():
    st.markdown("---")
    
    # Resume download section
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0 1rem 0;">
        <h4 style="color: #f2f2f2; margin-bottom: 1rem;">📄 Download Resume</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Define a callback function to set the state
    def set_download_clicked():
        st.session_state['resume_download_clicked'] = True

    # Center the download button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            with open("resume.pdf", "rb") as file:
                
                # Check the state to determine button appearance
                if st.session_state['resume_download_clicked']:
                    # Display the 'Success' button style (tick mark)
                    btn_label = "✅ Download Complete"
                    btn_help = "You have already downloaded the resume."
                    btn_disabled = True # Disable re-clicking
                else:
                    # Display the standard 'Download' button
                    btn_label = "📥 Download Resume"
                    btn_help = "Download my resume as PDF"
                    btn_disabled = False

                btn = st.download_button(
                    label=btn_label,
                    data=file,
                    file_name="ADITYA-KARCHI_Resume.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    help=btn_help,
                    on_click=set_download_clicked, # Use the callback on click
                    disabled=btn_disabled
                )
        except FileNotFoundError:
            st.error("Resume file not found. Please add resume.pdf to the project folder.")
    
    # Existing footer text
    st.markdown(f"""
    <div style="text-align: center; color: #64748b; font-size: 0.9rem; margin-top: 2rem;">
        <p>Built with ❤️ using Streamlit • © {datetime.now().year} ADITYA KARCHI</p>
        <p style="font-size: 0.8rem; margin-top: 0.5rem;">
            my-projects: <a href="https://github.com/adityakarchii" style="color: #14b8a6; text-decoration: none;">GitHub Profile</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

# Example of how you'd call the function
# render_footer()

if __name__ == "__main__":
    
    main()
