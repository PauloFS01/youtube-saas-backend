from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional

router = APIRouter(prefix="/users", tags=["users"])

# mock data
fake_user_db = [
    {"id": 1, "username": "John_doe", "email": "john@example.com"},
    {"id": 2, "username": "jane_smith", "email": "jane@example.com"}
]

@router.get("/")
async def all_users():
    """Return all users"""
    return fake_user_db
    
@router.post("/singup")
async def singup():
    print("singing up")

@router.post("/login")    
async def login():
    print("loging in")