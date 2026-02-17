from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

# Import database session creator and engine
from .database import SessionLocal, engine

# Import models and schemas
from . import models
from . import schemas


# This creates the database tables if they don't already exist
models.Base.metadata.create_all(bind=engine)


# Create FastAPI application instance
app = FastAPI()


# ---------------------------
# DATABASE SESSION DEPENDENCY
# ---------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------
# ROOT ENDPOINT
# ---------------------------
@app.get("/")
def read_root():
    return {"message": "CodePulse API running"}


# ---------------------------
# CREATE DEVELOPER (JSON BODY)
# ---------------------------
@app.post("/developers", response_model=schemas.DeveloperResponse)
def create_developer(dev: schemas.DeveloperCreate, db: Session = Depends(get_db)):

    # Create SQLAlchemy model using validated request data
    new_dev = models.Developer(name=dev.name, skill=dev.skill)

    db.add(new_dev)
    db.commit()
    db.refresh(new_dev)

    return new_dev


# ---------------------------
# GET ALL DEVELOPERS
# ---------------------------
@app.get("/developers", response_model=list[schemas.DeveloperResponse])
def get_developers(db: Session = Depends(get_db)):

    developers = db.query(models.Developer).all()

    return developers
