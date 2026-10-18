#!/usr/bin/env python3
import c
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

mydata = "LangChain is a framework designed to simplify the creation of applications using large language models. As a language model integration framework, LangChain's use-cases largely overlap with those of language models in general, including document analysis and summarization, chatbots, and code analysis."

summary_template = "given this article `{mydata}`\ncreate a summary of it for non-technical people"

summary_prompt_template = PromptTemplate(input_variables=["mydata"], template=summary_template)

llm = ChatOpenAI(model_name="gpt-3.5-turbo")
chain = LLMChain(llm = llm, prompt = summary_prompt_template)
res = chain.invoke(input={"mydata": mydata})

print(res)




