# demo ( may have errors )
# this is the base Runnable class which will be used to create all the runnables like LLM, PromptTemplate, OutputParser etc.
from abc import ABC, abstractmethod
import random


class Runnable(ABC):

    @abstractmethod
    def invoke(self, inputs):
        pass


class NakliLLM(Runnable):

    def __init__(self):
        print("LLM Created")

    def invoke(self, prompt):

        response_list = [
            'Delhi is the capital of India.',
            'Mumbai is the capital of Maharashtra.',
            'Kolkata is the capital of West Bengal.',
            'Chennai is the capital of Tamil Nadu.',
        ]

        return random.choice(response_list)

    def predict(self, prompt):

        print("This method will be deprecated in future. Please use invoke method instead")

        response_list = [
            'Delhi is the capital of India.',
            'Mumbai is the capital of Maharashtra.',
            'Kolkata is the capital of West Bengal.',
            'Chennai is the capital of Tamil Nadu.',
        ]

        return random.choice(response_list)


class NakliPromptTemplate(Runnable):

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, inputs):
        return self.template.format(**inputs)


template = NakliPromptTemplate(
    template='write a poem about {topic}',
    input_variables=['topic']
)

print(template.invoke({'topic': 'nature'}))


llm = NakliLLM()

print(llm.predict('What is the capital of India?'))

class NakliStrOutputParser(Runnable):


    def invoke(self, inputs):
        return inputs


class RunnableConnector(Runnable):

    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, inputs):

        for runnable in self.runnable_list:
            inputs = runnable.invoke(inputs)

        return inputs

parser = NakliStrOutputParser()
chain = RunnableConnector([template, llm, parser])

print(chain.invoke({'topic': 'nature'}))


template1 = NakliPromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)

template2=NakliPromptTemplate(
    template=' Explain the following joke {response}',
    input_variables=['response']
)
llm=NakliLLM()
parser=NakliStrOutputParser()
chain1=RunnableConnector([template1,llm])
#chain1.invoke({'topic':'nature'}) manual invoke
chain2=RunnableConnector([template2,llm,parser])
#chain2.invoke({'response':'this is a joke'}) manual invoke
final_chain=RunnableConnector([chain1,chain2])
final_chain.invoke({'topic':'nature'})
