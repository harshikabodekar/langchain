from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.6-flash')
result=model.invoke("What is the capital of India?")
# If result.content returns a list of dicts:
text_output = result.content[0]["text"]
print(text_output)
