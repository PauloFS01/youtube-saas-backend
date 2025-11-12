from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.services.youtube_services import youtube_service

router = APIRouter()

@router.get("/videos/{video_id}")
async def get_video(video_id: str):
    print("test ok!")
    return
    """Busca dados de um vídeo específico"""
    video_data = await youtube_service.get_video_data(video_id)
    
    if not video_data:
        raise HTTPException(status_code=404, detail="Vídeo não encontrado")
    
    return {
        "success": True,
        "data": video_data
    }

@router.get("/videos")
async def search_videos(
    q: str = Query(..., description="Termo de busca"),
    max_results: int = Query(10, description="Número máximo de resultados")
):
    """Busca vídeos no YouTube"""
    videos = await youtube_service.search_videos(q, max_results)
    
    return {
        "success": True,
        "query": q,
        "results": len(videos),
        "data": videos
    }

@router.post("/videos/batch")
async def get_multiple_videos(video_ids: List[str]):
    print("test ok!")
    return
    """Busca dados de múltiplos vídeos"""
    videos_data = []
    
    for video_id in video_ids:
        video_data = await youtube_service.get_video_data(video_id)
        if video_data:
            videos_data.append(video_data)
    
    return {
        "success": True,
        "requested": len(video_ids),
        "found": len(videos_data),
        "data": videos_data
    }