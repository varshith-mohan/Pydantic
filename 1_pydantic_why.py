from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    #Type: String Validation: Must be ≤ 50 characters Metadata: Title, description, example values (used in FastAPI docs) Annotated: Combines str type with Field configuration.
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['deva', 'varada'])]
    email: EmailStr #Must be a valid email.
    linkedin_url: AnyUrl #Must be a valid URL
    age: int = Field(gt=0, lt=120) #Must be integer Must be greater than 0 Must be less than 120 "23" (string) will be converted to 23  "abc" → Validation error
    weight: Annotated[float, Field(gt=0, strict=True)] #Must be float, "87.2" (string) →  not allowed because strict=True, 87.2 (float) allowed,  Must be > 0
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')] # Boolean value (True/False) Default = None If user does not pass it → married = None
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)] #Optional → can be None or a list of strings Max length of list = 5 items Examples: ["dust", "pollen"]
    contact_details: Dict[str, str] # Must be a dictionary with: key = string, value = string


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')
    # This function accepts a Patient object, not a dictionary.
    # Pydantic already validated everything before this function is called.

# Input data
patient_info = {'name':'varshith', 'email':'gvm@gmail.com', 'linkedin_url':'http://linkedin.com/13854', 'age': '23', 'weight': 87.2,'contact_details':{'phone':'2353462'}}

# Creating Patient object
patient1 = Patient(**patient_info) #** unpacks dictionary keys/values into the model.

# Calling the update function
update_patient_data(patient1)
