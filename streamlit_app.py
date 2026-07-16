"""
streamlit_app.py

Professional Streamlit UI for WorkWell AI
"""

import time
import streamlit as st

from ai_engine import AIEngine

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="WorkWell AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# LOAD CSS
# ======================================================

def load_css():

    try:

        with open("assets/style.css") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    except:

        pass


load_css()

# ======================================================
# SESSION STATE
# ======================================================

if "engine" not in st.session_state:

    st.session_state.engine = AIEngine()

if "messages" not in st.session_state:

    st.session_state.messages = []

if "stats" not in st.session_state:

    st.session_state.stats = {

        "messages": 0,

        "rag_queries": 0,

        "recommendations": 0

    }

if "example_prompt" not in st.session_state:

    st.session_state.example_prompt = None


engine = st.session_state.engine

# ======================================================
# SIDEBAR
# ======================================================

with st.sidebar:

    st.markdown(
        """
<div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.2rem;">
  <div style="width:38px;height:38px;border-radius:11px;display:flex;align-items:center;
  justify-content:center;font-size:1.15rem;background:linear-gradient(135deg,#3B82F6,#8B5CF6);
  box-shadow:0 4px 14px rgba(59,130,246,0.35);">🧠</div>
  <div>
    <div style="font-size:1.1rem;font-weight:700;color:#E5E7EB;line-height:1.1;">WorkWell AI</div>
    <div style="font-size:0.78rem;color:#94A3B8;">Mental Wellness Assistant</div>
  </div>
</div>
""",
        unsafe_allow_html=True
    )

    st.divider()

    st.subheader("🟢 System Status")

    st.success("Analysis Model : Qwen 2.5")

    st.success("Chat Model : Llama 3.2")

    st.success("Embedding : nomic-embed-text")

    st.success("Knowledge Base : Ready")

    st.success("Conversation Memory : Active")

    st.divider()

    st.subheader("📚 Knowledge Base")

    st.metric(

        "Documents",

        "6"

    )

    st.metric(

        "Status",

        "Indexed"

    )

    st.divider()

    st.subheader("📈 Session Statistics")

    st.metric(

        "Messages",

        st.session_state.stats["messages"]

    )

    st.metric(

        "RAG Queries",

        st.session_state.stats["rag_queries"]

    )

    st.metric(

        "Recommendations",

        st.session_state.stats["recommendations"]

    )

    st.divider()

    st.subheader("💬 Quick Questions")

    if st.button("😔 I'm stressed"):

        st.session_state.example_prompt = (

            "I'm feeling stressed."

        )

    if st.button("🏠 Work From Home"):

        st.session_state.example_prompt = (

            "Can employees work from home?"

        )

    if st.button("🌴 Leave Policy"):

        st.session_state.example_prompt = (

            "How many annual leaves do employees receive?"

        )

    if st.button("💼 Employee Benefits"):

        st.session_state.example_prompt = (

            "What employee benefits are available?"

        )

    if st.button("❤️ Mental Wellness"):

        st.session_state.example_prompt = (

            "Give me some stress management tips."

        )

    st.divider()

    if st.button("🗑 Clear Conversation"):

        engine.clear_memory()

        st.session_state.messages = []

        st.session_state.stats = {

            "messages": 0,

            "rag_queries": 0,

            "recommendations": 0

        }

        st.rerun()

# ======================================================
# MAIN HEADER
# ======================================================

st.markdown(

"""
<div class="app-header">

  <div class="logo-badge">🧠</div>

  <div class="title">WorkWell AI</div>

  <div class="subtitle">Mental Wellness Support for IT Employees</div>

</div>
""",

unsafe_allow_html=True

)

# ======================================================
# FEATURE CARDS
# ======================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.info("😊 Emotional Support")

with col2:

    st.success("💡 Recommendations")

with col3:

    st.warning("📚 Company Policies")

with col4:

    st.error("🧠 Memory")

# ======================================================
# WELCOME
# ======================================================

if len(st.session_state.messages) == 0:

    st.markdown(

"""
<div class="welcome-card">

<h3>👋 Welcome to WorkWell AI</h3>

<p style="color:#94A3B8;margin-bottom:0.6rem;">I can help you with:</p>

<ul>
<li>😊 Stress Management</li>
<li>🌴 Leave Policies</li>
<li>🏠 Work From Home</li>
<li>💼 Employee Benefits</li>
<li>❤️ Mental Wellness</li>
<li>📚 HR Policies</li>
</ul>

<p style="color:#94A3B8;margin-top:0.6rem;margin-bottom:0;">Type your question below to begin.</p>

</div>
""",

unsafe_allow_html=True

)

# ======================================================
# DISPLAY CHAT HISTORY
# ======================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        if message["role"] == "assistant":

            st.markdown(
                f"""
<div class="assistant-card">

{message["content"]}

</div>
""",
                unsafe_allow_html=True
            )

        else:

            st.markdown(message["content"])


# ======================================================
# CHAT INPUT
# ======================================================

prompt = st.chat_input(
    "Ask WorkWell AI anything..."
)

if st.session_state.example_prompt:

    prompt = st.session_state.example_prompt

    st.session_state.example_prompt = None


# ======================================================
# PROCESS USER MESSAGE
# ======================================================

if prompt:

    # ---------------------------------------------
    # User Message
    # ---------------------------------------------

    st.session_state.messages.append(

        {

            "role": "user",

            "content": prompt

        }

    )

    st.session_state.stats["messages"] += 1

    with st.chat_message("user"):

        st.markdown(prompt)

    # ---------------------------------------------
    # Assistant
    # ---------------------------------------------

    with st.chat_message("assistant"):

        badge = "🤖 General Assistant"

        p = prompt.lower()

        if any(

            word in p

            for word in [

                "leave",

                "policy",

                "work from home",

                "benefit",

                "insurance",

                "holiday",

                "salary",

                "hr"

            ]

        ):

            badge = "📚 Knowledge Base"

            st.session_state.stats["rag_queries"] += 1

        elif any(

            word in p

            for word in [

                "stress",

                "burnout",

                "sleep",

                "sad",

                "anxiety",

                "depressed",

                "tired"

            ]

        ):

            badge = "💡 Recommendation Engine"

            st.session_state.stats["recommendations"] += 1

        st.markdown(

            f"""
<div class="response-header">

{badge}

</div>

""",

            unsafe_allow_html=True

        )

        with st.spinner("🧠 Thinking..."):

            response = engine.process(prompt)

        # ---------------------------------------------
        # Typing Animation
        # ---------------------------------------------

        placeholder = st.empty()

        text = ""

        for word in response.split():

            text += word + " "

            placeholder.markdown(

                f"""
<div class="assistant-card">

{text}

</div>

""",

                unsafe_allow_html=True

            )

            time.sleep(0.015)

    st.session_state.messages.append(

        {

            "role": "assistant",

            "content": response

        }

    )

    st.rerun()


# ======================================================
# FOOTER
# ======================================================

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:

    st.success("🟢 Local LLM")

with col2:

    st.success("📚 Semantic RAG")

with col3:

    st.success("🧠 Memory Enabled")

st.markdown(

"""
<div class="app-footer">

<span class="brand">WorkWell AI v2.0</span><br/>

Powered by Qwen 2.5 + Llama 3.2 + ChromaDB

</div>

""",

unsafe_allow_html=True

)