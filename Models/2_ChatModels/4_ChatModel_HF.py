""" I AM DOING IT WITH hUGGING fACE api (Access Token)"""

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("HF_TOKEN")
print("Token loaded:", bool(token))

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    huggingfacehub_api_token=token
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of Pakistan?")
print(result.content)



