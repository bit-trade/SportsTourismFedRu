from typing import Optional
from fastapi import FastAPI
from data import PerevalRead, PerevalCreate


pereval = FastAPI()


@pereval.post('/pereval/', response_model=PerevalRead)
def submitData(data: PerevalRead):
    pass








# # Эндпоинт для создания пользователя
# @pereval.post("/users/", response_model=UserResponse)
# def create_user(user: UserCreate, db: SessionLocal = next(get_db())):
#     db_user = User(name=user.name, age=user.age)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
# # Эндпоинт для получения всех пользователей
# @pereval.get("/users/", response_model=list[UserResponse])
# def read_users(skip: int = 0, limit: int = 10, db: SessionLocal = next(get_db())):
#     users = db.query(User).offset(skip).limit(limit).all()
#     return users
#
# # Эндпоинт для получения пользователя по ID
# @pereval.get("/users/{user_id}", response_model=UserResponse)
# def read_user(user_id: int, db: SessionLocal = next(get_db())):
#     user = db.query(User).filter(User.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
