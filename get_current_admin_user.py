from fastapi import Depends, HTTPException
from app.dependencies.auth import get_current_user

def get_current_admin_user(current_user = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return current_user
