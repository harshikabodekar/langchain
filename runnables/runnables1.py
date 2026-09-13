# to show that this is not flexiable  enough to use in real world everytime 
#dummy LLM for testing purpose
import random
class NakliLLM:
    def __init__(self):
        print("LLM Created")
    def predict(self,prompt):

        response_list=[
            'Delhi is the capital of India.',
            'Mumbai is the capital of Maharashtra.',
            'Kolkata is the capital of West Bengal.',
            'Chennai is the capital of Tamil Nadu.',
        ]
        return random.choice(response_list)
llm=NakliLLM()
llm.predict('What is the capital of India?')


# dummy for prompt template
class NakliPromptTemplate:
    def __init__(self,template,input_variables):
        self.template=template
        self.input_variables=input_variables
    def invoke(self,inputs):
        return self.template.format(**inputs)
template=NakliPromptTemplate(template='write a poem about {topic}',
                             input_variables=['topic'])
# template.invoke({'topic':'nature'})
prompt=template.invoke({'topic':'nature'})
llm=NakliLLM()
llm.predict(prompt)
# building demo chain 

class NakliChain:
    def __init__(self,llm,prompt):
        self.llm=llm
        self.prompt=prompt 
    def run(self,inputs):
        final_prompt=self.prompt.invoke(inputs)
        return self.llm.predict(final_prompt)

chain=NakliChain(llm=llm,prompt=template)
result=chain.run({'topic':'nature'})
print(result)


