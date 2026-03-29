from auth import verify_token
from fastapi import Depends

@router.get("/users")
def get_users(
    db: Session = Depends(get_db),
    user=Depends(verify_token)
):
    return db.query(User).all()