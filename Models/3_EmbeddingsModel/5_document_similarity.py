from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    """
    Artificial Intelligence enables machines to perform tasks that usually require human intelligence.
    Machine learning is a major branch of artificial intelligence.
    It allows computers to learn patterns from data.
    Deep learning uses neural networks with multiple layers.
    AI is used in healthcare, education, and finance.
    Chatbots use AI to answer questions and assist users.
    Responsible AI development is important for society.
    """,

    """
    Pakistan is a country located in South Asia.
    Islamabad is the capital city of Pakistan.
    Pakistan gained independence on 14 August 1947.
    Urdu is the national language of Pakistan.
    The country has four provinces.
    The northern areas are famous for their mountains.
    Agriculture and industry contribute to its economy.
    """,

    """
    Python is a popular programming language.
    It is known for its simple and readable syntax.
    Python is widely used in artificial intelligence.
    Developers use libraries such as NumPy and pandas.
    LangChain helps developers build applications with language models.
    Embeddings represent text as numerical vectors.
    These vectors can help find semantically similar documents.
    """
]

query = "What is Python in programming?"

embedded_documents = embeddings.embed_documents(documents)
embedded_query = embeddings.embed_query(query)

similarities = cosine_similarity([embedded_query], embedded_documents)

print("Similarities:")
for i, similarity in sorted(enumerate(similarities[0]), key=lambda x: x[1], reverse=False):
    print(f"Document {i + 1}: {similarity:.4f}")
