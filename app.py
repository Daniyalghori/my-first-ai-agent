import os
import streamlit as st
from google import genai

# Set up page configuration for a clean, academic look
st.set_page_config(
    page_title="IntelliAgent Engine",
    page_icon="🤖",
    layout="centered"
)

# Application Header Styling
st.markdown("""
    <style>
    .main-title {
        font-size: 2.3rem !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #1E293B, #2563EB);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.1rem !important;
    }
    .subtitle {
        font-size: 1.0rem !important;
        color: #475569;
        margin-bottom: 1.5rem !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🤖 IntelliAgent Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Foundational Real-Time Inference Gateway & Model Baseline Pipeline</div>', unsafe_allow_html=True)

# 1. Initialize the Gemini GenAI Client
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.error("🚨 CRITICAL REGISTRY FAILURE: GEMINI_API_KEY environment variable is missing.")
    st.stop()

# Initialize using the Google GenAI SDK standards
client = genai.Client(api_key=api_key)

# 2. Modern Interactive Input Area
user_query = st.text_area(
    "Execution Input Workspace:",
    placeholder="Enter your instruction or query here...",
    height=150
)

# 3. Execution Pipeline
if st.button("Execute Baseline Inference", type="primary", use_container_width=True):
    if not user_query.strip():
        st.warning("⚠️ Execution halted: Workspace input is empty.")
    else:
        with st.spinner("Processing inference pipeline on Gemini 2.5 Flash..."):
            try:
                # Direct single-turn inference call to Gemini 2.5 Flash
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_query
                )
                
                st.success("🎯 IntelliAgent Telemetry Output:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"❌ Core processing error: {e}")