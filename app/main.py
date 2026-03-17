from typing import List
from fastapi import Request

import httpx
from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.core.security import verify_token
from pydantic import BaseModel

from app.core.database import Base, engine
from app.routes.auth import router as auth_router, get_current_user
from app.models import User

app = FastAPI()
templates = Jinja2Templates(directory="templates")
#app.mount("/static", StaticFiles(directory="static"), name="static")  # Se precisar CSS

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/dashboard")
async def dashboard(request: Request, payload: dict = Depends(verify_token)):
    return templates.TemplateResponse("dashboard.html", {"request": request, "user": payload.get("sub")})


# Cria tabelas
Base.metadata.create_all(bind=engine)

# Inclui rotas de autenticação
app.include_router(auth_router)


# =========================
# Pydantic models
# =========================
class WordResponse(BaseModel):
    word: str
    definition: str
    example: str | None = None


class QuizQuestion(BaseModel):
    word: str
    options: List[str]
    correct: int


class QuizResponse(BaseModel):
    quiz_id: str
    questions: List[QuizQuestion]


# =========================
# Endpoints
# =========================
@app.get("/", tags=["health"])
async def root():
    return {"message": "DailyWord API v1.0 - Aprenda inglês diário!"}


@app.get("/word/random", response_model=WordResponse, tags=["words"])
async def get_random_word():
    """Puxa palavra da Free Dictionary API"""
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get("https://api.dictionaryapi.dev/api/v2/entries/en/serene")

        if resp.status_code != 200:
            raise HTTPException(status_code=503, detail="Dictionary API indisponível")

        data = resp.json()[0]
        meaning = data["meanings"][0]["definitions"][0]

        return WordResponse(
            word=data["word"].title(),
            definition=meaning["definition"],
            example=meaning.get("example"),
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro API externa: {str(e)}")


@app.post("/quiz/start", response_model=QuizResponse, tags=["quiz"])
async def start_quiz():
    """Quiz simples de 3 palavras"""
    questions = [
        {
            "word": "Serene",
            "options": ["Calm and peaceful", "Angry", "Loud", "Fast"],
            "correct": 0,
        },
        {
            "word": "Ubiquitous",
            "options": ["Everywhere", "Rare", "Old", "New"],
            "correct": 0,
        },
        {
            "word": "Ephemeral",
            "options": ["Short-lived", "Eternal", "Permanent", "Long"],
            "correct": 0,
        },
    ]
    return QuizResponse(quiz_id="quiz_001", questions=questions)


@app.get("/protected", tags=["auth"])
async def protected(current_user: User = Depends(get_current_user)):
    return {
        "msg": "✅ Token válido!",
        "user": current_user.email,
    }

from app.core.database import Base, engine
from app.models import User, Review  # Importa models
Base.metadata.create_all(bind=engine)  # Cria users/reviews
print("Tabelas criadas!")  # Confirma


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)