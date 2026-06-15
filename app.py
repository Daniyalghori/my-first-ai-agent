import os
import streamlit as st
from google import genai

# Setup the connection to Google AI Studio
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

st.title("🤖 My Day 1 AI App")

# Create a text box for user input
user_input = st.text_input("Ask your AI Agent to write something:", "Write a tagline for an AI course.")

if st.button("Run Agent"):
    with st.spinner("Thinking..."):
        # Send the text to the Gemini model
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_input
        )
        st.subheader("Agent Response:")
        st.write(response.text)