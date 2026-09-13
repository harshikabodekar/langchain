# pydantic+ with_structured_output used together 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field
load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-3.6-flash')
#schema 
class Review(BaseModel):
    key_themes:list[str]=Field(description="Key themes of the review")
    summery:str= Field(description=" A brief summary of the review")
    sentiment:Literal['pros','cons']=Field(description="The sentiment of the review")
    pros: Optional[str]=Field(default=None,description="Positive aspects of the movie, if any")
    cons: Optional[str]=Field(default=None,description="Negative aspects of the movie, if any")
    name:Optional[str]=Field(default=None,description="Name of the product or movie being reviewed")

structured_model= model.with_structured_output(Review)

result = structured_model.invoke("""
I recently tried the Noise smartwatch and found it to be a decent option for everyday use. The design is sleek, the display is bright, and features like fitness tracking, notifications, and heart-rate monitoring are useful for regular users.

**Pros:**

* Attractive and lightweight design
* Good battery life
* Useful fitness and health-tracking features
* Easy-to-use interface
* Reasonable price for the features offered

**Cons:**

* Some features can feel less accurate compared to premium smartwatches
* App experience could be improved
* Limited options for advanced users

**Overall:** It is a good budget-friendly smartwatch for someone looking for basic fitness tracking and smart features without spending too much.
""")
print(result)
print(result.key_themes)


