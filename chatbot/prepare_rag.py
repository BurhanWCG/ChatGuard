import pandas as pd
import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.docstore.document import Document

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLEANED_DATA_PATH = os.path.join(BASE_DIR, "data", "chat_data_cleaned.csv")
VECTOR_STORE_PATH = os.path.join(BASE_DIR, "embeddings", "vector_store")

if not os.path.exists(CLEANED_DATA_PATH):
    raise FileNotFoundError("Cleaned dataset not found!")
df = pd.read_csv(CLEANED_DATA_PATH)

if df.empty:
    raise ValueError("Cleaned dataset is empty!")

documents = [
    Document(page_content=row["text"], metadata={"instruction": row["instruction"], "response": row["response"]})
    for _, row in df.iterrows()
]

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vector_store = FAISS.from_documents(documents, embeddings)
vector_store.save_local(VECTOR_STORE_PATH)

print(f"FAISS vector store saved at {VECTOR_STORE_PATH}")
