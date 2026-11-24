
import streamlit as st
from s4_agent import agent as s4_agent
from s5_tool import agent as s5_agent

# Page configuration
st.set_page_config(
    page_title="Agentic AI Studio",
    page_icon="🤖",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
}
.main-title {
    font-size: 38px;
    font-weight: bold;
    color: #8b9cff;
}
.subtitle {
    color: #a0a0a0;
    font-size: 16px;
}
.stChatMessage {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🤖 Agentic AI")
    st.caption("AI Assistant Dashboard")

    st.divider()

    selected_agent = st.selectbox(
        "Choose Your Agent",
        [
            "S4 - Web Search Agent",
            "S5 - Tool Agent"
        ]
    )

    st.divider()

    st.markdown("### Available Features")

    if selected_agent.startswith("S4"):
        st.success("Weather Tool")
        st.success("Web Search")
    else:
        st.success("Weather Tool")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Select agent
if selected_agent.startswith("S4"):
    current_agent = s4_agent
else:
    current_agent = s5_agent

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Main header
st.markdown(
    '<div class="main-title">🤖 Agentic AI Studio</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your intelligent AI assistant with tools and web search.</div>',
    unsafe_allow_html=True
)

st.divider()

st.info(f"Currently using: {selected_agent}")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Ask anything...")

if user_input:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Run agent
    with st.chat_message("assistant"):
        with st.spinner("AI is thinking..."):

            try:
                result = Runner.run_sync(
                    current_agent,
                    user_input
                )

                response = result.final_output

                st.markdown(response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

            except Exception as e:
                st.error(f"Error: {str(e)}")