from google import genai
from dotenv import load_dotenv
from PIL import Image
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Enter image path
image_path = input("Enter image path: ")

image = Image.open(image_path)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
    "Extract all text from this image.",
    image
]
)

print("\n===== Gemini Response =====")
print(response.text)