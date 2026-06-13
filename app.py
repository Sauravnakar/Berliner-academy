import streamlit as st

# 1. Setup the Page Layout
st.set_page_config(page_title="Boss Academy", page_icon="🦉", layout="centered")

# 2. Initialize the App's "Memory" (Session State)
# This prevents the app from resetting every time she clicks a button
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.score = 0

# 3. The Quiz Data (German to English)
questions = [
    {
        "german": "Du bist sehr anstrengend.", 
        "options": ["You are very smart.", "You are very exhausting."], 
        "answer": "You are very exhausting."
    },
    {
        "german": "Ich habe keine Ahnung.", 
        "options": ["I have no idea.", "I am the best player here."], 
        "answer": "I have no idea."
    },
    {
        "german": "Wer ist der Boss?", 
        "options": ["Who is the boss? (Obviously Saurav)", "Where is my coffee?"], 
        "answer": "Who is the boss? (Obviously Saurav)"
    }
]

# 4. The App UI
st.title("🦉 The Boss-Level Academy")
st.write("Let's see if your brain is lagging today. Choose the correct English translation.")

st.divider()

# 5. The Interactive Game Loop
# If she hasn't finished all the questions yet:
if st.session_state.question_index < len(questions):
    
    # Calculate and show the live progress bar
    progress = st.session_state.question_index / len(questions)
    st.progress(progress)
    
    # Load the current question
    current_q = questions[st.session_state.question_index]
    
    st.subheader(f"Translate this: **{current_q['german']}**")
    st.write("") # Just adds a little blank space
    
    # Create two big, side-by-side buttons like a mobile app
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(current_q['options'][0], use_container_width=True):
            if current_q['options'][0] == current_q['answer']:
                st.session_state.score += 1
            st.session_state.question_index += 1
            st.rerun() # This instantly refreshes the screen to the next question
            
    with col2:
        if st.button(current_q['options'][1], use_container_width=True):
            if current_q['options'][1] == current_q['answer']:
                st.session_state.score += 1
            st.session_state.question_index += 1
            st.rerun()

# 6. The Final Results Screen
else:
    st.progress(1.0)
    st.header("🎓 Exam Finished")
    st.subheader(f"Your Final Score: {st.session_state.score} / {len(questions)}")
    
    if st.session_state.score == len(questions):
        st.balloons()
        st.success("Perfect score! You are officially promoted from Intern.")
    elif st.session_state.score > 0:
        st.warning("You passed, but barely. We need to work on your skills.")
    else:
        st.error("Zero points. Absolutely terrible. Back to the lobby.")
        
    st.divider()
    
    # Let her restart the game
    if st.button("Retake the Exam", use_container_width=True):
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.rerun()
