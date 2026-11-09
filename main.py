import streamlit as st
import time
import random

# Set up page configurations with a premium mobile-responsive layout
st.set_page_config(page_title="The Grand Chandriya Empire v5", page_icon="👑", layout="centered")

# --- Initialize Interactive Game Session States ---
if "followers" not in st.session_state:
    st.session_state.followers = 1
if "shawarmas" not in st.session_state:
    st.session_state.shawarmas = 10
if "muttus_deployed" not in st.session_state:
    st.session_state.muttus_deployed = 0
if "messengers" not in st.session_state:
    st.session_state.messengers = 0
if "preach_count" not in st.session_state:
    st.session_state.preach_count = 0
if "achievements" not in st.session_state:
    st.session_state.achievements = []
if "luxury_unlocked" not in st.session_state:
    st.session_state.luxury_unlocked = []

# --- PREMIUM COHESIVE PASTEL CSS INJECTIONS ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    * { font-family: 'Quicksand', sans-serif; }
    
    .main-title { font-family: 'Fredoka One', cursive; font-size: 44px !important; font-weight: 800; color: #FF69B4; text-align: center; text-shadow: 2px 2px 0px #FFF; margin-bottom: 2px; }
    .subtitle { font-size: 15px !important; text-align: center; font-style: italic; color: #7B1FA2; font-weight: 700; margin-bottom: 25px; }
    
    .chat-bubble-goddess { background-color: #2A2A2A; color: #FFFFFF; padding: 14px 18px; border-radius: 20px 20px 20px 5px; margin: 10px 0px; border: 2px dashed #FF69B4; max-width: 85%; font-weight: 600; font-size: 0.95rem; }
    .chat-bubble-messenger { background-color: #F3E5F5; color: #4A148C; padding: 14px 18px; border-radius: 20px 20px 5px 20px; margin: 10px 0px; margin-left: auto; text-align: right; max-width: 85%; font-weight: 700; border: 2px dashed #B388FF; font-size: 0.95rem; }
    
    .luxury-card { background: linear-gradient(135deg, #FFF8E1 0%, #FFECB3 100%); border: 2px solid #FFC107; padding: 18px; border-radius: 16px; color: #FF8F00; font-weight: 700; margin: 12px 0px; box-shadow: 0 4px 12px rgba(0,0,0,0.02); text-align: center;}
    .locked-card { background: #F5F5F5; border: 2px dashed #BDBDBD; padding: 15px; border-radius: 16px; color: #757575; font-weight: 700; margin: 12px 0px; text-align: center; opacity: 0.6; }
    .memory-box { background: rgba(255, 255, 255, 0.85); border: 2px solid #E1BEE7; padding: 18px; border-radius: 18px; color: #4A148C; margin: 12px 0px; font-weight: 600; box-shadow: 0 4px 12px rgba(0,0,0,0.02); }
    .game-stat { background: #FFF0F5; border: 2px dashed #FF69B4; border-radius: 14px; padding: 12px; text-align: center; font-weight: 700; color: #7B1FA2; }
    
    .stTabs [data-baseweb="tab-list"] { gap: 6px; justify-content: center; }
    .stTabs [data-baseweb="tab"] { background-color: rgba(255, 255, 255, 0.6); border-radius: 20px; padding: 6px 16px; font-weight: 700; color: #7B1FA2; }
    
    .visual-bubble { font-size: 50px; text-align: center; margin: 10px 0; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">✨ CHANDRIYA EMPIRE V5 ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">👑 The Infinite Interactive Sandbox Portal. Ranked #2 in Life (Next to ChatGPT) 🤖</p>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📖 Scrapbook", "🧠 MBTI Riddle", "🎭 Diagnostics", "🌯 Altar Economy", "🎮 Cult Simulator"])

# ================= TAB 1: THE INTERACTIVE SCRAPBOOK =================
with tab1:
    st.write("### 📖 The Interactive Dialogue Playback Vault")
    st.caption("Select a chapter archive below to dynamically simulate your iconic chat histories:")
    
    chapter = st.selectbox("Select a Chapter Archive to display:", ["--- Select Chapter ---", "Chapter 1: The Great Escape 🚀", "Chapter 2: The Private Persona 🕵️‍♂️", "Chapter 3: The Malayalam Greetings 🙏", "Chapter 4: Sibling Contrasts 🛌"])
    
    if chapter == "Chapter 1: The Great Escape 🚀":
        st.markdown('<div class="chat-bubble-goddess">Hoiiii! Finally i can talk to you without ads bro....those ads were testimg my patience A LOT!!! 🤬</div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-bubble-messenger">Actually, the headache is, can\'t double text on the old setup! 😂</div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-bubble-goddess">Exactly!!! Inshtaa is way better layout. 🤭</div>', unsafe_allow_html=True)
    elif chapter == "Chapter 2: The Private Persona 🕵️‍♂️":
        st.markdown('<div class="chat-bubble-goddess">Im glad im glad im not judging u or anything. Its just that u r suchhhhhh a privare person. I like it. 😊</div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-bubble-goddess">This is my second acc thats correct. Wow....u r a very private person. 🤫</div>', unsafe_allow_html=True)
    elif chapter == "Chapter 3: The Malayalam Greetings 🙏":
        st.markdown('<div class="chat-bubble-messenger">Remember when I went to my uncle\'s house in Kerala, thought "Thalayoli" was a beautiful warm greeting, and folded my hands to a 40-year-old uncle? 🙏😭</div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-bubble-goddess">OMG STOP!!! Call the Bangalore police immediately, my lungs are giving up! 😭😂</div>', unsafe_allow_html=True)
    elif chapter == "Chapter 4: Sibling Contrasts 🛌":
        st.markdown('<div class="chat-bubble-messenger">My sister loves to travel but parents say no. My parents yell at me to go out, but I prefer staying in bed. 🛌</div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-bubble-goddess">Wow....great example of opposite siblings. Ur sister must be cursing u daily: "u r so lucky our parents tell u to go travel n u dont!" 😭✈️</div>', unsafe_allow_html=True)

# ================= TAB 2: ADVANCED MBTI RIDDLE BOARD =================
with tab2:
    st.write("### 🧠 The Advanced Live MBTI Matrix")
    st.caption("Adjust the interactive trait variables below to unlock real-time cryptographic clues:")
    
    t1 = st.slider("Trait Variable 1: Deep emotional processing level", 0, 100, 50)
    t2 = st.slider("Trait Variable 2: Level of irritation towards loud temple speakers", 0, 100, 50)
    
    if t1 > 80 and t2 > 80:
        st.info("💡 TRANSMISSION RECEIVED: \"Ok... I take things deeply. What's the opposite of I?\" -> The character string begins with 'E' and ends with 'J'!")
    else:
        st.caption("💡 Adjust both trait variable sliders above 80 to unlock her active cryptographic clues.")
        
    mbti_guess = st.text_input("Decode and enter her definitive 4-letter personality code string:", placeholder="Type code (e.g. ENTJ)...").strip().upper()
    
    if st.button("📡 Execute Deep Matrix Scan", use_container_width=True):
        if mbti_guess == "ENTJ":
            st.balloons()
            st.markdown('<div class="visual-bubble">👑✨💅👑🏎️</div>', unsafe_allow_html=True)
            st.success("🎉 CORE SYSTEM UNLOCKED! \"FINALLY!!! I am ENTJ! You calculated it perfectly! Im deeply impressed!\" 😎🔥")
        elif mbti_guess in ["INTP", "INFJ", "INFP", "INTJ"]:
            st.warning("🔮 \"Partially correct da! Just one or two characters u have to change! I won\'t reveal, chill!\" 🤭")
        else:
            st.error("❌ \"Now u r completely wrong!!! Try using your introverted intuition to guess!\"")

# ================= TAB 3: DIAGNOSTIC APPARATUS =================
with tab3:
    st.write("### 🎭 The Sibling & Aunt Therapy Diagnostic Simulator")
    st.caption("Toggle her active behavioral modes to run diagnostic interaction reports:")
    
    mode = st.radio("Select current active diagnostic state:", ["Ambi Core (Innocent Wisdom)", "Anniyan Mode (Punishing Single Status)", "Remo State (Peak Narcissism)"], horizontal=True)
    
    st.markdown('<div class="memory-box">', unsafe_allow_html=True)
    if mode == "Ambi Core (Innocent Wisdom)":
        st.markdown('<div class="chat-bubble-goddess">Pray to me n I\'ll listen! I shall make girls into ✨ wifey material ✨ N boys into ✨ husband material ✨. Trust in the system!</div>', unsafe_allow_html=True)
    elif mode == "Anniyan Mode (Punishing Single Status)":
        st.markdown('<div class="chat-bubble-messenger">But I don\'t even have a relationship problem! How can you solve it if I don\'t have one?! 🤔</div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-bubble-goddess" style="background: #B71C1C; border: 2px solid #FF8A80;">🚨 CRITICAL FAULT: You are a chronic walker whose hands talk so much you hit your own face! Go buy 10 shawarmas immediately! ⚔️</div>', unsafe_allow_html=True)
    elif mode == "Remo State (Peak Narcissism)":
        st.markdown('<div class="chat-bubble-goddess">"Whst will u do without me macha!? Tsk tsk... See I\'m so useful. See!" 😎✨</div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-bubble-messenger">Roger senpaaaiii 🫡</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("---")
    st.write("#### 👁️ Advanced Threat Simulations:")
    
    col_sim1, col_sim2 = st.columns(2)
    with col_sim1:
        if st.button("💥 Simulate past relationship mention", use_container_width=True):
            st.markdown('<div class="visual-bubble">👁️👊💥</div>', unsafe_allow_html=True)
            st.error("💥 PUNCH! \"But god have a terrible relationship experience, don't talk about it, she will hit your eye at anight!\" 👁️👊")
            st.info("🎯 Clinical Diagnostic Result: Your aunt definitely thinks she has more potential as a patient than a therapist! 😂")
    with col_sim2:
        if st.button("📸 Trigger dormant photography account", use_container_width=True):
            st.markdown('<div class="visual-bubble">🌅📷🌅</div>', unsafe_allow_html=True)
    
