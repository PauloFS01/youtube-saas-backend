from fastapi import APIRouter, HTTPException, Query, Request
from typing import List, Optional

from app.services.youtube import YouTubeService 
from app.services.scraping import ScrapingService
from app.services.db import DatabaseSearch
from app.utils.security import get_decoded_data, token_verify

router = APIRouter(prefix="/youtubeapi", tags=["youtube"])

@router.get("/playlists")
async def get_all_playlists():
    return {
        "success": True,
        "data": []
    }

@router.get("/playlist/{playlist_id}")
async def get_playlist(playlist_id: str, request: Request):
    try:     
        user_token = request.headers.get("Authorization")
        is_valid = token_verify(user_token)
        if not user_token or not is_valid:
            raise HTTPException(status_code=401, detail="Unauthorized")         
        youtube_service = YouTubeService()
        playlists_data = await youtube_service.get_paylist_by_id(playlist_id)
    
        if not playlists_data:
            raise HTTPException(status_code=404, datails= "not found")

        return {
            "success": True,
            "data": playlists_data 
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": {
                "status_code": e.status_code,
                "detail": e.detail,
            } 

        }

@router.get("/playlistitems/{playlist_id}")
async def get_playlist(playlist_id: str, request: Request):
    try: 
        user_token = request.headers.get("Authorization")
        is_valid = token_verify(user_token)
        if not user_token or not is_valid:
            raise HTTPException(status_code=401, detail="Unauthorized")    
        youtube_service = YouTubeService()
        items_data = await youtube_service.get_playlist_items(playlist_id)
        if not items_data:
            raise HTTPException(status_code=404, detail="items não encontrados") 
        
        # print("data: ", items_data)

        return {
            "success": True,
            "data":items_data 
        }

    except Exception as e:
        print("video error: ", e)
        error = 500 
        if hasattr(e, 'status_code'):
            error = e.status_code
        return{
            "success": False,
            "error": error
        } 
    
@router.get("/videos/{video_id}")
async def get_video(video_id: str, request: Request):
    try:
        user_token = request.headers.get("Authorization")    
        is_valid = token_verify(user_token)
        if not user_token or not is_valid:
            raise HTTPException(status_code=401, detail="Unauthorized")      
        youtube_service = YouTubeService()

        video_data = await youtube_service.get_video_by_id(video_id)    
        
        if not video_data:
            raise HTTPException(status_code=404, detail="not found")
        
        return {
            "success": True,
            "data": video_data
        }
    except Exception as e:
        return {
            "success": False,
            "error": e
        }

@router.get("/searchvideos")
async def search_videos(
    request: Request,
    q: str = Query(..., description="Termo de busca"),
    max_results: int = Query(10, description="Número máximo de resultados"),
):
    try: 
        user_token = request.headers.get("Authorization")  
        is_valid = token_verify(user_token)
        if not user_token or not is_valid:
            raise HTTPException(status_code=401, detail="Unauthorized")   
        """Busca vídeos no YouTube"""
        youtube_service = YouTubeService()
        videos = await youtube_service.search_videos(q, max_results)
        
        return {
            "success": True,
            "query": q,
            "results": len(videos),
            "data": videos,
        }
        
    except Exception as e:
        print("error: ", e)
        return {
            "success": False,
            "error": e
        }

@router.get("/transcription/{video_id}")
async def get_transcription(video_id: str, request: Request):
    try:
        user_token = request.headers.get("Authorization")
        is_valid = token_verify(user_token)
        if not user_token or not is_valid:
            raise HTTPException(status_code=401, detail="Unauthorized")
        scraping = ScrapingService()
        transcription = await scraping.get_transcription(video_id)
        return{
            "success": True,
            "data": transcription
        }
    except Exception as e:
        return{
            "success": False,
            "data": e
        }