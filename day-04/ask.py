from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

db = Chroma(
    persist_directory="day-04/chroma_db",
    embedding_function=embeddings
)
retriever = db.as_retriever(
    search_kwargs={"k": 3}
)
question = "What are the steps to hotlist a debit card?"

docs = retriever.invoke(question)
print("Chroma DB loaded successfully")

print("\nRetrieved documents:")

for doc in docs:
    print("--------------------------------")
    print("Source:", doc.metadata.get("source"))
    print(doc.page_content)