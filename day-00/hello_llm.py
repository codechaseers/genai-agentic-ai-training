# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()
# client = OpenAI()  # reads OPENAI_API_KEY from the environment

# resp = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role": "user",
#                "content": "Say hello to a new AI engineering trainee in one sentence."}],
# ) 

# print("------------------------------- >>>>>>>>>>>>>>>>>> ")
# # print(resp.choices[0].message.content)
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Say hello to a new AI engineering trainee in one sentence."
)

print("------------------------------- >>>>>>>>>>>>>>>>>>")
print(response.text)