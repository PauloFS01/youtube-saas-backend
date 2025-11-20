from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import videos
from app.api.routes import users

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