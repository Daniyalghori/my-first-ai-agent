import os
import streamlit as st
from google import genai
from google.genai import types

# 1. Initialize your Gemini Client
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.error("Missing GEMINI_API_KEY! Please set it in your environment variables.")
    st.stop()

client = genai.Client(api_key=api_key)

st.title("🎒 Day 4: Secure Expense-Approval Agent")
st.write("Simulating **Human-in-the-Loop (HITL)**, Safety Guards, and Security Trajectories.")

# 2. Sidebar Security Guard Panel
st.sidebar.subheader("🛡️ 7-Pillar Security Triad")
st.sidebar.info("🟢 Ephemeral Sandboxing: **Active**\n\n🔵 Automated Threat Scan: **Enabled**\n\n🔴 Slopsquatting Protection: **Secure**")

# 3. Expense Input Form
with st.form("expense_form"):
    st.subheader("💵 Submit Corporate Expense Claim")
    item_name = st.text_input("Item / Service Name:", placeholder="e.g., Cloud Server Subscription")
    amount = st.number_input("Amount ($):", min_value=1.0, step=10.0, value=150.0)
    justification = st.text_area("Business Justification / Prompt:", placeholder="Provide details for the expense...")
    
    submit_button = st.form_submit_with_name("Analyze Claim")

# 4. Processing the Claim
if submit_button:
    if not item_name.strip() or not justification.strip():
        st.warning("Please fill out all fields before submitting.")
    else:
        # Step A: Run Automated Threat Scan / Safety Guard
        with st.status("🔍 Security Engine Running Scans...", expanded=True) as status:
            st.write("🛡️ Scanning inputs for Prompt Injections...")
            
            # Simple simulation of input sanitization/guardrails
            if "ignore previous instructions" in justification.lower() or "bypass" in justification.lower():
                status.update(label="🚨 Malicious Prompt Injection Detected!", state="error", expanded=True)
                st.error("Security Alert: System blocked potential exploit attempt.")
                st.stop()
                
            st.write("✅ Security Guard Scan Passed.")
            st.write("📊 Evaluating expense tier against automated policies...")
            
            # Step B: Determine policy routing based on amount
            if amount >= 500.0:
                # Requires Human-in-the-Loop Triage
                status.update(label="⚠️ Triage Triggered: Human-in-the-Loop Intervention Required", state="error", expanded=True)
                st.session_state["hitl_triggered"] = True
                st.session_state["pending_item"] = item_name
                st.session_state["pending_amount"] = amount
                st.session_state["pending_justification"] = justification
            else:
                # Auto-approve via Gemini Evaluation Trajectory
                status.update(label="✅ Policy Cleared: Passing to Automated Agent Evaluation", state="complete", expanded=False)
                st.session_state["hitl_triggered"] = False
                
                # Let Gemini evaluate the business validity
                eval_prompt = f"Review this expense claim for business validity. Item: {item_name}, Amount: ${amount}. Justification: {justification}. Give a 2-sentence corporate assessment decision."
                response = client.models.generate_content(model='gemini-2.5-flash', contents=eval_prompt)
                
                st.success(f"🤖 **Automated Agent Decision (Auto-Approved Under $500):**")
                st.write(response.text)

# 5. Render Human-in-the-Loop Interface if triggered
if st.session_state.get("hitl_triggered", False):
    st.markdown("---")
    st.warning(f"🚨 **HUMAN INTERVENTION REQUIRED**\n\nThe claim for **{st.session_state['pending_item']}** (${st.session_state['pending_amount']}) exceeds the $500 automated security threshold.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👍 Grant Human Approval", use_container_width=True):
            with st.spinner("Processing manual override trajectory..."):
                eval_prompt = f"The human supervisor has APPROVED this high-value expense. Generate a formal approval receipt response for: {st.session_state['pending_item']} costing ${st.session_state['pending_amount']}."
                response = client.models.generate_content(model='gemini-2.5-flash', contents=eval_prompt)
                st.success("💼 Expense Logged and Disbursed!")
                st.write(response.text)
                st.session_state["hitl_triggered"] = False
    with col2:
        if st.button("👎 Reject Claim", use_container_width=True):
            st.error(f"❌ Claim for {st.session_state['pending_item']} has been forcefully rejected by the Human Auditor.")
            st.session_state["hitl_triggered"] = False