import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

customer_message = """
My debit card is lost. Please block it immediately.
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"""
You are a banking customer-service intent classifier.

Classify this customer message:

{customer_message}

Return JSON containing:
- intent
- urgency
- language
"""
)

print(response.text)