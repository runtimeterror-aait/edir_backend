from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import create_database

# routers
from app.routers.v1 import auth, edir, event, member, payment, user

app = FastAPI()

create_database()

origins = [
    "*"
]

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Verson 1 api routers

app.include_router(auth.router)
app.include_router(edir.router)
app.include_router(event.router)
app.include_router(member.router)
app.include_router(payment.router)
app.include_router(user.router)