import typer
from typing import Optional, List
from phi.assistant import Assistant  # Independent AI -> Will assist for different things
from phi.storage.assistant.postgres import PgAssistantStorage  # For storage
from phi.knowledge.pdf import PDFKnowledgeBase  # Reading the content of the PDF
from phi.vectordb.pgvector import PgVector  # For vector database integration

import os
from dotenv import load_dotenv

# Load environment variable
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

# Setting up the DB URL
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

# Creating the Knowledge Base
knowledge_base = PDFKnowledgeBase(

    urls=["https://drive.google.com/file/d/1-8cvK7BJ4WFQ73mUxn7qW9MIDPNim00k/view?usp=drive_link"],  # Add links to resumes here 1. Riddhima's Resume 
    path="./pdf_storage",  # Specify a directory to store or read the PDFs
    vector_db=PgVector(db_url=db_url, table_name="Resume")  # Vector DB integration
)

# Load the knowledge base
knowledge_base.load()

# Setting up storage for the assistant
storage = PgAssistantStorage(table_name="Resume_assistant", db_url=db_url)

# Configure Groq API
groq_api = Groq(api_key=groq_api_key)  # Initialize Groq API with the API key

def pdf_assistant(new: bool = False, user: str = "user", run_id: Optional[str] = None):
    if not new:
        # Get existing run IDs
        existing_run_ids: List[str] = storage.get_all_run_ids(user)
        if len(existing_run_ids) > 0:
            run_id = existing_run_ids[0]

    # Create the assistant instance with Groq API
    assistant = Assistant(
        run_id=run_id,
        user_id=user,
        knowledge_base=knowledge_base,
        storage=storage,
        api=groq_api,  # Use Groq API explicitly
        # Show tool calls in the response
        show_tool_calls=True,
        # Enable the assistant to search the knowledge base
        search_knowledge=True,
        # Enable the assistant to read the chat history
        read_chat_history=True,
    )

    # Handle run ID and provide feedback
    if run_id is None:
        run_id = assistant.run_id
        print(f"Started Run: {run_id}\n")
    else:
        print(f"Continuing Run: {run_id}\n")

    # Start the assistant CLI app
    assistant.cli_app(markdown=True)


if __name__ == "__main__":
    typer.run(pdf_assistant)
