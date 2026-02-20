import streamlit as st
from pathlib import Path

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Shieldify – AI Security Suite",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. COMPONENTS ---
def render_module_card(title, subtitle, author, initials, desc, outputs, icon, color):
    # Fixed bullet points using HTML entities to avoid encoding errors (â€¢ fix)
    output_html = "".join([f"<li><span style='color:{color};'>&bull;</span> {item}</li>" for item in outputs])
    
    return f"""
    <div class="card-container" style="border-top: 2px solid {color};">
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
            <ul>{output_html}</ul>
        </div>
        <div class="card-footer">
            <span class="status-indicator">&bull;</span> <span class="status-text">Active</span>
        </div>
    </div>
    """

def load_css():
    css_path = Path("ui_style.css")
    if css_path.exists():
        with open(css_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize Styles
load_css()

# --- 3. TOP NAVIGATION BAR ---
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

# --- 4. SIDEBAR NAVIGATION ---
menu = st.sidebar.radio("Go to", ["Dashboard", "Network Guardian", "Social Shield", "Voice Verify", "Video Sentinel"])

# --- 5. DASHBOARD PAGE ---
if menu == "Dashboard":
    # Hero Section with Centered Content
    st.markdown("""
    <div class="hero-section">
        <div class="orbit-container">
            <div class="orbit-circle circle-1"></div>
            <div class="orbit-circle circle-2"></div>
            <div class="main-glow-logo"><h1>🛡️ Shiel<span>dify</span></h1></div>
        </div>
        <h2 class="hero-title">Multi-Domain Threat Detection Platform</h2>
        <p class="hero-desc">
            Advanced AI-powered security suite protecting against network attacks, 
            deepfakes, fake profiles, and audio manipulation in real-time.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Architecture Header
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; margin-bottom: 40px;">
        <p style="color: #00ffa3; font-size: 12px; letter-spacing: 2px; font-weight: bold; margin-bottom: 5px;">🛡️ DETECTION MODULES</p>
        <h1 style="font-size: 34px; margin-top: 0;">Multi-Layer Security Architecture</h1>
    </div>
    """, unsafe_allow_html=True)

    # 2-Column Grid Layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(render_module_card(
            "Network Guardian", "Cybersecurity", "Muhammad Ali", "MA", 
            "Detection of MITM attacks, ARP spoofing, and secure traffic analysis.", 
            ["Network Guardian Backend", "Attack Detection Engine", "Security Reports"], 
            "📶", "#00ffa3"
        ), unsafe_allow_html=True)
        
        st.markdown(render_module_card(
            "Voice Verify", "Audio Detection", "Arsalan Imran", "AI", 
            "Detecting AI-generated voices through advanced classification algorithms.", 
            ["Voice Authenticity Model", "Real vs Fake Probability Score"], 
            "🎙️", "#ffcc00"
        ), unsafe_allow_html=True)
        
    with col2:
        st.markdown(render_module_card(
            "Social Shield", "Fake Profile Detection", "Ali Jaffri", "AJ", 
            "Detecting bots & AI profiles through behavioral analysis.", 
            ["Fake Profile Detection Model", "ML Classification Engine"], 
            "👥", "#a855f7"
        ), unsafe_allow_html=True)
        
        st.markdown(render_module_card(
            "Video Sentinel", "Video Detection", "Adil Abid", "AA", 
            "AI video detection with face manipulation analysis.", 
            ["Deepfake Video Model", "Real-time Video Scanning"], 
            "🎥", "#ff4d4d"
        ), unsafe_allow_html=True)

# --- 6. FOOTER ---
st.markdown("""
<div class="footer-container">
    <span>🛡️ Shieldify v1.0.0</span>
    <span>🔒 End-to-End Encrypted | 📂 Open Source</span>
    <span>© 2026 Shieldify Security Suite</span>
</div>
""", unsafe_allow_html=True)