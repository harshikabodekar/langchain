from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()
model1=ChatGoogleGenerativeAI(model='gemini-3.6-flash')
model2=ChatAnthropic(model='claude-3-5-sonnet-20241022')

prompt1=PromptTemplate(
    template='Generate short and simple notes from the following text. \n{text}',
    input_variables=['text']
)

prompt2=PromptTemplate(
    template='Generate 5 short answers from the following text. \n{text}',
    input_variables=['text']
)
prompt3=PromptTemplate(
    template='Merge the provided notes and quize into a single document.\nNotes: {notes}\nQuiz: {quiz}',
    input_variables=['notes','quiz']
)
parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'notes': prompt1|model1|parser,
    'quiz': prompt2|model2|parser
})
merge_chain=prompt3|model1|parser

chain=parallel_chain|merge_chain
text='''The Great Wall of China is a series of fortifications that were built across the historical northern borders of China to protect against invasions and raids. The wall stretches over 13,000 miles and was constructed over several dynasties, with the most well-known sections built during the Ming Dynasty. It is made of various materials, including stone, brick, tamped earth, and wood. The Great Wall is not a single continuous wall but rather a collection of walls and fortifications that were built at different times. It is considered one of the greatest architectural feats in history and is a UNESCO World Heritage Site. The wall also served as a means of border control, allowing for the imposition of duties on goods transported along the Silk Road, regulation of trade, and control of immigration and emigration. Today, the Great Wall of China is a popular tourist destination and a symbol of China's historical strength and perseverance.'''

result=chain.invoke({'text':text})
print(result)
#visualize chain 
chain.get_graph().print_ascii()
