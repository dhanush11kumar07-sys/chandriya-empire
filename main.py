import streamlit as st
import time
import random

st.set_page_config(page_title="The Grand Chandriya Empire", page_icon="👑", layout="centered")

# --- CUSTOM STYLE LAYOUT (INJECTED VIA STREAMLIT) ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    * { font-family: 'Quicksand', sans-serif; }
    
    .main-title { font-family: 'Fredoka One', cursive; font-size: 42px !important; font-weight: 800; color: #FF69B4; text-align: center; text-shadow: 2px 2px 0px #FFF; margin-bottom: 2px; }
    .subtitle { font-size: 15px !important; text-align: center; font-style: italic; color: #7B1FA2; font-weight: 700; margin-bottom: 25px; }
    
    .chat-bubble-goddess { background-color: #2A2A2A; color: #FFFFFF; padding: 14px 18px; border-radius: 20px 20px 20px 5px; margin: 10px 0px; border: 1px solid #444; max-width: 85%; font-weight: 600; }
    .chat-bubble-messenger { background-color: #BA55D3; color: white; padding: 14px 18px; border-radius: 20px 20px 5px 20px; margin: 10px 0px; margin-left: auto; text-align: right; max-width: 85%; font-weight: 600; }
    
    .luxury-card { background: linear-gradient(135deg, #FFF8E1 0%, #FFECB3 100%); border-left: 5px solid #FFC107; padding: 18px; border-radius: 16px; color: #FF8F00; font-weight: 700; margin: 12px 0px; box-shadow: 0 4px 10px rgba(0,0,0,0.02); }
    .memory-box { background: #F3E5F5; border-left: 5px solid #B388FF; padding: 15px; border-radius: 14px; color: #4A148C; margin: 12px 0px; font-weight: 600; }
    
    .stTabs [data-baseweb="tab-list"] { gap: 8px; justify-content: center; }
    .stTabs [data-baseweb="tab"] { background-color: rgba(255, 255, 255, 0.6); border-radius: 20px; padding: 6px 18px; font-weight: 700; }
    
    /* Kawaii Visual Bubble Element CSS */
    .visual-bubble { font-size: 50px; text-align: center; animation: floatUp 2s ease-in-out infinite alternate; margin: 10px 0; }
    @keyframes floatUp { from { transform: translateY(0px); } to { transform: translateY(-10px); } }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">✨ CHANDRIYA EMPIRE ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Exsctly ✨ Inshtaa ✨ Sponsored. Ranked #2 in Life (Next to ChatGPT) 🤖</p>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📖 Friendship Chronicles", "🧠 MBTI Game Matrix", "🎭 The Face-Punch Oracle", "💎 Luxury Altar"])

with tab1:
    st.write("### 📖 The Origin Vault")
    st.caption("A premium digital monument of how this whole chaos expanded.")
    st.markdown('<div class="memory-box">🚀 <strong>Chapter 1: The Great Escape</strong><br>"Finally i can talk to you without ads bro....those ads were testimg my patience A LOT!!!" — Escaping the messaging app matrix to live on Instagram.</div>', unsafe_allow_html=True)
    st.markdown('<div class="memory-box">🕵️‍♂️ <strong>Chapter 2: The Private Persona Discovery</strong><br>"Im glad im glad im not judging u or anything. Its just that u r suchhhhhh a privare person. I like it. 😊"</div>', unsafe_allow_html=True)
    st.markdown('<div class="memory-box">🙏 <strong>Chapter 3: The Innocent Malayalam Greetings</strong><br>Going to an uncle\'s house in Kerala, thinking "Thalayoli" meant a warm friendly welcome, and greeting a 40-year-old uncle with folded hands! 😂</div>', unsafe_allow_html=True)
    st.markdown('<div class="memory-box">🎆 <strong>Chapter 4: Peak Sibling Joy</strong><br>"FIREWORRRKKSSS!!!!!!!! ✨❤️ HAPPY HAPPY HAPPY!!! ~" paired with custom cat emojis! 🐱❤️</div>', unsafe_allow_html=True)

with tab2:
    st.write("### 🧠 The Interactive MBTI Personality Grid")
    st.caption("\"In mbti what clue i shud give da.... ok... i take things deeply. What\'s the opposite of I?\"")
    mbti_guess = st.text_input("Guess the exact 4-letter personality type of the Goddess:", placeholder="Type here...").strip().upper()
    if st.button("📡 Decode Personality String", use_container_width=True):
        if mbti_guess == "ENTJ":
            st.balloons()
            st.markdown('<div class="visual-bubble">👑✨🥳👑</div>', unsafe_allow_html=True)
            st.success("🎉 FINALLY!!! I am ENTJ! You unlocked her true form! Im impressed! 😎✨")
        elif mbti_guess in ["INTP", "INFJ", "INFP"]:
            st.warning("🔮 \"Partially correct da! Just one character u have to change! I won\'t reveal, chill!\" 🤭")
        else:
            st.error("❌ \"Now u r completely wrong!!! 😂 Try using your introverted intuition to guess!\"")

with tab3:
    st.write("### 🎭 The Multi-Personality Oracle Booth")
    st.caption("Warning: \"Your aunt may hink she has more potential as a patient than a therapist.\" 😂")
    personality = st.selectbox("Select current active Goddess mood state:", ["Ambi Mode (Innocent)", "Anniyan Mode (Punishment)", "Remo Mode (Peak Narcissism)"])
    st.write("---")
    if personality == "Ambi Mode (Innocent)":
        st.markdown('<div class="chat-bubble-goddess">I will make girls into ✨ wifey material ✨ N boys into ✨ husband material ✨. Pray to Goddess Chandini!</div>', unsafe_allow_html=True)
    elif personality == "Anniyan Mode (Punishment)":
        st.markdown('<div class="chat-bubble-messenger">I don\'t have a relationship problem! How can you solve it if I don\'t have one?!</div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-bubble-goddess" style="background: #C62828;">🚨 ANNIYAN JUDGMENT: You are a chronic walker whose hands do the talking! Go buy 10 shawarmas instantly! ⚔️</div>', unsafe_allow_html=True)
    elif personality == "Remo Mode (Peak Narcissism)":
        st.markdown('<div class="chat-bubble-goddess">"Whst will u do without me macha!? Tsk tsk... See, I\'m so useful." 😎</div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-bubble-messenger">Roger senpaaaiii 🫡</div>', unsafe_allow_html=True)
    st.write("---")
    if st.button("❌ Mention her past relationship experience", use_container_width=True):
        st.markdown('<div class="visual-bubble">👁️👊💥</div>', unsafe_allow_html=True)
        st.error("💥 PUNCH! \"But god have a terrible relationship experience, don\'t talk about it, she will hit your eye at anight!\" 👁️👊")

with tab4:
    st.write("### 🌯 The Luxury Altar Economy")
    st.caption("System Ratio Law: 10 Shawarmas = 1 Drop of Relationship Guidance.")
    shawarmas = st.slider("Select how many Shawarmas you are sacrificing today:", 0, 50, 10)
    if st.button("🔥 Place Sacrifices Upon Altar", use_container_width=True):
        if shawarmas < 10:
            st.error("🚨 INSUFFICIENT PRASAADHAM! The Goddess demands chunks of 10 or she will deploy the slipper shot!")
        else:
            tokens = shawarmas // 10
            st.balloons()
            st.success(f"🎉 TRANSACTION SECURED! You earned {tokens} Advice Tokens!")
            
            st.write("---")
            st.write("#### 💎 The Luxury Daydream Wishlist Unlocked:")
            
            st.markdown('<div class="luxury-card">🧼 Tier 1 Daydream: Having a good bubble bath in a luxury bathtub</div>', unsafe_allow_html=True)
            st.markdown('<div class="visual-bubble">🛁🧼🫧🛀🫧🧼🛁</div>', unsafe_allow_html=True)
            
            if tokens >= 2: 
                st.markdown('<div class="luxury-card">👠 Tier 2 Daydream: Buying Prada, Gucci, and Louis Vuitton heels... thats the life bro!</div>', unsafe_allow_html=True)
                st.markdown('<div class="visual-bubble">🛍️👠👜👠🛍️</div>', unsafe_allow_html=True)
            if tokens >= 3: 
                st.markdown('<div class="luxury-card">🏨 Tier 3 Daydream: Eating luxurious meals at 7-star hotels! Ufffff! 🔥</div>', unsafe_allow_html=True)
                st.markdown('<div class="visual-bubble">🛎️🍽️🏨🥂🍽️🛎️</div>', unsafe_allow_html=True)
                
            st.info("⚔️ Levi Wisdom: 'The only thing we are allowed to do is believe we don\'t regret our choices.'")
