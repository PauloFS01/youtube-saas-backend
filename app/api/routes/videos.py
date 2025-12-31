from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.services.youtube import YouTubeService 
from app.services.scraping import ScrapingService
router = APIRouter()

mock = [
      {
        "playlist_id": "PLaQhQgENCDLGhF5gd23fxK0o8vYS_GvRv",
        "title": "Saúde suplementos",
        "description": "lista de videos curiosos de ciencia",
        "thumbnail": "https://i.ytimg.com/vi/iQE8RLvIk2k/hqdefault.jpg",
      },   
      {
        "playlist_id": "PLaQhQgENCDLGhF5gd23fxK0o8vYS_GvRv",
        "title": "Saúde suplementos",
        "description": "lista de videos curiosos de ciencia",
        "thumbnail": "https://i.ytimg.com/vi/iQE8RLvIk2k/hqdefault.jpg",
      },  
      {
        "playlist_id": "PLaQhQgENCDLGhF5gd23fxK0o8vYS_GvRv",
        "title": "Saúde suplementos",
        "description": "lista de videos curiosos de ciencia",
        "thumbnail": "https://i.ytimg.com/vi/iQE8RLvIk2k/hqdefault.jpg",
      },  
      {
        "playlist_id": "PLaQhQgENCDLGhF5gd23fxK0o8vYS_GvRv",
        "title": "Saúde suplementos",
        "description": "lista de videos curiosos de ciencia",
        "thumbnail": "https://i.ytimg.com/vi/iQE8RLvIk2k/hqdefault.jpg",
      },                    
]

@router.get("/playlists")
async def get_all_playlists():
    return {
        "success": True,
        "data": mock
    }

@router.get("/playlists/{playlist_id}")
async def get_playlist(playlist_id: str):
    youtube_service = YouTubeService()
    playlists_data = await youtube_service.get_paylist_by_id(playlist_id)
    
    if not playlists_data:
        raise HTTPException(status_code=404, datails= "Playlist não encontradas")

    return {
        "success": True,
        "data": playlists_data # object
    }

@router.get("/playlistitems/{playlist_id}")
async def get_playlist(playlist_id: str):
    print(playlist_id)
    youtube_service = YouTubeService()

    items_data = await youtube_service.get_playlist_items(playlist_id)
    if not items_data:
        raise HTTPException(status_code=404, datail="items não encontrados") 

    return {
        "success": True,
        "data":items_data 
    }
    
@router.get("/videos/{video_id}")
async def get_video(video_id: str):
    """Busca dados de um vídeo específico"""
    youtube_service = YouTubeService()

    video_data = await youtube_service.get_video_by_id(video_id)    
    
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
    youtube_service = YouTubeService()
    videos = await youtube_service.search_videos(q, max_results)
    
    return {
        "success": True,
        "query": q,
        "results": len(videos),
        "data": videos,
    }

@router.get("/transcription/{video_id}")
async def get_transcription(video_id: str):
    scraping = ScrapingService()
    try:
        transcription = await scraping.get_transcription(video_id)
        return{
            "success": True,
            "data": transcription
        }
    except:
        return{
            "success": False,
            "data": None
        }