# gives the input as output without any changes 
#useful in certain scenarios where you want to pass the input to the next runnable without any modifications
# only explanation was printed in last two to print the joke we can use runnablepassthrough 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableParallel


load_dotenv()

# passthrough=RunnablePassthrough()
# print(passthrough.invoke(2))
# just to check if it actually works or not 

prompt1=PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)
model=ChatOpenAI(model='gpt-3.5-turbo')
parser=StrOutputParser()

prompt2=PromptTemplate(
    template='Explain the following joke {text}',
    input_variables=['text']

)

joke_gen_chain=RunnableSequence([prompt1, model, parser])

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(joke_gen_chain),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain=RunnableSequence(joke_gen_chain, parallel_chain)
print(final_chain.invoke({'topic':'AI'}))