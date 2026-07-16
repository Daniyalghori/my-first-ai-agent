import os
import streamlit as st
from google import genai

# Set up page configuration for an ultra-modern, high-tech engine portal
st.set_page_config(
    page_title="IntelliAgent",
    page_icon="🧠",
    layout="centered"
)

# Advanced CSS Architecture: Blueprint Aesthetics, AI Schematics & Micro-Animations
st.markdown("""
    <style>
    /* Absolute AI Circuit Board Blueprint Background Layer */
    .stApp {
        background-color: #0b0f19 !important;
        background-image: 
            /* Subtle grid lines */
            linear-gradient(rgba(37, 99, 235, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(37, 99, 235, 0.05) 1px, transparent 1px),
            /* Abstract Neural Node Vector Doodles */
            radial-gradient(circle at 10% 20%, rgba(59, 130, 246, 0.08) 2px, transparent 3px),
            radial-gradient(circle at 85% 15%, rgba(16, 185, 129, 0.06) 4px, transparent 6px),
            /* Circuit traces and nodes */
            radial-gradient(circle at 30% 80%, rgba(37, 99, 235, 0.07) 3px, transparent 5px),
            radial-gradient(circle at 75% 70%, rgba(59, 130, 246, 0.05) 2px, transparent 4px);
        background-size: 40px 40px, 40px 40px, 200px 200px, 350px 350px, 300px 300px, 250px 250px;
        color: #f8fafc !important;
    }

    /* Keyframes for Engineering Micro-Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes corePulse {
        0% { border-color: rgba(37, 99, 235, 0.3); box-shadow: 0 0 8px rgba(37, 99, 235, 0.1); }
        50% { border-color: rgba(59, 130, 246, 0.7); box-shadow: 0 0 18px rgba(59, 130, 246, 0.4); }
        100% { border-color: rgba(37, 99, 235, 0.3); box-shadow: 0 0 8px rgba(37, 99, 235, 0.1); }
    }
    
    /* Animation Wrapper classes */
    .animated-container {
        animation: fadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    
    /* Premium Title Header Typography */
    .main-title {
        font-size: 2.8rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #ffffff, #60a5fa, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.1rem !important;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }
    .subtitle {
        font-size: 0.95rem !important;
        color: #94a3b8;
        margin-bottom: 2rem !important;
        font-family: 'Courier New', Courier, monospace;
        letter-spacing: 1px;
    }

    /* Target input label color explicitly for dark mode visibility */
    label[data-testid="stWidgetLabel"] p {
        color: #cbd5e1 !important;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    
    /* Cybernetic Workspace Input Terminal Panels */
    div[data-testid="stTextArea"] textarea {
        background-color: #0f172a !important;
        color: #f1f5f9 !important;
        border-radius: 10px !important;
    }
    div[data-testid="stTextArea"] {
        border: 2px solid rgba(51, 65, 85, 0.7) !important;
        border-radius: 12px !important;
        transition: all 0.3s ease-in-out !important;
        background: #0f172a !important;
    }
    div[data-testid="stTextArea"]:focus-within {
        animation: corePulse 2s infinite !important;
    }
    
    /* Telemetry Output Box Glassmorphism Styling */
    .telemetry-card {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-left: 6px solid #3b82f6;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1.5rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(4px);
    }
    .telemetry-title {
        font-weight: 700;
        color: #60a5fa;
        font-size: 1.1rem;
        margin-bottom: 0.75rem;
        font-family: 'Courier New', Courier, monospace;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .telemetry-content {
        color: #e2e8f0;
        line-height: 1.6;
    }
    
    /* Custom Engineering Trigger Button Override */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #1e3a8a, #2563eb) !important;
        color: #ffffff !important;
        border: 1px solid rgba(96, 165, 250, 0.4) !important;
        border-radius: 8px !important;
        padding: 0.65rem 2rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.75px !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 20px rgba(37, 99, 235, 0.4) !important;
        background: linear-gradient(90deg, #2563eb, #3b82f6) !important;
        border-color: #60a5fa !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main Dashboard Frame Wrapping
st.markdown('<div class="animated-container"><div class="main-title">🤖 IntelliAgent Engine</div></div>', unsafe_allow_html=True)
st.markdown('<div class="animated-container"><div class="subtitle">CORE BASELINE // NEURAL NETWORK INTELLIGENCE GATEWAY v1.0.5</div></div>', unsafe_allow_html=True)

# 1. Initialize the Gemini GenAI Client
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.error("🚨 CRITICAL REGISTRY FAILURE: GEMINI_API_KEY environment variable is missing.")
    st.stop()

client = genai.Client(api_key=api_key)

# 2. Workspace Input Area (Monitored via Custom CSS States)
user_query = st.text_area(
    "Execution Input Workspace:",
    placeholder="Enter structural text prompts, algorithms, or engineering instructions here...",
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
                
                # Render results within a custom styled blueprint card block
                st.markdown(f"""
                <div class="telemetry-card">
                    <div class="telemetry-title">🎯 IntelliAgent Telemetry Output</div>
                    <div class="telemetry-content">{response.text}</div>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"❌ Core processing error: {e}")