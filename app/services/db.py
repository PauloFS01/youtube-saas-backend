import requests
import json
from fastapi import HTTPException

from app.core.config import settings
from app.models.schemas import SessionContent, SaveImage, SaveScript, SavePlaylist, LoginRequest

class DatabaseSearch:
    def __init__(self):
        self.db_key = settings.DATABASE_KEY
        self.db_url = settings.DATABASE_URL

    async def db_login(self, data: LoginRequest):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "insomnia/12.2.0",
            "apikey": self.db_key
        }
        login_dict = {
            "email": data.email,
            "password": data.password
        }
        try:
            response = requests.post(f"{self.db_url}/auth/v1/token?grant_type=password", headers=headers, json=login_dict)
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail="authentication service error"
                )                
            return {
                "token": response.json().get("access_token", []),
                "expires_at": response.json().get("expires_at", []),
                "user_id": response.json().get("user", []).get("id", " "),
                "refresh_token": response.json().get("refresh_token", [])
            }
        except Exception as e:
            print(f"erro interno: {e}")
            raise            

    async def get_playlists(self, id: str, session: SessionContent):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "insomnia/12.2.0",
            "apikey": self.db_key,
            "authorization": f"Bearer {session["token"]}"
        }
        try:
            response = requests.get(f"{self.db_url}/rest/v1/playlists?select=*", headers=headers)
            if response.status_code != 200:
                raise HTTPException(
                    status_code=500,
                    detail="authentication service error"
                )             
            response_json = response.json()
            return response_json
        except Exception as e:
            print(f"erro interno: ", e)
            raise

    async def get_scripts(self, id: str, session: SessionContent):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "insomnia/12.2.0",
            "apikey": self.db_key,
            "authorization": f"Bearer {session["token"]}"
        }
        try:
            response = requests.get(f"{self.db_url}/rest/v1/scripts?select=*", headers=headers)
            if response.status_code != 200:
                raise HTTPException(
                    status_code=500,
                    detail="authentication service error"
                )             
            response_json = response.json()
            return {
                "scripts": response_json
            }
        except Exception as e:
            print(f"erro interno: ", e)
            raise
        
    async def get_images(self, id: str, session: SessionContent):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "insomnia/12.2.0",
            "apikey": self.db_key,
            "authorization": f"Bearer {session["token"]}"
        }        
        try:
            response = requests.get(f"{self.db_url}/rest/v1/generated_images?", headers=headers)
            if response.status_code != 200:
                raise HTTPException(
                    status_code=500,
                    detail="authentication service error"
                )             
            response_json = response.json()
            return response_json
        except Exception as e:
            print(f"internal error: ", e)
            raise

    async def save_image(self, data: SaveImage, session: SessionContent):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "insomnia/12.2.0",
            "apikey": self.db_key,
            "authorization": f"Bearer {session["token"]}"
        }        
        try:

            response = requests.post(f"{self.db_url}/rest/v1/generated_images", headers=headers, json=data)
            if response.status_code != 200:
                raise HTTPException(
                    status_code=500,
                    detail="authentication service error"
                )             
            response_json = response.json()
            return response_json

        except Exception as e:
            print(f"internal error: ", e)
            raise

    async def save_script(self, data: SaveScript, session: SessionContent):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "insomnia/12.2.0",
            "apikey": self.db_key,
            "authorization": f"Bearer {session["token"]}"
        }        
        try:

            response = requests.post(f"{self.db_url}/rest/v1/scripts", headers=headers, json=data)
            if response.status_code != 200:
                raise HTTPException(
                    status_code=500,
                    detail="authentication service error"
                )             
            response_json = response.json()
            return response_json

        except Exception as e:
            print(f"internal error: ", e)
            raise

    async def save_playlist(self, data: SavePlaylist, session: SessionContent):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "insomnia/12.2.0",
            "apikey": self.db_key,
            "authorization": f"Bearer {session["token"]}"
        }
        try:

            response = requests.post(f"{self.db_url}/rest/v1/playlists", headers=headers, json=data)
            if response.status_code != 200:
                raise HTTPException(
                    status_code=500,
                    detail="authentication service error"
                )             
            response_json = response.json()
            return response_json

        except Exception as e:
            print(f"internal error: ", e)
            raise
