from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):   # This validates the email field.

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com     # Splits email to get domain Example: "abc@icici.com" --> "icici.com"
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:  #"abc@icici.com" --> valid  "user@gmail.com" --> invalid → throws error
            raise ValueError('Not a valid domain')

        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):  # Converts the user’s name to uppercase, always.
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod  # Pydantic first converts "30" --> 30 (int), THEN your validation checks the numeric value.
    def validate_age(cls, value):
        if 0 < value < 100:
            return value   # Allowed ages: 1 to 99,  Not allowed: -10, 0, 100, 150 --> error
        else:
            raise ValueError('Age should be in between 0 and 100')


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'teja', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)

# ** is called dictionary unpacking.
# It expands a dictionary into key = value pairs when passing arguments to a function or class.