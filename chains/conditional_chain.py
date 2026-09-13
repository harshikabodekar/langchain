from typing import Literal
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableBranch,
    RunnableLambda,
    RunnableParallel,
)
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description=" Give the sentiment of the feedback text"
    )


parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative\n{feedback} \n {format_instruction}",
    input_variables=["feedback"],  # Added missing comma here
    partial_variables={"format_instruction": parser2.get_format_instructions()},
)

# Chain 1: Returns a Feedback Pydantic object
classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template="write an appropriate response to this positive feedback text. \n{feedback}",
    input_variables=["feedback"],
)
prompt3 = PromptTemplate(
    template="write an appropriate response to this negative feedback text. \n{feedback}",
    input_variables=["feedback"],
)

# To pass the original feedback text along with the sentiment to the branches,
# we bundle them together using RunnableParallel / RunnablePassthrough or dict mapping
prepare_branch_input = RunnableLambda(
    lambda x: {"sentiment": x.sentiment, "feedback": "I love this product!"}
)

branch_chain = RunnableBranch(
    (lambda x: x["sentiment"] == "positive", prompt2 | model | parser),
    (lambda x: x["sentiment"] == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "couldnt find sentiment"),
)

chain = classifier_chain | prepare_branch_input | branch_chain

result = chain.invoke({"feedback": "I love this product!"})
print(result)

#visualize chain 
chain.get_graph().print_ascii()
