from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv


load_dotenv()

model = ChatAnthropic(model_name="claude-v1", temperature=0)
result = model.invoke("Tell a story about a rabbit and a turtle.")
print(result.content)