from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate , MessagePlaceholder
from langchain_core.messages import SystemMessage , HumanMessage


model = ChatOpenAI("")
chat_template = ChatPromptTemplate.from_messages ([
    ('system', 'You are a helpful Customer Support Agent'),
    MessagePlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

prompt = chat_template.invoke({'chat_history':chat_history, 'query':  'Where is my order?' })

result = model.invoke(prompt)

print(result.content)