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
#definition du LLM
# llm =
# définition du prompt
# prompt = 
# définition = de la langchain
# chain =

chat = ChatGroq(temperature=0, groq_api_key="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", model_name="mixtral-8x7b-32768")
system = "You are a french helpful assistant."
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

chain = prompt | chat