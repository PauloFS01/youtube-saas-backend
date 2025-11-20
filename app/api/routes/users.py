from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional

router = APIRouter()

@router.post("/singup")
async def singup():
    print("singing up")

@router.post("/login")    
async def login():
    print("loging in")