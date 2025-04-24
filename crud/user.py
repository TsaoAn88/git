from sqlalchemy.orm import Session
from models.user import User
from schemas.user_create import UserCreate

#SELECT * FROM users;
def get_users(db: Session):
    return db.query(User).all()

#SELECT * FROM users WHERE id = {user_id} LIMIT 1;
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

#INSERT INTO users (name, email, age) VALUES (...);
def create_user(db: Session, user: UserCreate):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#UPDATE users SET name = ..., email = ..., age = ... WHERE id = {user_id};
def update_user(db: Session, user_id: int, update_data: dict):
    user = get_user_by_id(db, user_id)
    for key, value in update_data.items():
        setattr(user, key, value)
    db.commit()
    return user

#delete_user(db: Session, user_id: int)
def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    db.delete(user)
    db.commit()
