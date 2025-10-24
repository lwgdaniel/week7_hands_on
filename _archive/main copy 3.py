
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

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="CrapGPT"
)
# endregion <--------- Streamlit App Configuration --------->

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


input_container = st.container()

with input_container:

    # Input area
    form = st.form(key="form")
    user_prompt = form.text_area("write some text below", height=300)

    if form.form_submit_button("Submit"):
        if user_prompt.strip():
            # Store user message
            st.session_state.messages.append({"role": "user", "content": user_prompt})
            st.chat_message("user").write(user_prompt)

            # Generate model response
            response = get_completion_by_messages(st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": response})

            # Display model response
            st.chat_message("assistant").write(response)

    print(st.session_state.messages)