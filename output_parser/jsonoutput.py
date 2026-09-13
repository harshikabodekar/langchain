# cant tell the schema of the output so we are using stroutputparser to parse the output as string and then we can use it in next prompt.
# #json cant give structured outtput like fact1 --- 
# fact2---
# fact3----
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.6-flash')

parser=JsonOutputParser()

template=PromptTemplate(
    template="Give me 5 facts about{topic} \n {format_instructution} ",
    input_variables=['topic'],
    partial_variables={'format_instructution': parser.get_format_instructions()}
    )
chain= template | model | parser
result=chain.invoke({'topic':'black hole'})
print(result)

# prompt =template.format()
# result=model.invoke(prompt)
# final_result=parser.invoke(result)

# print(final_result)
# print(type(final_result))