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

st.title("🎒 Day 3: Dynamic Agent Skills Framework")
st.write("Simulating **Antigravity ADK & Skills Directory** with Progressive Disclosure.")

# 2. Simulate our Local Skills Registry (The SKILL.md configurations)
SKILLS_REGISTRY = {
    "Code_Linter_Skill": {
        "description": "Lints, optimizes, and debugs source code syntax using natural language standards.",
        "skill_md": """
        # SKILL.md: Code Linter Specialist
        - ROLE: Senior Python Code Reviewer
        - INSTRUCTIONS: Analyze the provided code block for missing syntax, security flaws, or unhandled exceptions.
        - OUTPUT FORMAT: Provide a 'Bugs Found' section followed by an 'Optimized Solution' block.
        """
    },
    "Agent_Tester_Skill": {
        "description": "Generates automated test cases and edge-case testing scenarios for AI agents.",
        "skill_md": """
        # SKILL.md: Automated Agent Tester
        - ROLE: QA Automation Engineer
        - INSTRUCTIONS: Design 3 critical test scenarios (including a bad/empty input scenario) for the user's logic.
        - OUTPUT FORMAT: Bulleted test cases with expected results.
        """
    }
}

# 3. User UI - Selecting/Discovering a Skill
st.subheader("🛠️ Step 1: Load a Specialist Skill from ADK Directory")
selected_skill = st.selectbox(
    "Choose an available Agent Skill to load into memory:",
    options=list(SKILLS_REGISTRY.keys()),
    format_func=lambda x: f"{x} — {SKILLS_REGISTRY[x]['description']}"
)

# Display the loaded SKILL.md contents dynamically (Progressive Disclosure)
with st.expander(f"📄 View Loaded `{selected_skill}/SKILL.md` Configurations", expanded=False):
    st.code(SKILLS_REGISTRY[selected_skill]["skill_md"], language="markdown")

# 4. User Prompt Input
st.subheader("⚡ Step 2: Execute Task with Loaded Skill")
user_task = st.text_area(
    "Enter the code or agent prompt you want this specialist to process:",
    placeholder="Paste code to lint or describe a feature to test here..."
)

if st.button("Execute Skill via Agents CLI"):
    if not user_task.strip():
        st.warning("Please provide task details first!")
    else:
        # Load rules only at execution time to avoid "context rot"
        active_skill_rules = SKILLS_REGISTRY[selected_skill]["skill_md"]
        
        with st.status(f"⚙️ Antigravity CLI: Initializing `{selected_skill}`...", expanded=True) as status:
            st.write("📦 Reading local skill workspace registry...")
            st.write("🔍 Parsing `SKILL.md` rules into execution context...")
            st.write("🚀 Sending temporary lightweight frame to Gemini...")
            
            # Combine the lightweight skill guide with the user's task
            orchestration_prompt = f"""
            {active_skill_rules}
            
            USER TASK TO EXECUTE:
            \"\"\"{user_task}\"\"\"
            """
            
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=orchestration_prompt
            )
            
            status.update(label=f"✅ `{selected_skill}` Execution Completed!", state="complete", expanded=False)
            
        st.markdown(f"### 🎯 `{selected_skill}` Output:")
        st.info(response.text)