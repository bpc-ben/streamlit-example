from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun
import streamlit as st

st.set_page_config(page_title="LangChain: Chat with search", page_icon="🦜")
st.title("🦜 LangChain: Chat with search")


from langchain.chains.api.prompt import API_RESPONSE_PROMPT
from langchain.chains import APIChain
from langchain.prompts.prompt import PromptTemplate


from langchain.llms import OpenAI

llm = OpenAI(temperature=0,openai_api_key="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")

# Function to find competitor names
def get_competitor_names():

    pass


if 'openai_api_key' not in st.session_state:
    st.session_state.openai_api_key = ""
st.session_state.openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password",value=st.session_state.openai_api_key)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Please enter your brand name:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    if not st.session_state.openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k-0613", openai_api_key=st.session_state.openai_api_key, streaming=True)
    search_agent = initialize_agent(
        tools=[DuckDuckGoSearchRun(name="Search")],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
    )
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)