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
