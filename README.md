# 🛡️ ChatGuard

ChatGuard is a Retrieval-Augmented Generation (RAG) chatbot system that leverages LangChain, Hugging Face models, and vector databases to deliver domain-specific question-answering from a custom dataset.
It preprocesses and indexes your dataset with FAISS, retrieves relevant context, and generates accurate, context-aware answers LLMs.

---

## 🌟 Features

- **Data Cleaning & Preparation:** 
  - Loads a customer support dataset, cleans text fields, and merges instructions with responses into a single searchable text.
- **Vector Database Creation:**
  - Converts cleaned data into vector embeddings using `all-MiniLM-L6-v2` via LangChain's HuggingFaceEmbeddings.
  - Stores embeddings locally in a FAISS vector store for fast retrieval.
- **RAG Chatbot Pipeline:**
  - Uses LangChain's `RetrievalQA` chain with a prompt template to combine retrieved context and user questions.
  - Generates answers using Hugging Face’s hosted Mistral-7B model through `HuggingFaceHub`.
- **Django Integration:**
  - Exposes a simple Django view to receive user questions via POST requests and return chatbot responses as JSON.
- **Error Handling:**
  - Robust checks for missing or empty datasets, malformed CSVs, or other runtime issues.

---


---

## 🛠️ Technologies Used

| Core Frameworks    | NLP & Vector Search    | Web & Tools        |
|--------------------|------------------------|--------------------|
| Django             | LangChain              | VS Code            |
|                    | HuggingFace Transformers |                   |
|                    | FAISS                  |                    |
|                    | Elasticsearch (for advanced search, optional) |  |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Node.js and npm (if you plan to expand frontend features)
- [Hugging Face Hub API Token](https://huggingface.co/settings/tokens)
- (Optional) Docker, if you wish to containerize




