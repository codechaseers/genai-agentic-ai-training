
import os
from urllib import response
from click import prompt
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_queries(question):
    prompt = f"""
    Generate 3 different versions of this user question.
    Return only a JSON list.

    Question: {question}
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        print("Gemini API called successfully",response)
        return response.text
    
    except Exception as e:
        print("Error calling Gemini API:", e)
        return None
     
 



question = "What are the steps to hotlist a debit card?"

print(generate_queries(question))