from langchain_openai import OpenAIEmbeddings
from loadenv import dot_loadenv


dot_loadenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

embedding_vector = embeddings.embed_query("What is the capital of Pakistan?")

print(str(embedding_vector))