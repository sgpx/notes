from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

model_id = "mistralai/Mistral-7B-v0.1"

pipeline = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task="text-generation",
    device=0,
    pipeline_kwargs={"max_new_tokens": 20},
)

llm = HuggingFacePipeline(pipeline=pipeline)

template = """<s>[INST] You are a helpful, respectful and honest assistant. Answer exactly in few words from the context
Answer the question below from context below :
{context}
{question} [/INST] </s>
"""

question_p = """What is the date for announcement"""
context_p = """ On August 10 said that its arm JSW Neo Energy has agreed to buy a portfolio of 1753 mega watt renewable energy generation capacity from Mytrah Energy India Pvt Ltd for Rs 10,530 crore."""
prompt = PromptTemplate(template=template, input_variables=["question","context"])
llm_chain = LLMChain(prompt=prompt, llm=llm)
response = llm_chain.run({"question":question_p,"context":context_p})
print(response)
