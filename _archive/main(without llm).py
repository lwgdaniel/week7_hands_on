import streamlit as st  # import Streamlit library

# set the title of the app
st.title("Simple Chatbot")

# initialize session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []  # list of chat messages

# display all previous messages
for msg in st.session_state.messages:
    st.write(msg)

# input box for the user
user_input = st.text_input("You:", "")

# button to send the message
if st.button("Send"):
    # only proceed if user typed something
    if user_input.strip():
        # store user's message
        st.session_state.messages.append(f"You: {user_input}")
        # store bot's response
        st.session_state.messages.append(f"Bot: ok, you have written {user_input}")
        # refresh the interface to show the new messages
        st.rerun()