import streamlit as st

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")
if 'openai_api_key' not in st.session_state:
    st.session_state.openai_api_key = ""
st.session_state.openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password",value=st.session_state.openai_api_key)



prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")