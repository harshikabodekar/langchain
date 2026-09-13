from langchain_core.messages import  HumanMessage, AIMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.6-flash')
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about Langchain "),
   
]
result = model.invoke(messages)
# If result.content returns a list of dicts:
messages.append(AIMessage(content=result.content[0]["text"]))
print(messages)

