from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "What is the capital of Pakistan?"

embedding_vector = embeddings.embed_query(text)

print(str(embedding_vector))