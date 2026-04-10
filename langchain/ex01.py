from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Define components
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
model = ChatOpenAI(model="gpt-5-turbo")
parser = StrOutputParser()

# Compose with pipe operator (|)
chain = prompt | model | parser

# Invoke
result = chain.invoke({"topic": "programming"})
print(result)  # "Why did the programmer quit?..."
