from jose import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

# THIS LINE IS MAGIC (shows Authorize button)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_token(data: dict):
    data.update({"exp": datetime.utcnow() + timedelta(hours=1)})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid or expired token")