from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    
    # Relasi One-to-Many
    jobs = relationship("RepairJob", back_populates="owner", cascade="all, delete-orphan")

class RepairJob(Base):
    __tablename__ = "repair_jobs"
    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String)
    issue = Column(String)
    status = Column(String, default="Pending")
    cost = Column(Float)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    
    owner = relationship("Customer", back_populates="jobs")