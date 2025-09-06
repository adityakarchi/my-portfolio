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
        background-color: #111;
        color: #f2f2f2;
        line-height: 1.6;
        position: relative;
        font-family: 'Roboto', sans-serif;
        overflow: hidden;
        height: 100vh;
    }
    
    /* Animated falling lines background */
    .lines {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 100vh;
        margin: auto;
        width: 90vw;
        display: flex;
        justify-content: space-between;
        z-index: -1;
        pointer-events: none;
    }

    .line {
        position: relative;
        width: 1px;
        height: 100%;
        overflow: hidden;
    }

    .line::after {
        content: '';
        display: block;
        position: absolute;
        height: 15vh;
        width: 100%;
        top: -50%;
        left: 0;
        background: linear-gradient(to bottom, rgba(255, 255, 255, 0) 0%, #ffffff 75%, #ffffff 100%);
        animation: drop 7s 0s infinite;
        animation-fill-mode: forwards;
        animation-timing-function: cubic-bezier(0.4, 0.26, 0, 0.97);
    }

    /* Different colors for each line */
    .line:nth-child(1)::after {
        background: linear-gradient(to bottom, rgba(255, 69, 0, 0) 0%, #FF4500 75%, #FF4500 100%);
        animation-delay: 0.5s;
    }

    .line:nth-child(2)::after {
        background: linear-gradient(to bottom, rgba(50, 205, 50, 0) 0%, #32CD32 75%, #32CD32 100%);
        animation-delay: 1s;
    }

    .line:nth-child(3)::after {
        background: linear-gradient(to bottom, rgba(30, 144, 255, 0) 0%, #1E90FF 75%, #1E90FF 100%);
        animation-delay: 1.5s;
    }

    .line:nth-child(4)::after {
        background: linear-gradient(to bottom, rgba(255, 215, 0, 0) 0%, #FFD700 75%, #FFD700 100%);
        animation-delay: 2s;
    }

    .line:nth-child(5)::after {
        background: linear-gradient(to bottom, rgba(138, 43, 226, 0) 0%, #8A2BE2 75%, #8A2BE2 100%);
        animation-delay: 2.5s;
    }

    .line:nth-child(6)::after {
        background: linear-gradient(to bottom, rgba(32, 178, 170, 0) 0%, #20B2AA 75%, #20B2AA 100%);
        animation-delay: 3s;
    }

    .line:nth-child(7)::after {
        background: linear-gradient(to bottom, rgba(220, 20, 60, 0) 0%, #DC143C 75%, #DC143C 100%);
        animation-delay: 3.5s;
    }

    .line:nth-child(8)::after {
        background: linear-gradient(to bottom, rgba(0, 250, 154, 0) 0%, #00FA9A 75%, #00FA9A 100%);
        animation-delay: 4s;
    }

    .line:nth-child(9)::after {
        background: linear-gradient(to bottom, rgba(255, 20, 147, 0) 0%, #FF1493 75%, #FF1493 100%);
        animation-delay: 4.5s;
    }

    .line:nth-child(10)::after {
        background: linear-gradient(to bottom, rgba(0, 191, 255, 0) 0%, #00BFFF 75%, #00BFFF 100%);
        animation-delay: 5s;
    }

    @keyframes drop {
        0% {
            top: -50%;
        }
        100% {
            top: 110%;
        }
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
        margin-bottom: 45px;
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
    
    .skill-tag {
        display: inline-block;
        background: #14b8a6;
        color: white;
        padding: 0.3rem 0.8rem;
        margin: 0.2rem 0.3rem 0.2rem 0;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    .education-item {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-left: 4px solid #14b8a6;
        padding: 1.2rem;
        margin-bottom: 1rem;
        border-radius: 0 8px 8px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .energy-emoji {
        font-size: 1.5rem;
        cursor: pointer;
        margin-left: 0.5rem;
        width: 3rem;
        height: 3rem;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        transition: transform 0.2s ease;
    }
    
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
    # Add animated background lines
    st.markdown("""
    <div class="lines">
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
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
    st.markdown("""
    <div id="container">
        <div>Hello</div>
        <div id="flip">
            <div><div>English</div></div>
            <div><div>नमस्ते</div></div>
            <div><div>வணக்கம்</div></div>
            <div><div>నమస్కారం</div></div>
            <div><div>ನಮಸ್ಕಾರ</div></div>
            <div><div>നമസ്കാരം</div></div>
            <div><div>নমস্কার</div></div>
            <div><div>नमस्कार</div></div>
            <div><div>નમસ્તે</div></div>
            <div><div>ਸਤ ਸ੍ਰੀ ਅਕਾਲ</div></div>
            <div><div>ନମସ୍କାର</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
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
            
        with col_emoji:
            # Enhanced 3D-style avatar with CSS 3D transforms
            st.markdown("""
            <div style="text-align: center; margin-bottom: 1rem; perspective: 1000px;">
                <div class="avatar-3d" style="
                    width: 80px; 
                    height: 80px; 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 2.5rem;
                    box-shadow: 
                        0 8px 16px rgba(0,0,0,0.4),
                        0 0 0 4px #14b8a6,
                        0 0 0 8px rgba(20, 184, 166, 0.3);
                    margin: 0 auto;
                    animation: rotate3d 6s linear infinite;
                    transform-style: inherit;
                    position: relative;
                ">
                    <div style="
                        position: absolute;
                        width: 100%;
                        height: 100%;
                        background: radial-gradient(circle at 30% 30%, rgba(255,255,255,1.0), transparent 25%);
                        border-radius: 50%;
                        pointer-events: none;
                    "></div>
                    ❤️
                </div>
            </div>
            
            <style>
                @keyframes rotate3d {
                    0% { 
                        transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg);
                        box-shadow: 
                            0 8px 16px rgba(0,0,0,0.4),
                            0 0 0 4px #14b8a6,
                            0 0 0 8px rgba(20, 184, 166, 0.3);
                    }
                    25% { 
                        transform: rotateX(15deg) rotateY(90deg) rotateZ(0deg);
                        box-shadow: 
                            -8px 8px 16px rgba(0,0,0,0.4),
                            0 0 0 4px #ff6b6b,
                            0 0 0 8px rgba(255, 107, 107, 0.3);
                    }
                    50% { 
                        transform: rotateX(0deg) rotateY(180deg) rotateZ(15deg);
                        box-shadow: 
                            0 -8px 16px rgba(0,0,0,0.4),
                            0 0 0 4px #4ecdc4,
                            0 0 0 8px rgba(78, 205, 196, 0.3);
                    }
                    75% { 
                        transform: rotateX(-15deg) rotateY(270deg) rotateZ(0deg);
                        box-shadow: 
                            8px 8px 16px rgba(0,0,0,0.4),
                            0 0 0 4px #45b7d1,
                            0 0 0 8px rgba(69, 183, 209, 0.3);
                    }
                    100% { 
                        transform: rotateX(0deg) rotateY(360deg) rotateZ(0deg);
                        box-shadow: 
                            0 8px 16px rgba(0,0,0,0.4),
                            0 0 0 4px #14b8a6,
                            0 0 0 8px rgba(20, 184, 166, 0.3);
                    }
                }
                
                .avatar-3d:hover {
                    animation-duration: 3s;
                    transform: scale(1.1);
                }
            </style>
            """, unsafe_allow_html=True)
            
            # Create animated emoji button
            current_emoji = energy_emojis[st.session_state.emoji_index]
            
            # Custom styled emoji button with animation
            st.markdown(f"""
            <style>
                .emoji-button {{
                    font-size: 2rem;
                    background: none;
                    border: none;
                    cursor: pointer;
                    width: 3rem;
                    height: 3rem;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    border-radius: 50%;
                    transition: all 0.3s ease;
                    animation: wipe-enter 1s ease-out;
                }}
                .emoji-button:hover {{
                    transform: scale(1.2);
                    background: rgba(20, 184, 166, 0.1);
                }}
            </style>
            <div style="text-align: center;">
                <span class="emoji-button emoji-animation">{current_emoji}</span>
            </div>
            """, unsafe_allow_html=True)
            
            # # Hidden button for functionality
            if st.button("Change Energy", key="emoji_btn", help="Click to change energy level"):
                st.session_state.emoji_index = (st.session_state.emoji_index + 1) % len(energy_emojis)
                st.rerun()
        
        st.markdown("""
        <div class="description">
            A curious student who loves building things with code! I'm passionate about systems programming 
            . Currently looking for internships where I can learn, contribute, 
            and maybe break some code along the way!!!!!
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
                🔗 <a href="{contact_info['github']}" style="text-decoration: none; color: #14b8a6;" target="_blank">GitHub</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_education():
    st.markdown('<div class="section-header">🎓 Education</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="education-item">
        <h3 style="color: #1e293b; font-weight: 600; margin-bottom: 0.5rem;">{education_info['institution']}</h3>
        <p style="color: #475569; margin-bottom: 0.3rem;">{education_info['degree']}</p>
        <p style="color: #64748b; font-size: 0.9rem;">{education_info['duration']}</p>
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
    frameworks_tools = ["open-cv", "streamlit","machine-learning"]
    concepts = ["Data Structures & Algorithms", "Terminal Applications"]
    
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
    <div style="background: #f8fafc; padding: 2rem; border-radius: 10px; text-align: center;">
        <p style="color: #475569; margin-bottom: 1.5rem; font-size: 1.1rem;">
            I'm always open to discussing new opportunities, interesting projects, or just having a chat about technology!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📧 Send me an Email", use_container_width=True):
            st.markdown(f'<meta http-equiv="refresh" content="0;url=mailto:{contact_info["email"]}">', unsafe_allow_html=True)

def render_footer():
    st.markdown("---")
    
    # Resume download section
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0 1rem 0;">
        <h4 style="color: #f2f2f2; margin-bottom: 1rem;">📄 Download Resume</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Center the download button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            with open("resume.pdf", "rb") as file:
                btn = st.download_button(
                    label="📥 Download Resume",
                    data=file,
                    file_name="ADITYA_KARCHI_Resume.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    help="Download my resume as PDF"
                )
        except FileNotFoundError:
            st.error("Resume file not found. Please add resume.pdf to the project folder.")
    
    st.markdown(f"""
    <div style="text-align: center; color: #64748b; font-size: 0.9rem; margin-top: 2rem;">
        <p>Built with ❤️ using Streamlit • © {datetime.now().year} ADITYA KARCHI</p>
        <p style="font-size: 0.8rem; margin-top: 0.5rem;">
            my-projects: <a href="https://github.com/adityakarchii" style="color: #14b8a6; text-decoration: none;">GitHub Profile</a>
        </p>
    </div>
    """, unsafe_allow_html=True)



if __name__ == "__main__":
    
    main()
