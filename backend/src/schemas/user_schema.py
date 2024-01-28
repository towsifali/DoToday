from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="Email of the user")
    username: str = Field(..., min_length=5, max_length=50,
                          description="Username of the user")
    password: str = Field(..., min_length=5, max_length=24,
                          description="Password of the user")
