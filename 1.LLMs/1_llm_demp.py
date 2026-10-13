from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = OpenAI(model_name="text-davinci-003")


result = llm.invoke("What is the capital of Pakistan?")

print(result)

