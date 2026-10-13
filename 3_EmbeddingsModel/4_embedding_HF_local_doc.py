from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


documents = ["What is the capital of Pakistan?",
             "What is the capital of India?",
             "What is the capital of Bangladesh?",
             "What is the capital of Sri Lanka?",
             "What is the capital of Nepal?",]


embedding_vector = embeddings.embed_documents(documents)



print(str(embedding_vector))