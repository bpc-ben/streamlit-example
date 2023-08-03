from langchain.chains.api.prompt import API_RESPONSE_PROMPT
from langchain.chains import APIChain
from langchain.prompts.prompt import PromptTemplate


from langchain.llms import OpenAI

llm = OpenAI(temperature=0,openai_api_key="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")

from langchain.chains.api import open_meteo_docs
chain_new = APIChain.from_llm_and_api_docs(llm, open_meteo_docs.OPEN_METEO_DOCS, verbose=True)