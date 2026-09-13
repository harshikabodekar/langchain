# output parse is used when llm cant understand the schema and it returns a string output instead of structured output.

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.6-flash')


#1st prompt - detailed report 
template1=PromptTemplate(
    template=" write a detailed report on {topic}",
    input_variables=['topic']
)

#2nd promt - summery 
template2=PromptTemplate(
    template=" write a 5 line summery on the following text. /n {text}",
    input_variables=['text']
)

#template 1 to prompt 
prompt1 =template1.invoke({'topic':'black hole'})
result =model.invoke(prompt1)
#print(result)
#template 2 to prompt
prompt2 =template2.invoke({'text':result.content})
model2 = model.invoke(prompt2)
print(model2.content)