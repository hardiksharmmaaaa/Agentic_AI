# In this particular Usecase, WE gonna make a KB of Resumes and from that we will use agentic AI 

import typer 
from typing import Optional
from phi.assistant import assistant  # its like independent AI -> Will assist for diff things 
from phi.storage.assistant.postgres import PgAssistantStorage # for storage 
from phi.knowledge.pdf import PDFKnowledgeBase  # reading the content of the PDF 
from phi.vectordb.pgvector import PgVector, SearchType

import os 
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

#Setting up the Db url
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

#creating the Knowledge base 
knowledge_base=PDFKnowledgeBase(
    urls=[""]   ## will add the links of the resumes here 
)


