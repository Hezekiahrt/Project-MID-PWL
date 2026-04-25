from pydantic import BaseModel
from typing import List, Optional

class RepairJobBase(BaseModel):
    device_name: str
    issue: str
    cost: float
    status: str = "Pending"

class RepairJobCreate(RepairJobBase):
    customer_id: int

class RepairJob(RepairJobBase):
    id: int
    customer_id: int
    class Config:
        from_attributes = True

class CustomerBase(BaseModel):
    name: str
    phone: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    jobs: List[RepairJob] = []
    class Config:
        from_attributes = True