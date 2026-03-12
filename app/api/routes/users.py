from datetime import datetime, timedelta
import secrets

from fastapi import APIRouter, HTTPException, Query, Request
from typing import List, Optional

from app.services.db import DatabaseSearch
from app.utils.security import create_access_token, get_decoded_data, token_verify
from app.models.schemas import LoginRequest, SaveImage, SavePlaylist, SaveScript

router = APIRouter(prefix="/users", tags=["users"])

SESSION_STORE = {}

@router.get("/")
async def all_users():
    """Return all users"""
    return {
        "success": True,
        "data": [SESSION_STORE]
    }
    
@router.post("/singup")
async def singup():
    return {
        "success": True,
        "data": []
    }

@router.post("/login")    
async def login(request: Request):
    database = DatabaseSearch()
    try:
        raw_data:LoginRequest  = await request.json()
        data = LoginRequest(**raw_data)
        res = await database.db_login(data)
        user_token = create_access_token(res)
        return{
            "success": True,
            "user_id": res["user_id"],
            "expires_at": res["expires_at"],
            "authorization": user_token
        }
    except Exception as e:
        error = 500
        if hasattr(e, 'status_code'):
            error = e.status_code 
        return{
            "success": False,
            "error": error
        }

@router.get("/playlists/{user_id}")
async def get_playlists(user_id: str, request: Request):
    database = DatabaseSearch()
    try: 
        user_token = request.headers.get("Authorization")
        is_valid = token_verify(user_token)
        if not user_token or not is_valid:
            raise HTTPException(status_code=401, detail="Token inválido")
        decoded_data = get_decoded_data(user_token)
        # print("i am here: ", decoded_data)
        if user_id != decoded_data['user_id']:
            raise HTTPException(status_code=401, detail="Unauthorized")        
        res = await database.get_playlists(user_id, decoded_data)
        # res = []
        return{
            "success": True,
            "data": res
        }
    except Exception as e:
        error = 500 
        if hasattr(e, 'status_code'):
            error = e.status_code
        return{
            "success": False,
            "error": error
        }        

@router.get("/images/{user_id}")
async def get_images(user_id: str, request: Request):

    database = DatabaseSearch()
    try:
        user_token = request.headers.get("Authorization")
        is_valid = token_verify(user_token)
        if not user_token or not is_valid:
            raise HTTPException(status_code=401, detail="Token inválido")    
        decoded_data = get_decoded_data(user_token)
        if user_id != decoded_data['user_id']:
            raise HTTPException(status_code=401, detail="Unauthorized")        
        res = await database.get_images(user_id, decoded_data)
        return{
            "success": True,
            "data":res
        }
    except Exception as e:
        return{
            "success": False,
            "error": e.status_code
        }        

@router.get("/scripts/{user_id}")
async def get_scripts(user_id: str, request: Request):
    database = DatabaseSearch()
    try:
        user_token = request.headers.get("Authorization")
        is_valid = token_verify(user_token)
        if not user_token or not is_valid:
            raise HTTPException(status_code=401, detail="Token inválido")
        decoded_data = get_decoded_data(user_token)
        if user_id != decoded_data['user_id']:
            raise HTTPException(status_code=401, detail="Unauthorized")
        res = await database.get_scripts(user_id, decoded_data)
        return{
            "success": True,
            "data": res
        }
    except Exception as e: 
        return{
            "success": False,
            "error": e.status_code
        }        

@router.post("/playlist")
async def save_playlist(playlist: SavePlaylist, request: Request):
    database = DatabaseSearch()
    try:
        user_token = request.headers.get("Authorization")
        is_valid = token_verify(user_token)
        if not user_token or not is_valid:
            raise HTTPException(status_code=401, detail="Token error")      
        decoded_data = get_decoded_data(user_token)
        if user_id != decoded_data['user_id']:
            raise HTTPException(status_code=401, detail="Unauthorized")        
        res = await database.save_playlist(playlist, decoded_data)
        return {
            "success": True,
            "data": res 
        }
    except Exception as e:
        return{
            "success": False,
            "error": e.status_code 
        }        

@router.post("/image")    
async def save_image(image: SaveImage, request: Request):
    database = DatabaseSearch()
    try:
        user_token = request.headers.get("Authorization")
        is_valid = token_verify(user_token)
        if not user_token or not is_valid:
            raise HTTPException(status_code=401, detail="Token inválido")       
        decoded_data = get_decoded_data(user_token)
        if user_id != decoded_data['user_id']:
            raise HTTPException(status_code=401, detail="Unauthorized")        
        res = await database.save_image(image, decoded_data)
        return{
            "success": True,
            "data": res 
        }

    except Exception as e:
        return{
            "success": False,
            "error": e.status_code 
        }

@router.post("/script")    
async def save_script(script: SaveScript, request: Request):
    database = DatabaseSearch()
    try: 
        user_token = request.headers.get("Authorization")
        is_valid = token_verify(user_token)
        if not user_token or not is_valid:
            raise HTTPException(status_code=401, detail="Token inválido")      
        decode_data = get_decoded_data(user_token)
        if user_id != decoded_data['user_id']:
            raise HTTPException(status_code=401, detail="Unauthorized")        
        res = await database.save_script(script, decode_data)
        return{
            "success": True,
            "data": res 
        }
        
    except Exception as e:
        return{
            "success": False,
            "error": e.status_code 
        }