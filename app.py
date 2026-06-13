import streamlit as st
import random

# 1. Setup the Page
st.set_page_config(page_title="Main Character Academy", page_icon="🎬", layout="centered")

# 2. Advanced Memory State (Endless Loop)
if 'scenario' not in st.session_state:
    st.session_state.scenario = None
if 'score' not in st.session_state:
    st.session_state.score = 0

# 3. The K-Drama Database
# This makes it continuous. It pulls randomly from these scenes.
kdrama_scenes = [
    {
        "title": "🌧️ The Wrist Grab in the Rain",
        "german": "Der reiche CEO greift plötzlich nach deinem Handgelenk, während es regnet.",
        "english": "Where do you think you are going? You work for me now.",
        "acting_tip": "Say it loudly, like you are annoyed but secretly in love with him."
    },
    {
        "title": "✉️ The Evil Mother-in-Law",
        "german": "Die böse Schwiegermutter schiebt dir einen Umschlag mit Geld über den Tisch.",
        "english": "Keep your money. My love cannot be bought!",
        "acting_tip": "Speak with absolute confidence. Pretend to slam your hand on the table."
    },
    {
        "title": "☕ The Coffee Spill",
        "german": "Du kommst zu spät und schüttest Kaffee auf einen gutaussehenden Fremden.",
        "english": "Watch where you are going, idiot! ...Oh wait, you're my new boss?",
        "acting_tip": "Start angry, and end the sentence sounding completely panicked."
    },
    {
        "title": "☂️ The Second Male Lead",
        "german": "Der süße beste Freund schaut dich traurig an und hält einen Regenschirm.",
        "english": "I was always one step behind him, wasn't I?",
        "acting_tip": "Say it slowly. Cue the sad piano music in your head."
    },
    {
        "title": "🍜 The Ramen Confession",
        "german": "Er fragt dich, ob du noch auf Ramen mit zu ihm kommen willst.",
        "english": "Do you want to come in and eat ramen before you leave?",
        "acting_tip": "Say it softly and act very, very shy. (We all know what this means in K-Dramas)."
    }
]

# 4. The UI Engine
st.title("🎬 The Main Character English Simulator")
st.write("Since you are always shy about speaking English, we are going to fix that. Welcome to your K-Drama acting class.")
st.divider()

# 5. The "Boredom" Button (Generates endless scenes)
if st.button("🎭 Give Me a Scene to Act", use_container_width=True):
    st.session_state.scenario = random.choice(kdrama_scenes)

# 6. Display the Scene interactively
if st.session_state.scenario:
    scene = st.session_state.scenario
    
    st.header(scene["title"])
    st.caption("THE SCENARIO:")
    st.info(scene["german"])
    
    st.write("---")
    st.caption("YOUR ENGLISH LINE (SAY IT OUT LOUD):")
    st.success(f"**\"{scene['english']}\"**")
    
    st.warning(f"🎬 **Director's Note:** {scene['acting_tip']}")
    
    st.write("---")
    
    # Confidence Booster Checkbox
    if st.checkbox("✅ I said it out loud like a true Main Character!"):
        st.balloons()
        st.session_state.score += 10
        st.write(f"**Star Power Level:** {st.session_state.score} / 100")
