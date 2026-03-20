from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from pydantic_settings import BaseSettings
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    QWEN_API_KEY: str = os.getenv("QWEN_API_KEY", "")
    QWEN_BASE_URL: str = os.getenv("QWEN_BASE_URL", "https://api.aitunnel.ru/v1")
    QWEN_MODEL: str = os.getenv("QWEN_MODEL", "qwen/qwen-2.5-3b-instruct")
    
settings = Settings()

client = None
if settings.QWEN_API_KEY:
    client = OpenAI(
        api_key=settings.QWEN_API_KEY,
        base_url=settings.QWEN_BASE_URL
    )

app = FastAPI(title="Moody Movie API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "ok", "message": "Moody Movie API is running"}

class SituationRequest(BaseModel):
    situation: str

class MovieRecommendation(BaseModel):
    title: str
    description: str
    year: int
    country: str
    actors: list[str]

@app.post("/recommend", response_model=MovieRecommendation)
async def recommend_movie(request: SituationRequest):
    if not client:
        raise HTTPException(status_code=500, detail="Qwen API Key not configured")
    
    prompt = f"""
    Ситуация: {request.situation}
    
    Найди художественный фильм, который лучше всего подходит под эту ситуацию по смыслу, настроению или сюжету. 
    Верни ответ СТРОГО в формате JSON со следующими полями:
    - title (название фильма)
    - description (краткое описание)
    - year (год выпуска, только число)
    - country (страна)
    - actors (список главных актеров)
    
    Ответ должен быть только JSON, без лишнего текста и без markdown разметки ```json.
    """
    
    try:
        response = client.chat.completions.create(
            model=settings.QWEN_MODEL,
            messages=[
                {"role": "system", "content": "Ты — помощник по подбору фильмов. Отвечай только в формате JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        content = response.choices[0].message.content.strip()
            
        # Clean up potential markdown formatting in response
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
                
        movie_data = json.loads(content)
        return MovieRecommendation(**movie_data)
            
    except Exception as e:
        print(f"Error calling Qwen: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
