import streamlit as st
import random

# Configure page
st.set_page_config(
    page_title="For My Amazing Girlfriend ❤️",
    page_icon="💕",
    layout="centered"
)

# Hide streamlit interface completely
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;}
div[data-testid="stToolbar"] {visibility: hidden;}
div[data-testid="stDecoration"] {visibility: hidden;}
div[data-testid="stStatusWidget"] {visibility: hidden;}
#stDecoration {display:none;}
.css-h5rgaw {display:none;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Beautiful romantic styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        padding: 20px;
    }
    
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
    }
    
    .love-title {
        font-size: 4em;
        color: #d63384;
        text-align: center;
        font-family: cursive;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        margin: 30px 0;
        animation: heartbeat 2s ease-in-out infinite;
    }
    
    .message-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin: 20px auto;
        max-width: 800px;
        text-align: center;
        border: 3px solid #ff69b4;
    }
    
    .love-text {
        font-size: 1.3em;
        color: #495057;
        line-height: 1.8;
        margin: 20px 0;
    }
    
    .heart-divider {
        font-size: 2em;
        text-align: center;
        margin: 30px 0;
        color: #ff69b4;
    }
    
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    
    .floating-hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1000;
    }
    
    .heart {
        position: absolute;
        color: #ff69b4;
        font-size: 25px;
        animation: float 8s linear infinite;
    }
    
    @keyframes float {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
    }
</style>

<div class="floating-hearts">
    <div class="heart" style="left: 10%; animation-delay: 0s;">💖</div>
    <div class="heart" style="left: 25%; animation-delay: 2s;">💕</div>
    <div class="heart" style="left: 40%; animation-delay: 4s;">💗</div>
    <div class="heart" style="left: 55%; animation-delay: 6s;">💝</div>
    <div class="heart" style="left: 70%; animation-delay: 8s;">💖</div>
    <div class="heart" style="left: 85%; animation-delay: 10s;">💕</div>
</div>
""", unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="love-title">To My Beautiful Girlfriend 💕</h1>', unsafe_allow_html=True)

st.markdown("""
<div class="message-box">
    <h2 style="color: #d63384; margin-bottom: 25px;">You Are My Everything 💖</h2>
    
    <p class="love-text">
    From the moment you walked into my life, everything changed for the better. 
    Your smile lights up my darkest days, your laugh is my favorite sound, 
    and your love gives me strength I never knew I had.
    </p>
    
    <p class="love-text">
    You're not just my girlfriend - you're my best friend, my partner in crime, 
    my safe haven, and my greatest adventure all in one amazing person.
    </p>
    
    <h3 style="color: #ff1493; margin: 30px 0;">I LOVE YOU SO MUCH! 💕</h3>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="heart-divider">💖 💕 💗 💝 💖 💕 💗 💝 💖</div>', unsafe_allow_html=True)

# Interactive section
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💕 Love Note", use_container_width=True):
        love_notes = [
            "You are the reason I believe in love 💖",
            "My heart skips a beat every time I see you 💓",
            "You're my favorite notification 📱💕",
            "I fall for you more and more every day 🥰",
            "You're my sunshine on cloudy days ☀️",
            "With you, I'm home 🏠💕"
        ]
        st.success(random.choice(love_notes))

with col2:
    if st.button("🎵 Our Song", use_container_width=True):
        songs = [
            "🎵 'Perfect' by Ed Sheeran",
            "🎵 'All of Me' by John Legend", 
            "🎵 'Thinking Out Loud'",
            "🎵 'A Thousand Years'",
            "🎵 'Can't Help Myself'"
        ]
        st.info(random.choice(songs))

with col3:
    if st.button("🤗 Virtual Hug", use_container_width=True):
        st.balloons()
        st.success("Sending you the biggest hug! 🤗💕")

# Reasons why I love you
st.markdown("""
<div class="message-box">
    <h3 style="color: #d63384;">Why I Love You 💕</h3>
    <p class="love-text">💖 Your beautiful smile that brightens my entire day</p>
    <p class="love-text">💖 The way you laugh at my terrible jokes</p>
    <p class="love-text">💖 How you always know exactly what to say</p>
    <p class="love-text">💖 Your kindness and caring heart</p>
    <p class="love-text">💖 The way you support my dreams</p>
    <p class="love-text">💖 How you make ordinary moments magical</p>
</div>
""", unsafe_allow_html=True)

# Final message
st.markdown("""
<div class="message-box">
    <h2 style="color: #d63384;">Thank You For Being YOU 💖</h2>
    <p class="love-text">
    Thank you for loving me, supporting me, and making life so much brighter. 
    You're my person, my love, my everything.
    </p>
    <h1 style="color: #ff1493; font-size: 2.5em;">I LOVE YOU! 💕💕💕</h1>
    <p style="font-style: italic; color: #6c757d;">- Your boyfriend who adores you 😘</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="heart-divider">💖💕💗💝💖💕💗💝💖💕💗💝💖</div>', unsafe_allow_html=True)