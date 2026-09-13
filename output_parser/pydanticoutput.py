from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.6-flash')

class Person(BaseModel):
    name:str=Field(description="name of the person")
    age:int=Field(gt=18,description="age of the person")
    city:str=Field(description="city of the person")
parser=PydanticOutputParser(pydantic_object=Person)
template=PromptTemplate(
    template='Generate the name , age and city of a fictional {place} person \n{format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
# prompt=template.invoke({'place':'India'})
# result=model.invoke(prompt)

# final_result=parser.invoke(result.content)
# print(final_result)
chain= template|model|parser
result=chain.invoke({'place':'Sri Lanka'})
print(result)
