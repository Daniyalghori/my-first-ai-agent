import os
import streamlit as st
from google import genai

# Set up page configuration for Day 1
st.set_page_config(
    page_title="Day 1: Baseline AI Agent",
    page_icon="🤖",
    layout="centered"
)

# Application Header
st.title("🤖 Day 1: Foundational AI Agent")
st.write("This represents the simple, single-turn LLM agent setup used to start the Generative AI Intensive.")

# 1. Initialize the Gemini GenAI Client
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.error("🚨 CRITICAL ERROR: GEMINI_API_KEY environment variable is not set.")
    st.stop()

# Initialize using the new Google GenAI SDK standards
client = genai.Client(api_key=api_key)

# 2. Basic Interactive UI
user_query = st.text_area(
    "Submit a query to the model:",
    placeholder="Type something here (e.g., 'Explain neural networks in one sentence')..."
)

# 3. Simple Single-Turn Generation Execution Path
if st.button("Query Agent", type="primary"):
    if not user_query.strip():
        st.warning("⚠️ Please provide a query before executing.")
    else:
        with st.spinner("Agent is generating response..."):
            try:
                # Classic direct single model generation call
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_query
                )
                
                st.success("🎯 Response Received:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"❌ Execution failed: {e}")