# pydantic+ with_structured_output used together 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field
load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-3.6-flash')
#schema 
 
json_schema={
    "title":"Review",
    "description":"A review of a product or movie",
    "type":"object",
    "properties":{
        "key_themes":{
            "type":"array",
            "items":{
                "type":"string"
            }
        },
        "summery":{
            "type":"string"
        },
        "sentiment":{
            "type":"string",
            "enum":["pros","cons"]
        },
        "pros":{
            "type":"string"
        },
        "cons":{
            "type":"string"
        },
        "name":{
            "type":"string"
        }
    },
    "required":["key_themes","summery","sentiment"]
}


structured_model= model.with_structured_output(json_schema)

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



