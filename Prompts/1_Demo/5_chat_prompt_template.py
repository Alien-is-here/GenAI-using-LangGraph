from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage 

#chat_template = ChatPromptTemplate (
 #   ("system", 'You are a helpful {domain} expert')

#)

chat_template = ChatPromptTemplate.from_messages ([
        ("system", """
         You are an expert in {domain}.
        Extract these details from the user's message:
        - Domain
        - Topic
        - Skill level
        - User's request
        Return the result clearly.
        """),
        ("human", "{user_message}")
    ])

user_input = input("You: ")
prompt = chat_template.invoke({"user_message":user_input})

print(prompt)