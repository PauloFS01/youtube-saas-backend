import requests
from typing import List, Dict, Optional
from app.core.config import settings

class YouTubeService:
    def __init__(self):
        self.api_key = settings.YOUTUBE_API_KEY
        self.base_url = settings.YOUTUBE_BASE_URL 

    async def get_paylist_by_id(self, playlist_id: str ):
        search_url = f"{self.base_url}/playlists"
        params = {
            "part": "snippet,contentDetails",
            "id": playlist_id,
            "key": self.api_key
        }
        try:
            response = requests.get(search_url, params=params)
            items = response.json().get("items", [])
            
            if len(items) > 0:
                return {
                    "playlist_id": playlist_id,
                    "title": items[0]["snippet"]["title"],
                    "description": items[0]["snippet"]["description"],
                    "thumbnail": items[0]["snippet"]["thumbnails"]["high"]["url"],
                }
                
        except Exception as e:
            print("erro ao buscar playlists")

    async def get_playlist_items(self, playlist_id: str) -> Optional[Dict]:
        search_url = f"{self.base_url}/playlistItems"
        params = {
            "part": "snippet",
            "playlistId": playlist_id,
            "key": self.api_key
        }
        try:
            response = requests.get(search_url, params=params) 
            items = response.json().get("items",[])

            videos = []
            for item in items:
                videos.append({
                    "title": item["snippet"]["title"],
                    "description": item["snippet"]["description"],
                    "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
                    "video_id": item["snippet"]["resourceId"]["videoId"]
                })
            return videos
        except Exception as e:
            print("Erro ao buscar items", e)

    async def get_video_by_id(self, video_id: str) -> Optional[Dict]:
        """Busca dados básicos de um vídeo"""
        url = f"{self.base_url}/videos"
        params = {
            "part": "snippet,contentDetails",
            "id": video_id,
            "key": self.api_key
        }
        
        try:
            response = requests.get(url, params=params)
            items = response.json().get("items", [])
            
            if len(items) > 0:
                return {
                "video_id": video_id,
                "description": items[0]["snippet"]["description"],
                "title": items[0]["snippet"]["title"],
                "tags": items[0].get("snippet", {}).get("tags", "none"),        
                "thumbnail": items[0]["snippet"]["thumbnails"]["high"]["url"],
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
            items = response.json().get("items", [])
            
            videos = []
            for item in items:
                videos.append({
                    "id": item["id"]["videoId"],
                    "title": item["snippet"]["title"],
                    "description": item["snippet"]["description"],
                    "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
                })
            
            return videos 
            
        except Exception as e:
            print(f"Erro na busca: {e}")
            return []

# youtube_service = YouTubeService()