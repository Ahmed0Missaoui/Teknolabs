from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
import os
load_dotenv()
cle = os.getenv("GROQ_API_KEY")
modele = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.3,
    max_tokens=500,
    api_key=cle
)
chargeur = TextLoader("documents.txt")
documents = chargeur.load()
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vecteurs = FAISS.from_documents(documents, embeddings)
chaine_rag = RetrievalQA.from_chain_type(llm=modele, retriever=vecteurs.as_retriever())

reponse = chaine_rag.invoke("Qu'est-ce que LangChain ?")
print(reponse['result'])

