import os
import streamlit as st
from google import genai

# Set up page configuration with an ultra-modern layout
st.set_page_config(
    page_title="IntelliAgent",
    page_icon="🧠",
    layout="centered"
)

# Advanced CSS Architecture: Custom Injectable UI Framework with Animations
st.markdown("""
    <style>
    /* Keyframes for Engineering Micro-Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulseGlow {
        0% { box-shadow: 0 0 5px rgba(37, 99, 235, 0.2); }
        50% { box-shadow: 0 0 15px rgba(37, 99, 235, 0.5); }
        100% { box-shadow: 0 0 5px rgba(37, 99, 235, 0.2); }
    }
    
    /* Animation Wrapper classes */
    .animated-container {
        animation: fadeIn 0.8s ease-out forwards;
    }
    
    /* Premium Title Header Typography */
    .main-title {
        font-size: 2.6rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #1E293B, #2563EB, #3B82F6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.1rem !important;
        animation: fadeIn 0.6s ease-out;
    }
    .subtitle {
        font-size: 1.05rem !important;
        color: #64748B;
        margin-bottom: 2rem !important;
        font-family: 'Courier New', Courier, monospace;
        letter-spacing: 0.5px;
        animation: fadeIn 0.8s ease-out;
    }
    
    /* Glassmorphic Engineering Workspace Panels */
    div[data-testid="stTextArea"] {
        border: 2px solid #E2E8F0 !important;
        border-radius: 12px !important;
        transition: all 0.3s ease-in-out !important;
        background: #F8FAFC !important;
    }
    div[data-testid="stTextArea"]:focus-within {
        border-color: #2563EB !important;
        animation: pulseGlow 2s infinite !important;
    }
    
    /* Telemetry Info & Status Card Styling */
    .telemetry-card {
        background: linear-gradient(145deg, #ffffff, #f1f5f9);
        border: 1px solid #cbd5e1;
        border-left: 6px solid #2563EB;
        border-radius: 10px;
        padding: 1.25rem;
        margin-top: 1.5rem;
        animation: fadeIn 0.5s ease-out forwards;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    .telemetry-title {
        font-weight: 700;
        color: #0F172A;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    
    /* Custom Override for the Action Execution Button */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #1E293B, #2563EB) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.6rem 2rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2) !important;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.4) !important;
        background: linear-gradient(90deg, #0F172A, #1D4ED8) !important;
    }
    div.stButton > button:first-child:active {
        transform: translateY(0px) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Layout Container with dynamic entry animations
st.markdown('<div class="animated-container"><div class="main-title">🤖 IntelliAgent Engine</div></div>', unsafe_allow_html=True)
st.markdown('<div class="animated-container"><div class="subtitle">SYSTEM CORE: REAL-TIME INFERENCE GATEWAY // RUNTIME MODULE v1.0.4</div></div>', unsafe_allow_html=True)

# 1. Initialize the Gemini GenAI Client
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.error("🚨 CRITICAL REGISTRY FAILURE: GEMINI_API_KEY environment variable is missing.")
    st.stop()

# Initialize using the Google GenAI SDK standards
client = genai.Client(api_key=api_key)

# 2. Workspace Input Area (Monitored via Custom CSS States)
user_query = st.text_area(
    "Execution Input Workspace:",
    placeholder="Enter systemic instructions, engineering constraints, or raw prompts here...",
    height=150
)

# 3. Micro-Animated Execution Pipeline
if st.button("Execute Baseline Inference", type="primary", use_container_width=True):
    if not user_query.strip():
        st.warning("⚠️ Execution halted: Workspace input is empty.")
    else:
        with st.spinner("Synchronizing pipeline with Gemini 2.5 Flash..."):
            try:
                # Direct single-turn inference call to Gemini 2.5 Flash
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_query
                )
                
                # Render results within a custom styled telemetry block
                st.markdown(f"""
                <div class="telemetry-card">
                    <div class="telemetry-title">🎯 IntelliAgent Telemetry Output</div>
                    <div>{response.text}</div>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"❌ Core processing error: {e}")