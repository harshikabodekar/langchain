# to make conditional chain 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnableParallel,RunnablePassthrough,RunnableBranch

load_dotenv()
prompt1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='write a 5 line summery on the following text. \n{text}',
    input_variables=['text']
)
model=ChatOpenAI(model='gpt-3.5-turbo')
parser=StrOutputParser()

report_gen_chain=RunnableSequence([prompt1, model, parser])
# report_gen_chain=prompt1|model|parser -> LCEL 

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>500 , RunnableSequence(prompt2, model,parser)), # 1st if condition
    RunnablePassthrough() # default condition or else condition
)
final_chain=RunnableSequence([report_gen_chain, branch_chain])

print(final_chain.invoke({'topic':'AI'}))

