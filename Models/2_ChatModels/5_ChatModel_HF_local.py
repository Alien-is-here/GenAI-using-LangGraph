""" I am using this with Hugging Face pipeline (local model)"""

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',task ="text-generation",pipeline_kwargs={"temperature":0.7,"max_length":512})

model = ChatHuggingFace(llm = llm)

result = model.invoke("What is the capital of Pakistan?")

print(result.content)
