import streamlit as st
import random

# Configure page
st.set_page_config(
    page_title="Soumya a.k.a. Somzilla ❤️",
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
st.markdown('<h1 class="love-title">Soumya a.k.a. Somzilla 💕</h1>', unsafe_allow_html=True)

st.markdown("""
<div style="font-size:18px; line-height:1.6; color:#ffefff; background-color:#1e1e2f; padding:20px; border-radius:10px;">
    Hey my Goddess,<br><br>

    I don’t even know where to start, so I’ll just say this:<br>
    You’re kinda stuck with me now. Forever. Sorry. Too late. Can’t escape. Dumbass move loving me but also the best one you ever made 😎<br><br>

    You’ve got this annoying habit of making my whole day better just by existing. I don’t even get how you do that. Like, I’ll be dying, and then boom — one "hey" from you and I’m smiling like an idiot.<br><br>

    You’re chaos, you're sweet, you're dramatic as hell, and you're mine.<br><br>

    I love the way you talk, the way you type like you’re half-asleep, the way you call me out and still stay, and the way you make me feel like I actually matter to someone.<br><br>

    Sometimes I scroll through our chats just to feel that again. Sometimes I miss you even when we’ve just talked.<br><br>

    I don’t say this stuff every day, but I swear on everything — I mean it. You make life better. For real.<br><br>

    So here’s a tiny dumb website to say what I usually mess up saying in texts:<br>
    You’re everything. You’re mine. You’re amazing. You’re loved.<br><br>

    …And yes, you’re stuck with me now. No returns. No refunds. Good luck. 😌<br><br>

    – sam · my lil baddie 🫶
</div>
""", unsafe_allow_html=True)

    
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="heart-divider">❤️ 💖 💘 💝 💗 💓 💞 💕 💟</div>', unsafe_allow_html=True)

# Interactive section
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💕 From the Heart", use_container_width=True):
        love_notes = [
            "You are the reason I believe in love 💖",
            "You're my favorite notification 📱💕",
            "I fall for you more and more every day 🥰",
            "You're my sunshine on cloudy days ☀️",
        ]
        st.success(random.choice(love_notes))

with col2:
    st.markdown("""
        <style>
        .custom-button {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            background-color: #ff69b4;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .custom-button:hover {
            background-color: #ff85c1;
        }
        </style>
        <a href="https://open.spotify.com/playlist/3fvp6A6BMDnBWUYNEgKeFp?si=f6Z4krQNTvSxeoL04JQlKw" target="_blank">
            <button class="custom-button">🎵 Our Song</button>
        </a>
    """, unsafe_allow_html=True)

with col3:
    if st.button("🤗 Virtual Hug", use_container_width=True):
        st.balloons()
        st.success("Sending you the biggest hug! 🤗💕")

# Reasons why I love you
st.markdown("""
<div class="message-box">
    <h3 style="color: #d63384;">Why I Love You 💕</h3>
    <p class="love-text">💖 Your beautiful smile that brightens my entire day</p>
    <p class="love-text">💖 you're MY chaos and I wouldn't want it any other way</p>
    <p class="love-text">💖 How you always know exactly what to say</p>
    <p class="love-text">💖 Your kindness and caring heart</p>
    <p class="love-text">💖 Because even when you say ‘stfu’ or roast me for no reason, I still think you’re the cutest person alive</p>
    <p class="love-text">💖 How you make ordinary moments magical</p>
</div>
""", unsafe_allow_html=True)

# Final message
st.markdown("""
<div class="message-box">
    <h2 style="color: #d63384;">Soumya-isms 💖</h2>
    <ul class="love-text">
    <li>Nap queen behavior 💤</li>
    <li>Random voice notes at <span style="color: #ff9ecb;">2am</span></li>
    <li>Calling me broski and then being cute 5 seconds later 😵‍💫</li>
</ul>
    
    <h1 style="color: #ff1493; font-size: 2.5em;">I LOVE YOU! 💕💕💕</h1>
    <p style="font-style: italic; color: #6c757d;">- Too late to run now.You picked me, suffer 😘</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="heart-divider">🐻 🐼 🐨 🐶 🐱 🐰 🦄 🐣 🎈</div>', unsafe_allow_html=True)
