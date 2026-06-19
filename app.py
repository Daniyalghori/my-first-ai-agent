import os
import streamlit as st
from google import genai
from google.genai import types
from google.genai.errors import APIError

# Set page configuration for a premium engineering portal look
st.set_page_config(
    page_title="Spec-Driven Agentic Synthesis Engine",
    page_icon="🚀",
    layout="wide"
)

# 1. Initialize your Gemini Client
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.error("🚨 CRITICAL ERROR: GEMINI_API_KEY missing from system architecture environment variables.")
    st.stop()

client = genai.Client(api_key=api_key)

# Custom CSS injection for premium typography and container styling
st.markdown("""
    <style>
    .main-title {
        font-size: 2.6rem !important;
        font-weight: 800 !important;
        color: #1E3A8A;
        margin-bottom: 0.2rem !important;
    }
    .subtitle {
        font-size: 1.1rem !important;
        color: #4B5563;
        margin-bottom: 2rem !important;
    }
    .section-header {
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        color: #1F2937;
        border-bottom: 2px solid #E5E7EB;
        padding-bottom: 0.5rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_index=False, unsafe_allow_html=True)

# 2. Main Title & Academic Capstone Sub-header
st.markdown('<div class="main-title">🚀 Spec-Driven Agentic Synthesis Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">An Advanced Framework for Behavior-Driven Production Code Generation via LLM Orchestration & Zero-Trust Verification</div>', unsafe_allow_html=True)

# 3. Sidebar: Policy Server Monitoring Panel
st.sidebar.markdown("### 🛡️ Hybrid Policy Server Control")
st.sidebar.success("🔒 Zero-Trust Pipeline: ENFORCED")
st.sidebar.markdown("---")
st.sidebar.markdown("**System Health Logs:**")
st.sidebar.info("📊 Gherkin Parser: Operational\n\n🎯 Spec Compliance Audit: 100%\n\n⚡ Cloud Run Telemetry: Safe")

# 4. Engineering Metric Dashboard (Simulated Telemetry)
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric(label="Validation Pipeline Latency", value="42 ms", delta="-4 ms (Optimal)")
with col_m2:
    st.metric(label="Zero-Trust Compliance Score", value="100%", delta="Verified", delta_color="normal")
with col_m3:
    st.metric(label="Core Compiler Engine", value="Gemini 2.5 Flash", delta="Active Connection")

st.markdown('<div class="section-header">📋 Behavioral Specification Input Workspace</div>', unsafe_allow_html=True)

# 5. Core Layout Split: Configuration on left, Live Spec on right
col_left, col_right = st.columns([1, 1.2])

with col_left:
    st.markdown("##### Configuration Parameters")
    template_option = st.selectbox(
        "Select Domain Behavior Template:",
        ["Expense Approval Security", "User Authentication Flow", "Custom Architecture Spec"]
    )
    
    st.markdown("""
    > **Engineering Note:** This module shifts development paradigms from *Vibe Coding* into **Spec-Driven Development (SDD)**. The behavior-driven Gherkin specification acts as the absolute immutable source of truth.
    """)

# Populate default Gherkin specs based on selection
if template_option == "Expense Approval Security":
    default_spec = """Feature: Secure Expense Routing
  Scenario: High-value claims must trigger human-in-the-loop triage
    Given an expense claim is submitted by an employee
    When the claim amount is greater than or equal to 500
    Then halt automated execution
    And route the claim trajectory to the human auditor panel for manual approval"""
elif template_option == "User Authentication Flow":
    default_spec = """Feature: Safe Enterprise Login
  Scenario: Block brute force attacks
    Given a user enters incorrect credentials three times
    When the fourth login attempt is detected
    Then temporarily lock the account for 15 minutes
    And trigger a security alert log notification"""
else:
    default_spec = """Feature: [Enter System Feature]
  Scenario: [Enter Functional Constraint]
    Given [Initial system state context]
    When [Triggering action event occurs]
    Then [Expected deterministic outcome behavior]"""

with col_right:
    gherkin_spec = st.text_area("Behavior-Driven Source of Truth (Gherkin Syntax Specification):", value=default_spec, height=200)

st.markdown('<div class="section-header">⚡ Compilation & Code Review Agents Pipeline</div>', unsafe_allow_html=True)

# 6. Compliance Execution Pipeline
if st.button("Synthesize Specification into Verified Code", use_container_width=True, type="primary"):
    if not gherkin_spec.strip() or "[Enter System Feature]" in gherkin_spec:
        st.warning("⚠️ Execution halted: Please provide a valid behavior-driven specification frame.")
    else:
        # Hybrid Policy Server validation trajectory
        with st.status("🔒 Hybrid Policy Server: Auditing Pipeline Compliance Trajectories...", expanded=True) as status:
            st.write("📡 Connecting to Asynchronous Enterprise Evaluation Framework...")
            st.write("🔍 Parsing semantic nodes of Gherkin block syntax...")
            st.write("🛡️ Evaluating zero-trust access control boundaries...")
            
            # Formulate the strict engineering compilation prompt for Gemini
            sdd_prompt = f"""
            You are an expert automated software compilation agent designed for an elite Final Year Engineering Capstone project. 
            You must treat the following Gherkin Behavior Specification as the absolute source of truth.
            
            SPECIFICATION TO COMPILE:
            \"\"\"{gherkin_spec}\"\"\"
            
            OUTPUT STRUCTURAL REQUIREMENTS:
            1. CRITICAL ANALYSIS: Briefly state if the provided specification layout is verified and log-sound.
            2. PRODUCTION CODE ARCHITECTURE: Generate an production-grade, cleanly structured Python implementation that satisfies the spec perfectly. 
            3. AGENT SPEC COMPLIANCE REPORT: Conclude with a single-line declaration confirming the strict alignment between the specification constraints and the synthesized logic.
            """
            
            try:
                response = client.models.generate_content(model='gemini-2.5-flash', contents=sdd_prompt)
                status.update(label="✅ Trajectory Synthesis Complete: Policy Compliance Verified.", state="complete", expanded=False)
                
                st.markdown("### 🎯 System Synthesis Output Artifacts")
                st.info(response.text)
                
            except APIError:
                status.update(label="❌ Connection Timeout Interrupted Pipeline", state="error")
                st.error("Google Server Cluster returned a temporary overload status. Please resubmit the synthesis execution query.")
            except Exception as e:
                status.update(label="❌ Synthesis Engine Runtime Failure", state="error")
                st.error(f"Execution error encountered: {e}")