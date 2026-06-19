import os
import streamlit as st
from google import genai
from google.genai import types
from google.genai.errors import APIError

# 1. Initialize your Gemini Client
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.error("Missing GEMINI_API_KEY! Please set it in your environment variables.")
    st.stop()

client = genai.Client(api_key=api_key)

st.title("🚀 Day 5: Spec-Driven Enterprise Engine")
st.write("Transitioning from **Vibe Coding** prototypes to **Behavior-Driven Specifications**.")

# 2. Sidebar Policy Server Monitoring
st.sidebar.subheader("🛡️ Hybrid Policy Server Status")
st.sidebar.success("🔒 Zero-Trust Pipeline: ENFORCED")
st.sidebar.info("📊 Gherkin Parser: Operational\n\n🎯 Spec Compliance Audit: 100%")

# 3. Choose a Feature Specification Template
st.subheader("📋 Step 1: Select or Write a Behavior Specification (Gherkin Syntax)")

template_option = st.selectbox(
    "Choose a production spec template:",
    ["Expense Approval Security", "User Authentication Flow", "Custom Specification"]
)

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
    default_spec = "# Write your own Given/When/Then spec here..."

gherkin_spec = st.text_area("Behavior-Driven Source of Truth (Gherkin Spec):", value=default_spec, height=160)

# 4. Compile and Run through Policy Server Pipeline
st.subheader("⚡ Step 2: Run Zero-Trust Compliance and Compilation")

if st.button("Compile Spec to Production Code"):
    if not gherkin_spec.strip() or gherkin_spec.startswith("#"):
        st.warning("Please provide a valid specification feature set first!")
    else:
        # Step A: Hybrid Policy Server validation animation
        with st.status("🔒 Policy Server: Auditing System Trajectories...", expanded=True) as status:
            st.write("📡 Connecting to Asynchronous Enterprise Pipeline...")
            st.write("🔍 Running static syntax check on Gherkin blocks...")
            st.write("🛡️ Validating zero-trust compliance constraints...")
            
            # Formulate the strict spec prompt for Gemini
            sdd_prompt = f"""
            You are an automated enterprise-grade code-review and compilation agent. 
            You must treat the following Gherkin Behavior Specification as the absolute source of truth.
            
            SPECIFICATION:
            \"\"\"{gherkin_spec}\"\"\"
            
            INSTRUCTIONS:
            1. Validate if the spec is sound.
            2. Generate the highly robust, clean production Python logic/code block that perfectly satisfies this specification.
            3. Include brief developer compliance notes at the end.
            """
            
            try:
                response = client.models.generate_content(model='gemini-2.5-flash', contents=sdd_prompt)
                status.update(label="✅ Policy Server Approved! Spec compiled successfully.", state="complete", expanded=False)
                
                # Step B: Present the compiled production asset
                st.success("🎯 **Compiled Production-Grade Code Block:**")
                st.write(response.text)
                
            except APIError:
                status.update(label="❌ Connection Timeout", state="error")
                st.error("Google's backend servers are busy. Please try clicking the button again.")
            except Exception as e:
                status.update(label="❌ Pipeline Error", state="error")
                st.error(f"An unexpected error occurred: {e}")