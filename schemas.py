"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Association-specific schemas

class MemberApplication(BaseModel):
    """
    Collection: "memberapplication" -> applications from students who want to join
    """
    name: str = Field(..., description="Full name of the applicant")
    email: EmailStr = Field(..., description="Applicant email")
    year: Literal["1st", "2nd"] = Field(..., description="BTS MCO year")
    motivation: str = Field(..., min_length=10, description="Motivation message")

class ContactMessage(BaseModel):
    """
    Collection: "contactmessage" -> general contact form submissions
    """
    name: str = Field(..., description="Sender name")
    email: EmailStr = Field(..., description="Sender email")
    message: str = Field(..., min_length=5, description="Message body")

# Example schemas (kept for reference)
class User(BaseModel):
    name: str
    email: str
    address: str
    age: Optional[int] = None
    is_active: bool = True

class Product(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    category: str
    in_stock: bool = True
