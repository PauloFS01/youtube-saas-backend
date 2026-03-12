from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes import videos
from app.api.routes import users
from app.utils.security import create_access_token, get_decoded_data

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[settings.FRONTEND_URL],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(videos.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "YouTube SaaS API está rodando!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/token")
async def token_test(data: dict):
    encoded = create_access_token(data)
    return encoded

@app.post("/detoken")
async def decode_test(data: dict):
    decoded = get_decoded_data(data)
    return decoded