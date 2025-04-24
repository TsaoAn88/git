from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.schemas.task import TaskCreate, TaskUpdate
from app.crud import task as crud
import logging
from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas.task import TaskCreate, TaskUpdate
from crud import task as crud

logger = logging.getLogger(__name__)  # 用模組名稱作為 logger 名稱

def create_task_service(db: Session, task_data: TaskCreate):
    task = crud.create_task(db, task_data)
    logger.info(f" 建立任務 [id={task.id}] title='{task.title}'")
    return task

def list_tasks_service(db: Session):
    logger.info(" 查詢任務列表")
    return crud.get_tasks(db)

def get_task_service(db: Session, task_id: int):
    task = crud.get_task_by_id(db, task_id)
    if not task:
        logger.warning(f" 查無任務 [id={task_id}]")
        raise HTTPException(status_code=404, detail="Task not found")
    logger.info(f"🔍 查詢任務成功 [id={task_id}]")
    return task

def update_task_service(db: Session, task_id: int, update_data: TaskUpdate):
    updated_task = crud.update_task(db, task_id, update_data)
    if not updated_task:
        logger.warning(f" 無法更新，任務不存在 [id={task_id}]")
        raise HTTPException(status_code=404, detail="Task not found")
    logger.info(f" 任務已更新 [id={task_id}]")
    return updated_task

def delete_task_service(db: Session, task_id: int):
    deleted = crud.delete_task(db, task_id)
    if not deleted:
        logger.warning(f" 刪除失敗，任務不存在 [id={task_id}]")
        raise HTTPException(status_code=404, detail="Task not found")
    logger.info(f" 任務已刪除 [id={task_id}]")
    return {"message": "Task deleted"}


def create_task_service(db: Session, task_data: TaskCreate):
    return crud.create_task(db, task_data)

def list_tasks_service(db: Session):
    return crud.get_tasks(db)

def get_task_service(db: Session, task_id: int):
    task = crud.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

def update_task_service(db: Session, task_id: int, update_data: TaskUpdate):
    updated_task = crud.update_task(db, task_id, update_data)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

def delete_task_service(db: Session, task_id: int):
    deleted = crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
