from langchain_openai import OpenAIEmbeddings
from loadenv import dot_loadenv


dot_loadenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = ["What is the capital of Pakistan?",
             "What is the capital of India?",
             "What is the capital of Bangladesh?",
             "What is the capital of Sri Lanka?",
             "What is the capital of Nepal?",]

embedding_vector = embeddings.embed_documents(documents)

print(str(embedding_vector))