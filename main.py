from fastapi import FastAPI
from routers import user,auth
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from middlewares.logging import LoggingMiddleware
# main.py
from middlewares.logging_middleware import LoggingMiddleware
app.add_middleware(LoggingMiddleware)

from core.logging_config import setup_logging

setup_logging()
app = FastAPI()
app.add_middleware(LoggingMiddleware)

app = FastAPI()

# CORS 設定（如果你有前端要串）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 可限制前端來源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 註冊路由
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"message": "Welcome to the API!"}
