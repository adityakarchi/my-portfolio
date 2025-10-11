import streamlit as st
import time
from datetime import datetime
# Ensure data.py is in the same directory as this file
from data import greetings, projects, skills, education_info, contact_info
import base64

# Configure the page
st.set_page_config(
    page_title="ADITYA KARCHI - Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling (Space Theme and Flip Animation)
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
        text-align: left;
        margin-bottom: 2rem;
    }

    #flip {
        height: 45px; /* Adjusted height to fit the inner div height */
        overflow: hidden;
        display: flex;
    }

    #flip > div {
        animation: showGreetings 12s ease-in-out infinite;
    }

    #flip > div > div {
        color: #fff;
        padding: 2px 10px;
        height: 45px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 8px;
        min-width: 120px;
        text-align: center;
    }

    /* Background colors (matched to the number of greetings in the flip structure) */
    #flip div:nth-child(1) div:nth-child(1) { background: #4ec7f3; }
    #flip div:nth-child(1) div:nth-child(2) { background: #ff6b6b; } 
    #flip div:nth-child(1) div:nth-child(3) { background: #4ecdc4; }
    #flip div:nth-child(1) div:nth-child(4) { background: #45b7d1; }
    #flip div:nth-child(1) div:nth-child(5) { background: #96ceb4; }
    #flip div:nth-child(1) div:nth-child(6) { background: #ffeaa7; }
    #flip div:nth-child(1) div:nth-child(7) { background: #dda0dd; }
    #flip div:nth-child(1) div:nth-child(8) { background: #98d8c8; } 
    #flip div:nth-child(1) div:nth-child(9) { background: #f7dc6f; }
    #flip div:nth-child(1) div:nth-child(10) { background: #bb8fce; }
    #flip div:nth-child(1) div:nth-child(11) { background: #85c1e9; }

    @keyframes showGreetings {
        0% { margin-top: 0; }
        8.3% { margin-top: 0; } /* 100% / 12 items (11 greetings + 1 return) */
        16.6% { margin-top: -45px; }
        24.9% { margin-top: -90px; }
        33.2% { margin-top: -135px; }
        41.5% { margin-top: -180px; }
        49.8% { margin-top: -225px; }
        58.1% { margin-top: -270px; }
        66.4% { margin-top: -315px; }
        74.7% { margin-top: -360px; }
        83% { margin-top: -405px; }
        91.3% { margin-top: -450px; }
        100% { margin-top: 0; }
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
    
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');

    .skill-tag {
        /* Base Style */
        display: inline-block;
        color: white;
        padding: 0.5rem 1.1rem; 
        margin: 0.4rem 0.5rem 0.4rem 0;
        border-radius: 30px; 
        font-size: 0.9rem;
        font-weight: 700; 
        font-family: 'Montserrat', sans-serif;
        letter-spacing: 1px;
        cursor: pointer;
        
        /* 3D-like Background and Border */
        background: linear-gradient(135deg, #FF7B6C, #E14434); 
        border: 2px solid rgba(255, 255, 255, 0.5); 
        
        /* Stronger Shadow for Depth (The 'Floating' Effect) */
        box-shadow: 
            0 8px 15px rgba(0, 0, 0, 0.4),
            inset 0 0 10px rgba(255, 255, 255, 0.3), 
            inset 0 -5px 5px rgba(0, 0, 0, 0.2); 
        
        /* Animation Setup */
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }

    /* Hover animation (The 'Pop-out' Effect) */
    .skill-tag:hover {
        /* Scale and Translate for a strong "pop" */
        transform: 
            translateY(-5px)
            scale(1.1);

        /* Change Gradient on Hover for a 'Pulsing' Effect */
        background: linear-gradient(135deg, #FF998A, #F55D4E);

        /* Enhanced Shadow for 'Closer' Look */
        box-shadow: 
            0 15px 25px rgba(0, 0, 0, 0.5), 
            inset 0 0 15px rgba(255, 255, 255, 0.4),
            inset 0 -8px 8px rgba(0, 0, 0, 0.3); 
    }

    /* Optional: Adding a small press/active state for completeness */
    .skill-tag:active {
        transform: translateY(0) scale(0.98);
        box-shadow: 
            0 2px 5px rgba(0, 0, 0, 0.3),
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
        transition: all 0.3s ease-in-out;
    }
    
    .stButton button:hover {
        background: #0d9488;
        box-shadow: 0 4px 15px rgba(20, 184, 166, 0.4);
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
    
    # Initialize session state for emoji (greeting rotation now handled by CSS animation)
    if 'emoji_index' not in st.session_state:
        st.session_state.emoji_index = 0
    
    # Wrap the main content in a container to respect the max-width set in CSS
    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    # Header Section
    render_header()
    
    # Main content
    render_education()
    render_projects()
    render_skills()
    render_contact()
    render_footer()
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_header():
    # Add animated flip text with all languages
    st.markdown("""
    <div id="container">
        <div id="flip">
            <div>
                <div>Hello</div>
                <div>नमस्ते</div>
                <div>வணக்கம்</div>
                <div>నమస్కారం</div>
                <div>ನಮಸ್ಕಾರ</div>
                <div>നമസ്കാരം</div>
                <div>নমস্কার</div>
                <div>नमस्कार</div>
                <div>નમસ્તે</div>
                <div>ਸਤ ਸ੍ਰੀ ਅਕਾਲ</div>
                <div>ନମସ୍କାର</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown('<div class="name-title">I\'m ADITYA KARCHI 😄</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="description">
            Third-year engineering student at BMS Institute of Technology and Management with strong interests in Machine Learning, Deep Learning, NLP, and Generative AI. Experienced in projects such as gesture recognition, visual-try-on, showcasing both technical knowledge and practical application. Got an opportunity to participate in Khelo India to represent my district and college, reflecting discipline, commitment, and teamwork. Focused on continuous learning, skill development, and preparing for placements.
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
            <div class="contact-item">
                🔗 <a href="{contact_info['linkden']}" style="text-decoration: none; color: #14b8a6;" target="_blank">LinkedIn</a>
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
        # Generate skill tags with custom styling
        tech_tags = ''.join([f'<span class="skill-tag">{tech}</span>' for tech in project['tech']])
        
        # Format details list
        details_html = ''.join([f'<li style="margin-bottom: 0.5rem; color: #d1d5db;">{detail}</li>' for detail in project['details']])
        
        st.markdown(f"""
        <div class="project-card">
            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
                <div class="project-title">{project['title']}</div>
                <div class="project-year">{project['year']}</div>
            </div>
            <div class="project-description">{project['description']}</div>
            <ul style="margin: 1rem 0; padding-left: 1.2rem;">
                {details_html}
            </ul>
            <div style="margin-top: 1rem;">
                {tech_tags}
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_skills():
    st.markdown('<div class="section-header">🛠️ Skills & Technologies</div>', unsafe_allow_html=True)
    
    # Group skills based on what's defined in the mock data (for consistency)
    programming_languages = ["C++", "Python", "SQL"]
    frameworks_tools = ["Open-CV", "Streamlit", "Tensorflow"]
    concepts = [
        "Data Structures & Algorithms",
        "Data Preprocessing", 
        "Data Visualization",
        "DeepLearning",
        "NLP",
        "Generative AI",
        "Machine-Learning"
    ]
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Programming Languages**")
        for skill in programming_languages:
            # Check if skill exists in the overall list (defined in data.py)
            if any(s['name'] == skill for s in skills):
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("**Frameworks & Tools**")
        for skill in frameworks_tools:
            if any(s['name'] == skill for s in skills):
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    with col3:
        st.markdown("**Concepts & Others**")
        for skill in concepts:
            if any(s['name'] == skill for s in skills):
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

def render_contact():
    st.markdown('<div class="section-header">📬 Get In Touch</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(5px); padding: 2rem; border-radius: 10px; text-align: left; border: 1px solid rgba(255, 255, 255, 0.2);">
        <p style="color: #f2f2f2; margin-bottom: 1.5rem; font-size: 1.3rem;">
            I'm always open to discussing new opportunities, interesting projects, or just having a chat about technology!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Use a hidden markdown element to trigger the mailto link upon button press
        if st.button("📧 Send me an Email", use_container_width=True):
            st.markdown(f'<meta http-equiv="refresh" content="0;url=mailto:{contact_info["email"]}">', unsafe_allow_html=True)

# Initialize session state for the button click if it doesn't exist
if 'resume_download_clicked' not in st.session_state:
    st.session_state['resume_download_clicked'] = False

def render_footer():
    st.markdown("<hr style='border-top: 1px solid #374151;'>", unsafe_allow_html=True)
    
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
        # --- RESUME HANDLING NOTE ---
        # The following block attempts to open 'resume.pdf'.
        # You must place your resume.pdf file in the same folder as this script to avoid an error.
        # I've kept the original error handling for resilience.
        # --------------------------
        try:
            with open("resume.pdf", "rb") as file:
                
                # Check the state to determine button appearance
                if st.session_state['resume_download_clicked']:
                    # Display the 'Success' button style (tick mark)
                    btn_label = "✅ Download Complete"
                    btn_help = "Thank you for reviewing my qualifications!"
                    btn_disabled = True # Disable re-clicking
                else:
                    # Display the standard 'Download' button
                    btn_label = "📥 Download Resume"
                    btn_help = "Download my resume as PDF"
                    btn_disabled = False

                st.download_button(
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
            st.error("⚠️ Resume file 'resume.pdf' not found. Please add the file to the project folder to enable download.")
    
    # Existing footer text
    st.markdown(f"""
    <div style="text-align: center; color: #64748b; font-size: 0.9rem; margin-top: 2rem;">
        <p>Built with ❤️ using Streamlit • © {datetime.now().year} ADITYA KARCHI</p>
        <p style="font-size: 0.8rem; margin-top: 0.5rem;">
            my-projects: <a href="https://github.com/adityakarchi" style="color: #14b8a6; text-decoration: none;">GitHub Profile</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
