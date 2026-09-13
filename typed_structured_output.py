from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional
load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-3.6-flash')
#schema 
class Review(TypedDict):
    summery:Annotated[str, "A brief summary of the review"] # just to tell LLM that this is a summary of the review and make it understand what it has to do with the text 
    sentiment:str
    pros: Annotated[Optional[str], "Positive aspects of the movie, if any"]
    cons: Annotated[Optional[str], "Negative aspects of the movie, if any"]
structured_model= model.with_structured_output(Review)

result=structured_model.invoke("The movie was entertaining with a good storyline and engaging characters.The pacing was smooth, although a few scenes felt predictable.Overall, it was an enjoyable watch and worth recommending for a relaxed evening.")
print(result)
print(result['summery'])
print(result['sentiment'])

