import streamlit as st
import random

# 1. Setup the Page
st.set_page_config(page_title="The Daily Saurav", page_icon="🔥", layout="centered")

# 2. Interactive Memory 
if 'current_hype' not in st.session_state:
    st.session_state.current_hype = ""
if 'current_roast' not in st.session_state:
    st.session_state.current_roast = ""
if 'current_task' not in st.session_state:
    st.session_state.current_task = ""

# 3. The Content Databases (Endless generation)
hypes = [
    "You are actually not terrible at PUBG today. Keep it up.",
    "Your English is getting better. Soon you'll be able to argue with me properly.",
    "You have main character energy today. Don't let the lobby ruin it.",
    "I'll admit it... you're a decent squadmate. (Don't let this go to your head)."
]

roasts = [
    "I've seen bots with better aim than you.",
    "Are you going to carry the squad today, or do I need to prepare my back again?",
    "Your brain lags more than a server with 900 ping.",
    "You ordered the most basic shisha flavor, didn't you? Basic.",
]

tasks = [
    "🎤 Send me a voice note in English explaining your most embarrassing gaming moment.",
    "🎤 Send me a voice note in English telling me what your absolute dream vacation is.",
    "🎤 Send me a voice note in English arguing why you are a better PUBG player than me.",
    "🎤 Send me a voice note in English telling me the most annoying thing about me."
]

# 4. The UI Engine
st.title("🔥 The Daily Saurav")
st.write("Your personal boredom killer and English confidence builder. Choose your button wisely.")
st.divider()

col1, col2 = st.columns(2)

# Button 1: The Hype
with col1:
    if st.button("👑 Hype Me Up", use_container_width=True):
        st.session_state.current_hype = random.choice(hypes)
        st.session_state.current_roast = ""
        st.session_state.current_task = ""

# Button 2: The Roast
with col2:
    if st.button("🤡 Reality Check", use_container_width=True):
        st.session_state.current_roast = random.choice(roasts)
        st.session_state.current_hype = ""
        st.session_state.current_task = ""

# Button 3: The Interactive English Task
st.write("---")
st.subheader("🗣️ The English Speaking Challenge")
st.write("You want to get confident speaking English? Time to do your homework.")

if st.button("📩 Give Me a Voice Note Task", use_container_width=True):
    st.session_state.current_task = random.choice(tasks)
    st.session_state.current_hype = ""
    st.session_state.current_roast = ""

# 5. Display the Results dynamically
if st.session_state.current_hype:
    st.success(f"**{st.session_state.current_hype}**")

if st.session_state.current_roast:
    st.error(f"**{st.session_state.current_roast}**")

if st.session_state.current_task:
    st.info(f"**{st.session_state.current_task}**")
    st.warning("⚠️ **Rule:** Do not text me the answer. You MUST record a voice note in English and send it to me right now. No being shy.")
