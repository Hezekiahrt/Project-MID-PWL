from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import database, auth.security as security
from models.repair import Customer, RepairJob
from schemas.repair import CustomerCreate, Customer as CustomerSchema, RepairJobCreate, RepairJob as JobSchema

router = APIRouter(tags=["Repair Management"])

# --- CUSTOMER ENDPOINTS ---
@router.post("/customers/", response_model=CustomerSchema, status_code=status.HTTP_201_CREATED)
def create_customer(customer: CustomerCreate, db: Session = Depends(database.get_db), current_user=Depends(security.get_current_user)):
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@router.get("/customers/", response_model=List[CustomerSchema])
def get_customers(db: Session = Depends(database.get_db)):
    return db.query(Customer).all()

# --- REPAIR JOB ENDPOINTS ---
@router.post("/jobs/", response_model=JobSchema, status_code=status.HTTP_201_CREATED)
def create_repair_job(job: RepairJobCreate, db: Session = Depends(database.get_db), current_user=Depends(security.get_current_user)):
    # Cek apakah customer id valid
    db_customer = db.query(Customer).filter(Customer.id == job.customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
        
    db_job = RepairJob(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("/jobs/", response_model=List[JobSchema])
def get_repair_jobs(db: Session = Depends(database.get_db)):
    return db.query(RepairJob).all()

@router.delete("/jobs/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(job_id: int, db: Session = Depends(database.get_db), current_user=Depends(security.get_current_user)):
    db_job = db.query(RepairJob).filter(RepairJob.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail="Repair job not found")
    db.delete(db_job)
    db.commit()
    return None