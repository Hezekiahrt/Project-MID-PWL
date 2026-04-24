from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import database, auth.security as security
from models.user import User as UserModel
from models.repair import Customer as CustomerModel, RepairJob as JobModel, Base
from schemas.user import UserCreate, Token
from schemas.repair import CustomerCreate, Customer, RepairJobCreate, RepairJob
from typing import List

app = FastAPI(title="Repair Shop API")

# Inisialisasi Tabel
Base.metadata.create_all(bind=database.engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# --- AUTH ---
@app.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(database.get_db)):
    hashed_pw = security.get_password_hash(user.password)
    new_user = UserModel(username=user.username, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    access_token = security.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(UserModel).filter(UserModel.username == form_data.username).first()
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = security.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# --- CUSTOMER CRUD ---
@app.post("/customers/", response_model=Customer, status_code=status.HTTP_201_CREATED)
def create_customer(customer: CustomerCreate, db: Session = Depends(database.get_db)):
    db_customer = CustomerModel(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.get("/customers/", response_model=List[Customer])
def get_customers(db: Session = Depends(database.get_db)):
    return db.query(CustomerModel).all()

# --- REPAIR JOB CRUD (PROTECTED) [cite: 32] ---
@app.post("/jobs/", response_model=RepairJob, status_code=status.HTTP_201_CREATED)
def create_job(job: RepairJobCreate, db: Session = Depends(database.get_db), token: str = Depends(oauth2_scheme)):
    db_job = JobModel(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@app.delete("/jobs/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(job_id: int, db: Session = Depends(database.get_db), token: str = Depends(oauth2_scheme)):
    db_job = db.query(JobModel).filter(JobModel.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    db.delete(db_job)
    db.commit()
    return None