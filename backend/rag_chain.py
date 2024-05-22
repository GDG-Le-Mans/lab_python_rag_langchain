from typing import List
from operator import itemgetter
from typing import TypedDict

from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community import embeddings
from langchain_together.embeddings import TogetherEmbeddings
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFDirectoryLoader
import os
import time
import textwrap
from config import GROQ_API_KEY
from config import TOGETHER_API_KEY

os.environ["TOGETHER_API_KEY"] = TOGETHER_API_KEY

# INGEST : chargement des docs et embedding dans base vector

pdf_loader = DirectoryLoader('../data/', glob="**/*.pdf")
txt_loader = DirectoryLoader('../data/', glob="**/*.txt")
word_loader = DirectoryLoader('../data/', glob="**/*.docx")

loaders = [pdf_loader, txt_loader, word_loader]
documents = []
for loader in loaders:
    documents.extend(loader.load())

print(f"Total number of documents: {len(documents)}")  

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)   

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=TogetherEmbeddings(model="togethercomputer/m2-bert-80M-8k-retrieval"),
)
retriever = vectorstore.as_retriever()     



# LLM : definition du modele pour une inférence sur groq

llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name='mixtral-8x7b-32768'
    )

class RagQuestion(TypedDict):
    question: str

rag_template = """Answer the question, in french, based only on the following context:
{context}
Question: {question}
"""
rag_prompt = ChatPromptTemplate.from_template(rag_template)
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
    | StrOutputParser()
).with_types(input_type=RagQuestion)