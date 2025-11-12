from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "YouTube SaaS API"
    DEBUG: bool = os.getenv("DEBUG", False)
    
    # YouTube API Config
    YOUTUBE_API_KEY: str = os.getenv("YOUTUBE_API_KEY", "")
    YOUTUBE_BASE_URL: str = os.getenv("YOUTUBE_BASE_URL", "")
    
    # CORS
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "")
    
    class Config:
        env_file = ".env"

settings = Settings()