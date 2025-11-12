import requests
from typing import List, Dict, Optional
from app.core.config import settings

class YouTubeService:
    def __init__(self):
        self.api_key = settings.YOUTUBE_API_KEY
        self.base_url = "https://www.googleapis.com/youtube/v3"
    
    async def get_video_data(self, video_id: str) -> Optional[Dict]:
        """Busca dados básicos de um vídeo"""
        url = f"{self.base_url}/videos"
        params = {
            "part": "snippet,statistics,contentDetails",
            "id": video_id,
            "key": self.api_key
        }
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            if data.get("items"):
                video = data["items"][0]
                return {
                    "id": video_id,
                    "title": video["snippet"]["title"],
                    "description": video["snippet"]["description"],
                    "thumbnail": video["snippet"]["thumbnails"]["high"]["url"],
                    "view_count": video["statistics"].get("viewCount", 0),
                    "like_count": video["statistics"].get("likeCount", 0),
                    "duration": video["contentDetails"]["duration"]
                }
            return None
        except Exception as e:
            print(f"Erro ao buscar vídeo: {e}")
            return None
    
    async def search_videos(self, query: str, max_results: int = 10) -> List[Dict]:
        """Busca vídeos por termo"""
        url = f"{self.base_url}/search"
        params = {
            "part": "snippet",
            "q": query,
            "type": "video",
            "maxResults": max_results,
            "key": self.api_key
        }
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            videos = []
            for item in data.get("items", []):
                videos.append({
                    "id": item["id"]["videoId"],
                    "title": item["snippet"]["title"],
                    "description": item["snippet"]["description"],
                    "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
                    "published_at": item["snippet"]["publishedAt"]
                })
            
            return videos
        except Exception as e:
            print(f"Erro na busca: {e}")
            return []

youtube_service = YouTubeService()