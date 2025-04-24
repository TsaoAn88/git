from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.task import TaskSchema, TaskCreate, TaskUpdate
from services import task_service
from utils.response import api_response

router = APIRouter()

@router.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    task_obj = task_service.create_task_service(db, task)
    return api_response(data=task_obj, message="Task created")

@router.get("/tasks")
def list_tasks(db: Session = Depends(get_db)):
    return api_response(data=task_service.list_tasks_service(db))

@router.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_task_service(db, task_id)
    return api_response(data=task)

@router.put("/tasks/{task_id}")
def update_task(task_id: int, update: TaskUpdate, db: Session = Depends(get_db)):
    task = task_service.update_task_service(db, task_id, update)
    return api_response(data=task, message="Task updated")

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return api_response(
        data=task_service.delete_task_service(db, task_id),
        message="Task deleted"
    )
