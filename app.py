import streamlit as st
import random
import google.generativeai as genai
from games import memory_game, reaction_game

# Configure Gemini
genai.configure(api_key=st.secrets["API_KEY"])
model = genai.GenerativeModel("gemini-pro")

st.title("🧠 Cognitive Brain Fitness Trainer")

st.markdown("""
Welcome to your personal brain gym!  
Train your mind, track progress, and receive AI-powered tips.  
""")

# --- Memory Game
st.header("🧩 Memory Game")

if st.button("Start Memory Challenge"):
    sequence = memory_game()
    st.write(f"Memorize this sequence: {sequence}")
    user_input = st.text_input("Enter the sequence (comma separated):")
    if user_input:
        user_seq = [int(i.strip()) for i in user_input.split(",")]
        if user_seq == sequence:
            st.success("Correct! Well done. 🎉")
        else:
            st.error(f"Incorrect! The correct sequence was {sequence}")

# --- Reaction Test
st.header("⚡ Reaction Time Test")

if st.button("Start Reaction Test"):
    st.write("Get ready...")
    st.info("When you see GO!, press Enter as fast as possible in your terminal or type 'done'.")
    delay = random.randint(2, 5)
    st.write("Wait for it...")
    time.sleep(delay)
    st.write("GO! Type 'done' below as fast as possible:")
    start_time = time.time()
    response = st.text_input("Type 'done':")
    if response.lower() == "done":
        reaction_time = round(time.time() - start_time, 3)
        st.success(f"Your reaction time: {reaction_time} seconds")

# --- AI Advice
st.header("🤖 AI Cognitive Fitness Tips")

goal = st.selectbox("What would you like to improve?", ["Memory", "Attention", "Problem-solving", "Speed", "Creativity"])

if st.button("Get Personalized Advice"):
    prompt = f"""
    I am working on improving my {goal.lower()} using brain games.
    Give me practical tips, training suggestions, and motivational advice in a friendly style.
    """
    response = model.generate_content(prompt)
    st.markdown(response.text)

st.caption("💪 Powered by Python, Streamlit & Gemini API")
