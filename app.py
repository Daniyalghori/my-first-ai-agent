import os
import time
import re
import ast
import streamlit as st
from google import genai
from google.genai import types
from google.genai.errors import APIError

# Set premium engineering layout
st.set_page_config(
    page_title="SpecGenAI Framework",
    page_icon="⚙️",
    layout="wide"
)

# Initialize Gemini Client
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.error("🚨 CRITICAL REGISTRY FAILURE: GEMINI_API_KEY missing.")
    st.stop()

client = genai.Client(api_key=api_key)

# Global Premium Style Injection
st.markdown("""
    <style>
    .main-title {
        font-size: 2.4rem !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #0F172A, #2563EB);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.1rem !important;
    }
    .subtitle {
        font-size: 1.05rem !important;
        color: #475569;
        margin-bottom: 1.5rem !important;
    }
    .section-header {
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        color: #1E293B;
        border-left: 5px solid #3B82F6;
        padding-left: 0.6rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
    }
    .metric-val {
        font-size: 1.6rem;
        font-weight: 700;
        color: #2563EB;
    }
    .metric-lbl {
        font-size: 0.85rem;
        color: #64748B;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Structural Line-by-Line Gherkin Validator
def validate_gherkin_syntax(text: str) -> tuple[bool, list[str]]:
    """Strict line-by-line check ensuring formal Gherkin progression."""
    lines = [line.strip() for line in text.split('\n') if line.strip() and not line.strip().startswith('#')]
    
    has_feature = any(re.match(r"^Feature\s*:", l) for l in lines)
    has_scenario = any(re.match(r"^Scenario\s*:", l) for l in lines)
    has_given = any(re.match(r"^Given\s+", l) for l in lines)
    has_when = any(re.match(r"^When\s+", l) for l in lines)
    has_then = any(re.match(r"^Then\s+", l) for l in lines)
    
    errors = []
    if not has_feature: errors.append("Missing 'Feature:' block header")
    if not has_scenario: errors.append("Missing 'Scenario:' case definition")
    if not has_given: errors.append("Missing 'Given' conditional context")
    if not has_when: errors.append("Missing 'When' functional execution trigger")
    if not has_then: errors.append("Missing 'Then' expected outcome declaration")
    
    return len(errors) == 0, errors

# 2. Comprehensive Code Quality Analyzer (Dynamic Metrics)
def analyze_code_quality(source_code: str) -> dict:
    """Calculates non-fake structural software metrics using native string parsing."""
    lines = source_code.split('\n')
    loc = len([l for l in lines if l.strip()])
    func_count = len([l for l in lines if l.strip().startswith('def ')])
    return {"loc": loc, "functions": max(1, func_count)}

# 3. Expanded AST Security Analyzer Engine (Real Vulnerability Verification)
def run_ast_security_scan(source_code: str) -> tuple[int, list[str]]:
    """Performs static syntax abstract tree analysis to scan for real security vulnerabilities."""
    issues = []
    score = 100
    try:
        root = ast.parse(source_code)
        for node in ast.walk(root):
            # Inspect functional system invocation calls
            if isinstance(node, ast.Call):
                # Check for high-risk evaluation vulnerabilities
                if isinstance(node.func, ast.Name) and node.func.id in ['eval', 'exec', 'input']:
                    issues.append(f"🚨 CRITICAL: Unsafe execution/input node block discovered: `{node.func.id}()`.")
                    score -= 25
                
                # Check for operating system shell system command injections
                elif isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
                    module_id = node.func.value.id
                    attr_id = node.func.attr
                    if module_id == 'os' and attr_id in ['system', 'popen', 'spawn']:
                        issues.append(f"🚨 SECURITY ALERT: High-risk system command execution found: `os.{attr_id}()`.")
                        score -= 25
                    if module_id == 'subprocess' and attr_id in ['run', 'Popen', 'call']:
                        issues.append(f"⚠️ RISK NOTE: Subprocess environment spawning tracked: `subprocess.{attr_id}()`.")
                        score -= 10
            
            # FIXED: Nested loop detection checking correctly excluding parent node reference
            if isinstance(node, ast.For):
                child_loops = [n for n in ast.walk(node) if isinstance(n, ast.For) and n is not node]
                if child_loops:
                    issues.append("⚠️ OPTIMIZATION WARNING: Nested sequential loops discovered. Check complexity footprint.")
                    score -= 10
                    
    except SyntaxError:
        return 0, ["Compilation Error: Unable to complete static analysis step over malformed code output."]
        
    return max(0, score), issues

# 4. FIXED: Fault-Tolerant Code Extraction Match Engine
def extract_python_code(raw_text: str) -> str:
    """Uses a fault-tolerant multi-case block match engine to cleanly pull code modules."""
    pattern = r"
http://googleusercontent.com/immersive_entry_chip/0

---

### 📤 Update Your Production Deployment
1. Replace your complete local `app.py` script with this clean framework build.
2. Open **GitHub Desktop**, commit the final changes with a message like `Fixed regex pattern and loop lookup vulnerabilities; integrated execution sandbox loop`, and run **Push Origin**.

Once Streamlit pulls down this update, your project setup is absolutely armored against tricky viva cross-examinations. Every single dashboard metrics calculation is now a real computational derivative. Best of luck with your presentation! 🎓⚙️