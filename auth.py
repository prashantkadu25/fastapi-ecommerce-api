from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "secret"
ALGORITHM = "HS256"

def create_token(data: dict):
    data.update({"exp": datetime.utcnow() + timedelta(hours=1)})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)