#!/usr/bin/env python3
import c
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama
mydata = "LangChain is a framework designed to simplify the creation of applications using large language models. As a language model integration framework, LangChain's use-cases largely overlap with those of language models in general, including document analysis and summarization, chatbots, and code analysis."

summary_template = "given this article `{mydata}`\ncreate a summary of it for non-technical people"

summary_prompt_template = PromptTemplate(input_variables=["mydata"], template=summary_template)

model = Ollama(model="mistral")
res = model.invoke("who is the CEO of Facebook?")
print(res)




