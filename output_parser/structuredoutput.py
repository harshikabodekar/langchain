# no data validation is done in this output parser. It just parses the output to pydantic model and then we can use it in next prompt.
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers.structured import StructuredOutputParser, ResponseSchema

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.6-flash')

schema =[
    ResponseSchema(name="fact1",description="first fact about topic"),
    ResponseSchema(name="fact2",description="second fact about topic"),
    ResponseSchema(name="fact3",description="third fact about topic"),
]
parser =StructuredOutputParser.from_response_schemas(schema)
template =PromptTemplate(
    template='write 3 facts about {topic} \n {format-instructions}',
    input_variables=['topic'],
    partial_variables={'format-instructions':parser.get_format_instructions()}
)
chain= template | model | parser
result=chain.invoke({'topic':'black hole'})
print(result)
# prompt=template.invoke({'topic':'black hole'})
# result =model.invoke(prompt)
# final_result= parser.invoke(result.content)
# print(final_result)