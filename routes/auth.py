from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from auth import create_token, verify_password
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user:
        return {"error": "User not found"}

    if not verify_password(form_data.password, user.password):
        return {"error": "Invalid password"}

    token = create_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}