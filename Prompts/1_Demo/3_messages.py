from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_openai import ChatOpenAI
from loadenv import load_dotenv

load_dotenv()

model = ChatopenAI("")

messages = [
    SystemMessage(content= "You are a senior AI Assistant")
]

user_input = input("You: ")
user_message = messages.append(HumanMessage(content=user_input))

result = model.invoke(user_message)
messages.append(AIMessage(content=result.content))

print(messages)