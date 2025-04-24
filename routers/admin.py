from fastapi import APIRouter, Depends
from dependencies.auth import get_current_admin_user
from models.user import User

router = APIRouter()

@router.get("/admin/dashboard")
def admin_dashboard(current_user: User = Depends(get_current_admin_user)):
    return {
        "message": "歡迎來到管理員專區",
        "admin": current_user.email
    }
