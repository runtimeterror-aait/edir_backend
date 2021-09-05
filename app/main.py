from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import create_database

# routers
from app.routers.v1 import auth, edir, event, member, payment, user

app = FastAPI()

async def common_parameters(id: str, name: str, age: int):
    if id is "1":
        return {"message": "You suck"}
    else:
        return { "id": id, "name": name, "age": age}

@app.get("/user/")
async def user(commons = Depends(common_parameters)):
    return commons

@app.get("/admin/")
async def admin(commons = Depends(common_parameters)):
    return commons
# create_database()

# origins = [
#     "*"
# ]

# # origins = [
# #     "http://localhost.tiangolo.com",
# #     "https://localhost.tiangolo.com",
# #     "http://localhost",
# #     "http://localhost:8080",
# # ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(auth.router)
# app.include_router(edir.router)
# app.include_router(event.router)
# app.include_router(member.router)
# app.include_router(payment.router)
# app.include_router(user.router)