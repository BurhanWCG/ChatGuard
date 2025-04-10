from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFaceHub
from decouple import config
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VECTOR_STORE_PATH = os.path.join(BASE_DIR, "embeddings", "vector_store")

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = FAISS.load_local(VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True)

huggingface_api_token = config('HUGGINGFACEHUB_API_TOKEN')
llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-Instruct-v0.1",
    huggingfacehub_api_token=huggingface_api_token,
    model_kwargs={"temperature": 0.7, "max_new_tokens": 512, "top_p": 0.9}
)

prompt_template = """
You are a helpful customer service assistant. Use the following context to answer the user's question.
If the context does not contain the answer, say "Sorry, I don’t have that information right now."

Context: {context}

User: {question}

Answer123:
"""

prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=False,
    chain_type_kwargs={"prompt": prompt}
)

def get_response(user_input):
    try:
        response = qa_chain.run(user_input)
        if "Answer123:" in response:
            answer_only = response.split("Answer123:")[1].strip()
            return answer_only
        else:
            return response.strip()

    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

