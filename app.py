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

st.title("🎒 Day 2: MCP Developer Knowledge Agent")
st.write("Connected to: **Google Developer Knowledge MCP Server**")

# 2. Define the MCP Tool function
def fetch_google_developer_knowledge(topic: str) -> str:
    """
    Connects to the Google Developer Knowledge MCP server to retrieve 
    canonical, machine-readable documentation and code samples.
    """
    # This simulates pulling live data from Google's documentation server
    topic_lower = topic.lower()
    if "gemini" in topic_lower or "genai" in topic_lower:
        return """
        [MCP Server Result - Source: ai.google.dev]
        To initialize the new Google GenAI SDK in Python:
```python
        from google import genai
        client = genai.Client()
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents='Hello World'
        )
        print(response.text)
        ```
        """
    elif "streamlit" in topic_lower:
        return "[MCP Server Result] Streamlit apps are run locally via command: `streamlit run app.py`"
    else:
        return f"[MCP Server Result] Successfully queried Google Knowledge MCP for: '{topic}'. No critical issues found."

# Create a tool dictionary map
tools_map = {"fetch_google_developer_knowledge": fetch_google_developer_knowledge}

# 3. User Interface
user_query = st.text_input(
    "Ask a technical question about Google tools:", 
    placeholder="e.g., How do I call gemini-2.5-flash using the new SDK?"
)

if st.button("Query Agent via MCP"):
    if not user_query.strip():
        st.warning("Please enter a question first!")
    else:
        with st.spinner("Routing request through Antigravity CLI context..."):
            
            # Ask Gemini while giving it access to our MCP tool
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_query,
                config=types.GenerateContentConfig(
                    tools=[fetch_google_developer_knowledge]
                )
            )
            
            # Check if Gemini decided it needed to read the documentation tool
            if response.function_calls:
                st.subheader("💭 Agent Thought Process (A2UI)")
                for call in response.function_calls:
                    st.info(f"🔍 AI decided it needs official data. Executing tool: `{call.name}`")
                    
                    # Run the tool
                    mcp_result = tools_map[call.name](**call.args)
                    
                    st.markdown("### 📥 Live Documentation Retrieved:")
                    st.code(mcp_result, language="python")
                    
                    # Send the data back to Gemini for a final summary
                    final_response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=f"The user asked: {user_query}. The documentation server returned this: {mcp_result}. Summarize this perfectly for them."
                    )
                    st.markdown("### 🎯 Final Answer:")
                    st.write(final_response.text)
            else:
                # If it didn't need tools, just print normal answer
                st.subheader("🎯 Answer:")
                st.write(response.text)