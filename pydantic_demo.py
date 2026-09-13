from pydantic import BaseModel,Field
from typing import Optional

#validation of data using pydantic
class Student(BaseModel):

    name:str ='Harshika'# for default value
    age:Optional[int] = None # in case no value then none
    #email:EmailStr # to validate email address
    cgpa:float = Field(gt=0,lt=10,default=5,description ='CGPA must be between 0 and 10') # to validate cgpa between 0 and 10
new_student ={'age':'20','email':'harshika@example.com','cgpa':'8.5'} #{'name':"Harshika"}

student = Student(**new_student)
print(student)
#print(type(student))
#print(student.name)
student_dict = dict(student)
print(student_dict['age'])
student_json =student.model_dump_json() # to convert to json format
print(student_json)
#understands the data provided =coerces the data to the correct type