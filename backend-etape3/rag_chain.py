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

####################
# A COMPTETER
#definition de l'embedding 
#vectorstore
# definition du retriever
#retriever = 
#definition du llm
#llm 
#definition du template 
#rag_template = 
# #rag_prompt = 
#rag_chain = 