from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model = "all-MiniLM-L6-v2"

)

texts = [
    "Hello this is Pratik Chavan",
    "Hello your name is youtube",
    "And you are very beautiful"
]

vector = embedding.embed_documents(texts)

print(vector)