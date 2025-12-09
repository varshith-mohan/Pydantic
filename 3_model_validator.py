!pip install pydantic

from pydantic import BaseModel, field_validator, model_validator, computed_field # type: ignore


class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, name):
        if len(name) < 4:
            raise ValueError('Username must be at least 4 characters')
        return name


class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Password do not match')
        return values
 # After validators: run after the whole model has been validated. As such, they are defined as instance methods and can be seen as post-initialization hooks.
 # Important note: the validated instance should be returned.


class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    # computed_field and property is used to define fields whose values are calculated dynamically based on other fields within the model.
    #These fields are treated like regular attributes when accessed, but their values are computed "on request" and are included in serialization (when using model_dump()).