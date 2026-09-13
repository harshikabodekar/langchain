#  convert python function into runnable
# to check if it works we will create a simple function that counts the number of words in a string and then convert it into a runnable using RunnableLambda.
# def word_count(text):
#     return len(text.split())

# word_count_runnable = RunnableLambda(word_count)
# print(word_count_runnable.invoke("Hello world! This is a test."))  # Output: 6
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnableParallel,RunnablePassthrough

load_dotenv()
def word_count(text):
    return len(text.split())

prompt=PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)
model=ChatOpenAI(model='gpt-3.5-turbo')
parser=StrOutputParser()

joke_gen_chain=RunnableSequence([prompt, model, parser])

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    word_count:RunnableLambda(word_count)
})
# parallel_chain=RunnableParallel({
#     'joke': RunnablePassthrough(),
#     'word_count': RunnableLambda(lambda x: len(x.split())) another menthod
#  })
final_chain=RunnableSequence([joke_gen_chain, parallel_chain])
# print(final_chain.invoke({'topic':'AI'}))
result =(final_chain.invoke({'topic':'AI'}))

final_result=""" {} \n word count: {}""".format(final_chain.invoke({'topic':'AI'})['joke'],final_chain.invoke({'topic':'AI'})['word_count'])
print(final_result)





