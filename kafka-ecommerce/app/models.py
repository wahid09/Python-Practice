# app/models.py
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from uuid import UUID, uuid4

class OrderItem(BaseModel):
    product: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)

class Order(BaseModel):
    order_id: UUID = Field(default_factory=uuid4)
    user_id: str
    items: List[OrderItem]
    total_amount: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    status: str = "pending"

    class Config:
        # This makes .dict() and .json() handle UUID and datetime properly
        json_encoders = {
            UUID: str,
            datetime: lambda v: v.isoformat()
        }

    def calculate_tax(self) -> float:
        return round(self.total_amount * 0.1, 2)