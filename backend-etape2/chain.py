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


pdf_loader = DirectoryLoader('../data/', glob="**/*.pdf")
txt_loader = DirectoryLoader('../data/', glob="**/*.txt")
word_loader = DirectoryLoader('../data/', glob="**/*.docx")

loaders = [pdf_loader, txt_loader, word_loader]
documents = []
for loader in loaders:
    documents.extend(loader.load())

####################
# A COMPTETER
#text_splitter = 
#vectorstore = Chroma.from_documents(
    #....
# )