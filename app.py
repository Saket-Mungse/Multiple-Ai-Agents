import streamlit as st
from pipeline import run_pipeline

st.set_page_config(page_title="Multi-Agent AI", page_icon="🤖", layout="wide")

st.title("🤖 Multi-Agent AI System")

# Agent mapping
agent_options = {
    "Career Agent": "career",
    "Diet Agent": "diet",
    "Summary Agent": "summary",
    "Coding Agent": "coding",
    "Image Generation Agent": "image"
}

# Sidebar
st.sidebar.title("Select Agent")
selected_agent_name = st.sidebar.selectbox(
    "Choose an Agent",
    list(agent_options.keys())
)

agent_type = agent_options[selected_agent_name]

# Initialize chat history for all agents
if "chat_history" not in st.session_state:
    st.session_state.chat_history = {
        "career": [],
        "diet": [],
        "summary": [],
        "coding": [],
        "image": []
    }

# Get current agent messages
current_messages = st.session_state.chat_history[agent_type]

# Display previous messages of selected agent
for message in current_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Ask your question...")

if user_input:
    # Save user message
    st.session_state.chat_history[agent_type].append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    response = run_pipeline(agent_type, user_input)

    # Save assistant response
    st.session_state.chat_history[agent_type].append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)



# Clear all chats
if st.sidebar.button("❌ Clear All Chats"):
    st.session_state.chat_history = {
        "career": [],
        "diet": [],
        "summary": [],
        "coding": [],
        "image": []
    }
    st.rerun()