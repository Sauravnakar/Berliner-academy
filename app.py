import streamlit as st
from deep_translator import GoogleTranslator

# 1. Setup the Page
st.set_page_config(page_title="The English Academy", page_icon="🦉")

st.title("🦉 Saurav's English Academy")
st.write("Forget the green owl. You're learning from the Boss now.")

st.divider()

# 2. The Real Translator (German -> English)
st.header("🌍 The Real Translator")
st.write("Type your German here, and let my algorithm do the heavy lifting.")

text_to_translate = st.text_area("Enter German text:")

if st.button("Translate to English"):
    if text_to_translate:
        translated = GoogleTranslator(source='de', target='en').translate(text_to_translate)
        st.success(f"**Perfect English:** {translated}")
    else:
        st.warning("You have to actually type something first, Boss.")

st.divider()

# 3. The Duolingo-Style Interactive Quiz
st.header("🎯 The Daily Pop Quiz")
st.write("Let's see if you can actually pass this class. Choose the correct translation.")

q1 = st.radio("1. How do you say 'Du bist sehr anstrengend' in English?", 
              ("You are very smart.", "You are very exhausting.", "You are very funny.", "I am hungry."))

q2 = st.radio("2. How do you say 'Ich bin der Boss' in English?", 
              ("I am the boss.", "You are the boss.", "We are friends.", "I need shisha."))

if st.button("Submit Answers"):
    score = 0
    
    # Grade Q1
    if q1 == "You are very exhausting.":
        st.success("✅ Question 1: Correct! (And highly accurate).")
        score += 1
    else:
        st.error("❌ Question 1: Wrong. You need to study more.")
        
    # Grade Q2
    if q2 == "I am the boss.":
        st.success("✅ Question 2: Correct! Remember who is in charge.")
        score += 1
    else:
        st.error("❌ Question 2: Wrong. (Hint: It's me).")
        
    # Final Score
    if score == 2:
        st.balloons()
        st.success("🎉 Perfect Score! You are officially promoted from Intern.")
    else:
        st.warning(f"You got {score}/2. Try again before I fail you.")
    st.info(f"**What she actually means:** {pubg_phrases[phrase_choice]}")
