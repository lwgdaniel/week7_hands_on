
##########  setup llm pipe

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('.env')

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_completion_by_messages(messages, model="gpt-4o-mini", temperature=0, top_p=1.0, max_tokens=1024, n=1):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        n=1
    )
    return response.choices[0].message.content

##########  streamlit 

import streamlit as st

# Streamlit App Configuration
st.set_page_config(layout="centered", page_title="CrapGPT")

st.title("a worse version of chatgpt")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# Chat input 
user_prompt = st.text_area("Write some text below...", height=150)

if user_prompt:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Generate model response
    response = get_completion_by_messages(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)