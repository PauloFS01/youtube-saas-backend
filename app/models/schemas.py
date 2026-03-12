from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str

class SaveImage(BaseModel):
    user_id: str
    image_url: str    

class SaveScript(BaseModel):
    user_id: str
    content: str

class SavePlaylist(BaseModel):
    user_uuid: str
    title: str
    description: str
    thumbnail: str        

class SessionContent(BaseModel):
    token: str
    expires_at: int
    user_id: str
    refresh_token: str    