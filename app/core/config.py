import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    APP_NAME: str = "YouTube SaaS API"
    DEBUG: bool = os.getenv("DEBUG", False)
    
    # YouTube API Config
    YOUTUBE_API_KEY: str = os.getenv("YOUTUBE_API_KEY", "")
    YOUTUBE_BASE_URL: str = os.getenv("YOUTUBE_BASE_URL", "")

    # Webshare proxy config
    WEBSHARE_PROXY_USER: str = os.getenv("WEBSHARE_USER",)
    WEBSHARE_PROXY_PASS: str = os.getenv("WEBSHARE_PASS")
    
    # CORS
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "")
    
    # Database
    DATABASE_URL: str = os.getenv("SUPABASE_PROJECT_URL", "")
    DATABASE_KEY: str = os.getenv("SUPABASE_PUBLISHABLE_API_KEY", "")
    DATABASE_SECRET_KEY: str = os.getenv("SUPABASE_SECRET_KEY", "")

    # jwt
    TOKEN_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "")
    TOKEN_ALGORITHM = os.getenv("ALGORITHM", "")
    EXPIRES = os.getenv("ACCESS_TOKEN_EXPIRES_MINUTES")

    class Config:
        env_file = ".env"

settings = Settings()