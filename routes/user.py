from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from schemas import UserCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    return {"msg": "User created"}

# READ
@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# DELETE
@router.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    db.delete(user)
    db.commit()
    return {"msg": "Deleted"}