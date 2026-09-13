from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-3.5-turbo')
prompt=PromptTemplate(
    template='write a  5 line summery on {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()

# Use the exact full path to where your file actually lives
loader = TextLoader(
    r"C:\Users\harsh\OneDrive\Desktop\langchain\RAG\Document_loader\random.txt", 
    encoding="utf-8"
)

docs = loader.load()
print(docs[0].page_content)

print(len(docs))
print(docs[0].metadata)

chain=prompt|model|parser
print(chain.invoke({'topic':docs[0].page_content}))