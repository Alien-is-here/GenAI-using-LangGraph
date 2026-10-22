from langchain_google_gemini import ChatGoogleGenerativeGemini
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeGemini(model_name="gemini-1.5-turbo", temperature=0)
result = model.invoke("Tell a story about a rabbit and a turtle.")

print(result.content)