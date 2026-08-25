from dotenv import load_dotenv

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

print(load_dotenv())
load_dotenv()

# loading 10 documents from the knowledge base... 

docs = DirectoryLoader(
    "day-04/kb",
    glob="*.txt",
    loader_cls=TextLoader
).load()

print(f"Loaded {len(docs)} documents")

# chunk the  folder into smaller chunks for better processing and indexing. and also overlap means suppose in first chunk we have 500 characters, then the next chunk will start from 450th character to 950th character. This is done to ensure that we don't lose any context between chunks.

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

print(f"Created {len(chunks)} chunks")

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)
db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="day-04/chroma_db"
)

print(f"Stored {len(chunks)} chunks in Chroma")