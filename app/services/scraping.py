# use youtube-transcription-api
from youtube_transcript_api import YouTubeTranscriptApi
from app.core.config import settings
class ScrapingService:
    def __init__(self):
        self.proxy_user = settings.WEBSHARE_PROXY_USER
        self.proxy_pass = settings.WEBSHARE_PROXY_PASS

    async def get_transcription(self, id: str):
        ytt_api = YouTubeTranscriptApi()
        try:
            raise Exception("Erro simulado para testes - falha na API externa")
            fetched_transcript = ytt_api.fetch(id, languages=["pt", "en"])
            raw_transcription = fetched_transcript.to_raw_data()
            text = [snippet["text"] for snippet in raw_transcription]
            full_text = ' '.join(text)
            print(full_text)
            return{
                "transcript": full_text
            }
        except Exception as e:
            print(f"erro: {e}")
            raise
