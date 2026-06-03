from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

document = """
Python is a high-level programming language.

It is used for:
- Web Development
- Data Science
- Artificial Intelligence
"""

question = input("Ask a question: ")

prompt = f"""
Answer the question using ONLY the information below.

Document:
{document}

Question:
{question}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)