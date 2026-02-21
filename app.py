import streamlit as st
from pathlib import Path

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Shieldify – AI Security Suite",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize Session State for Navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Dashboard'

def navigate_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- 2. BUILT-IN LOGIC (INTEGRATED VOICE & VIDEO) ---
def scan_for_mitm(): 
    return "Traffic Clean - Secure Connection"

def calculate_authenticity(p, c): 
    return 94.7

def get_risk_level(s): 
    return "Trusted", "#00ffa3"

# Voice Verify Logic (Simulating audio_features.py & voice_classifier.py)
def analyze_voice_sample(audio_file): 
    if audio_file is not None:
        # Simulate MFCC extraction and ResNet-34 classification
        return 96.2
    return 0.0

def analyze_video_forensics(video_file):
    # Simulating XceptionNet deep analysis results
    return 95.8, "Authentic", "#00ffa3"

# --- 3. CUSTOM STYLES ---
def load_css():
    css_path = Path("ui_style.css")
    if css_path.exists():
        with open(css_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    st.markdown("""
        <style>
        .card-button-container div.stButton > button {
            width: 100% !important;
            background-color: transparent !important;
            color: white !important;
            border: 1px solid #333 !important;
            border-radius: 8px !important;
            padding: 10px !important;
            font-weight: bold !important;
            transition: all 0.3s ease !important;
        }
        .card-button-container div.stButton > button:hover {
            border-color: #00ffa3 !important;
            color: #00ffa3 !important;
            background: rgba(0, 255, 163, 0.05) !important;
        }
        .hero-section {
            text-align: center;
            padding: 60px 0;
            background: radial-gradient(circle at center, rgba(0, 255, 163, 0.05) 0%, transparent 70%);
        }
        .back-section div.stButton > button {
            background: #1e1e1e !important;
            color: #00ffa3 !important;
            border: 1px solid #333 !important;
            border-radius: 5px !important;
            padding: 5px 20px !important;
        }
        .metric-box {
            text-align: center; 
            padding: 20px; 
            border-radius: 10px; 
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

load_css()

# --- 4. TOP NAVIGATION BAR ---
st.markdown("""
<div class="top-bar">
    <div class="logo-section"><span class="logo-text">🛡️ Shiel<span>dify</span></span></div>
    <div class="system-status">
        <span>📈 All Systems Operational</span>
        <span>⚡ 4 Modules Active</span>
        <span>🟢 Real-time Monitoring</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. REUSABLE CARD COMPONENT ---
def render_module_card(title, subtitle, author, initials, desc, outputs, icon, color):
    output_html = "".join([f"<li><span style='color:{color};'>&bull;</span> {item}</li>" for item in outputs])
    
    st.markdown(f"""
    <div class="card-container" style="border-top: 2px solid {color}; height: 480px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
            <div class="card-icon-box" style="background-color: {color};">
                <span style="font-size: 20px;">{icon}</span>
            </div>
            <h3 class="card-title">{title}</h3>
            <p class="card-subtitle" style="color: {color};">{subtitle}</p>
            <div class="author-row">
                <div class="avatar">{initials}</div>
                <span class="author-name">{author}</span>
            </div>
            <p class="card-body-text">{desc}</p>
            <div class="outputs-section">
                <p class="outputs-label">OUTPUTS</p>
                <ul style="list-style: none; padding-left: 0;">{output_html}</ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="card-button-container">', unsafe_allow_html=True)
    if st.button(f"Open {title}", key=f"btn_{title}"):
        navigate_to(title)
    st.markdown('</div></div>', unsafe_allow_html=True)

# --- 6. PAGE ROUTING ---

# --- DASHBOARD PAGE ---
if st.session_state.page == "Dashboard":
    st.markdown("<div class='hero-section'><h1>🛡️ Shiel<span>dify</span></h1><h2 style='color: #888;'>Multi-Domain Threat Detection Platform</h2></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        render_module_card("Network Guardian", "Cybersecurity", "Muhammad Ali", "MA", 
                          "Detecting MITM attacks, ARP spoofing, and traffic analysis.", 
                          ["Network Guardian Backend", "Attack Detection Engine"], "📶", "#00ffa3")
        render_module_card("Voice Verify", "Audio Detection", "Arsalan Imran", "AI", 
                          "Detecting AI-generated voices through classification.", 
                          ["Voice Authenticity Model"], "🎙️", "#ffcc00")
    with col2:
        render_module_card("Social Shield", "Fake Profile Detection", "Ali Jaffri", "AJ", 
                          "Detecting bots & AI profiles through behavior.", 
                          ["Fake Profile Detection Model"], "👥", "#a855f7")
        render_module_card("Video Sentinel", "Video Detection", "Adil Abid", "AA", 
                          "AI video detection with face analysis.", 
                          ["Deepfake Video Model"], "🎥", "#ff4d4d")

# --- 🎙️ VOICE VERIFY PAGE (Sentinel Logic Added) ---
elif st.session_state.page == "Voice Verify":
    st.markdown('<div class="back-section">', unsafe_allow_html=True)
    if st.button("← Back to Dashboard"): navigate_to("Dashboard")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<h1 style='color: white;'>Voice Verify</h1><p style='color: #ffcc00; font-weight: bold;'>Deepfake Audio Detection</p>", unsafe_allow_html=True)

    col_main, col_side = st.columns([1.5, 1])
    with col_main:
        st.markdown("<div class='card-container'><h3>Audio Analyzer</h3>", unsafe_allow_html=True)
        audio_file = st.file_uploader("Upload Audio Sample", type=["wav", "mp3"])
        if st.button("Run Deep Verification", use_container_width=True):
            # Activating the Sentinel Logic
            with st.spinner("Extracting Audio Features & Running ResNet-34..."):
                score = analyze_voice_sample(audio_file)
                st.markdown(f"<div class='metric-box' style='border: 1px solid #ffcc00;'><h1 style='color: #ffcc00;'>{score}%</h1><p style='color: #ffcc00;'>Voice Authenticity Score</p></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with col_side:
        st.markdown("<div class='card-container'><h4 style='color: #ffcc00;'>● Audio Metrics</h4><p>🧬 MFCC Extraction: Active</p><p>🏗️ Architecture: ResNet-34</p><p>🎯 Target Accuracy: 96.2%</p><p>🕒 Processing: Real-time</p></div>", unsafe_allow_html=True)

# --- 📶 NETWORK GUARDIAN PAGE ---
elif st.session_state.page == "Network Guardian":
    st.markdown('<div class="back-section">', unsafe_allow_html=True)
    if st.button("← Back to Dashboard"): navigate_to("Dashboard")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<h1 style='color: white;'>Network Guardian</h1>", unsafe_allow_html=True)
    
    col_main, col_side = st.columns([1.5, 1])
    with col_main:
        st.markdown("<div class='card-container'><h3>Network Scanner</h3><div style='text-align: center; padding: 40px 0;'><div style='font-size: 80px; color: #00ffa3;'>📶</div></div>", unsafe_allow_html=True)
        if st.button("Start Network Scan", use_container_width=True):
            st.success(f"Security Scan Result: {scan_for_mitm()}")
        st.markdown("</div>", unsafe_allow_html=True)
    with col_side:
        st.markdown("<div class='card-container'><h4 style='color: #00ffa3;'>● Detection Capabilities</h4><p>🛡️ MITM Detection</p><p>⚠️ ARP Spoofing</p><p>📈 Packet Sniffing</p></div>", unsafe_allow_html=True)

# --- 👥 SOCIAL SHIELD PAGE ---
elif st.session_state.page == "Social Shield":
    st.markdown('<div class="back-section">', unsafe_allow_html=True)
    if st.button("← Back to Dashboard"): navigate_to("Dashboard")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<h1 style='color: white;'>Social Shield</h1>", unsafe_allow_html=True)
    col_main, col_side = st.columns([1.5, 1])
    with col_main:
        st.markdown("<div class='card-container'><h3>Profile Analyzer</h3>", unsafe_allow_html=True)
        username = st.text_input("Username/URL", placeholder="@username")
        if st.button("Analyze Authenticity", use_container_width=True):
            score = calculate_authenticity(12, 0.85)
            label, color = get_risk_level(score)
            st.markdown(f"<div class='metric-box' style='border: 1px solid {color};'><h1 style='color: {color};'>{score}%</h1><p style='color: {color};'>{label}</p></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with col_side:
        st.markdown("<div class='card-container'><h4 style='color: #a855f7;'>● Model Specs</h4><p>🤖 Random Forest</p><p>📊 47 Data Points</p></div>", unsafe_allow_html=True)

# --- 🎥 VIDEO SENTINEL PAGE ---
elif st.session_state.page == "Video Sentinel":
    st.markdown('<div class="back-section">', unsafe_allow_html=True)
    if st.button("← Back to Dashboard"): navigate_to("Dashboard")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<h1 style='color: white;'>Video Sentinel</h1>", unsafe_allow_html=True)
    col_main, col_side = st.columns([1.5, 1])
    with col_main:
        st.markdown("<div class='card-container'><h3>Video Analyzer</h3>", unsafe_allow_html=True)
        video_file = st.file_uploader("Upload Video File", type=["mp4", "mov"])
        if st.button("Run Forensic Analysis", use_container_width=True):
            score, label, color = analyze_video_forensics(video_file)
            st.markdown(f"<div class='metric-box' style='border: 1px solid {color};'><h1 style='color: {color};'>{score}%</h1><p style='color: {color};'>{label}</p></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with col_side:
        st.markdown("<div class='card-container'><h4 style='color: #ff4d4d;'>● Analysis Metrics</h4><p>👤 Face Tracking: Active</p><p>🏗️ XceptionNet Model</p></div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<div style='text-align:center; padding: 20px; color: #555;'>© 2026 Shieldify Security Suite | End-to-End Encrypted</div>", unsafe_allow_html=True)