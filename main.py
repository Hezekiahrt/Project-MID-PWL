from fastapi import FastAPI
import database
from models.repair import Base as RepairBase
from models.user import Base as UserBase
from routers import auth, repair

# Inisialisasi Database
RepairBase.metadata.create_all(bind=database.engine)
UserBase.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Repair Shop API",
    description="Sistem Monitoring Perbaikan Gadget untuk UTS Pemweb Lanjutan",
    version="1.0.0"
)

# Registrasi Router Modular
app.include_router(auth.router)
app.include_router(repair.router)

@app.get("/")
def read_root():
    return {
        "status": "Online",
        "message": "Gadget Repair Monitoring API is running",
        "documentation": "/docs"
    }