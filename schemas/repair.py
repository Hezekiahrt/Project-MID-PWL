from pydantic import BaseModel
from typing import List

class RepairJobBase(BaseModel):
    device_name: str
    issue: str
    cost: float
    status: str = "Pending"

class RepairJobCreate(RepairJobBase):
    customer_id: int

class RepairJob(RepairJobBase):
    id: int
    class Config:
        from_attributes = True

class CustomerCreate(BaseModel):
    name: str
    phone: str

class Customer(BaseModel):
    id: int
    name: str
    phone: str
    jobs: List[RepairJob] = []
    class Config:
        from_attributes = True