from typing import List
from uuid import UUID
import uvicorn
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role, UserUpdateRequest


app = FastAPI()

db: List[User] = [
    User(
        #if let id=uuid4 whenver i run the code it'll show a different id, so this way i can hardcode in order to keep always the same id
        #id=uuid4(),
        id=UUID("d9be2a9d-1361-44ee-9ec9-af2bc3e44e80"),
        first_name="luis",
        last_name="nogueira",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
         #if let id=uuid4 whenver i run the code it'll show a different id, so this way i can hardcode in order to keep always the same id
        #id=uuid4(),
        id=UUID("5830c3f3-d758-41a8-8c8e-32169f884174"),
        first_name="eduardo",
        last_name="santos",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

#{user_id} isto no codigo é um path variable
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exists"
        )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id:UUID):
    for user in db:
        if user.id ==user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name =user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
        raise HTTPException(
            status_code = 404,
            detail =f"user with id {user_id} does not exists"
        )
