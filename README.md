# Pydantic
Pydantic is a Python library used to validate and parse data using Python type hints. It ensures the data you receive (from API requests, JSON files, databases, etc.) is clean, correct, and in the expected format.  Pydantic is heavily used in FastAPI, data pipelines, ML model configs, and backend systems.

| Reason                       | Meaning                                                             |
| ---------------------------- | ------------------------------------------------------------------- |
| **1. Automatic Validation**  | Ensures data is correct (type, format, constraints).                |
| **2. Auto Conversion**       | Converts types when possible (e.g `"123"` → `123`).               |
| **3. Easy Error Handling**   | Gives human-readable and structured validation errors.              |
| **4. Works with Type Hints** | Uses Python typing like `str`, `int`, `List[int]` to define schema. |
| **5. Prevents bugs**         | Ensures only valid data enters your application.                    |
| **6. Used by FastAPI**       | Every request/response model in FastAPI depends on Pydantic.        |

***

~~~
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

u = User(name="varshith", age="25", email="v@example.com")
print(u)
~~~

- "25" gets auto-converted to 25 (int) <br>
- If age="twenty" -> validation error<br>
- If email missing -> error<br>

***

~~~
from pydantic import BaseModel, validator

class Product(BaseModel):
    name: str
    price: float

    @validator("price")
    def check_price(cls, v):
        if v <= 0:
            raise ValueError("Price must be positive")
        return v

p = Product(name="Laptop", price=45000)
~~~

- If price = -10 then Pydantic throws custom validation error.

***

## Pydantic Usecases 

1. FastAPI request/response models - FastAPI automatically validates API input using Pydantic.
2. Data Cleaning in ML / ETL pipelines - Ensures your ML pipeline never receives corrupted data.
3. Configuration Management - Automatically reads from environment variables.

## Pydantic = Type-safe, auto-validating data models for Python.
It protects your application by ensuring all incoming data is valid, structured, and correctly typed.

1. Define a Pydantic model that represents the ideal schema of the data.
   • This includes the expected fields, their types, and any validation constraints (e.g gt=e for positive numbers).
2. Instantiate the model with raw input data (usually a dictionary or JSON-like structure).
   • Pydantic will automatically validate the data and coerce it into the correct Python types (if possible).
   • If the data doesn't meet the model's requirements, Pydantic raises a ValidationError .
3. pass the validated model object to functions or use it throughout your codebase
   • This ensures that every part of your program works with clean, type-safe, and logically valid data.

## Why these are used?

- BaseModel → Base class for all Pydantic models. Provides validation and parsing.
- EmailStr → Validates email format automatically.
- AnyUrl → Validates a URL string (HTTP/HTTPS etc.).
- Field → Adds validation rules, metadata (title, description, examples).
- Annotated → Used to combine Python type with Pydantic Field configuration.
- List, Dict, Optional → Type hinting for complex data structures.



