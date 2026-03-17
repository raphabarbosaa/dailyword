DailyWord API
Aprenda inglês com palavras diárias + Spaced Repetition System (SRS)! FastAPI + Postgres + Docker + Frontend HTML/JS. MVP funcional em 2h.
​

<!-- Substitua por seu screenshot -->
🚀 Features Atuais (até 17/03/2026)
✅ FastAPI v1.0 (localhost:8000/docs Swagger)

✅ Autenticação JWT (register/login/protected)

✅ Postgres (users/reviews) + Docker Compose

✅ Redis sessões

✅ /word/random (Dictionary API real)

✅ Frontend login + dashboard (templates HTML/CSS/JS)

✅ SRS Base (Review model com next_review)

✅ Git ready (requirements.txt + .gitignore)

Demo: http://localhost:8000 → Login → Dashboard → /docs

🛠 Tech Stack
text
FastAPI + SQLAlchemy + Alembic
Postgres 16 + Redis 7 (Docker)
JWT (python-jose) + bcrypt
HTML/JS + Jinja2 (frontend)
venv Python 3.13 Windows/VSCode
📦 Instalação Local
bash
git clone https://github.com/SEU_USER/dailyword-api
cd dailyword-api
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
docker-compose up -d
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
Teste:

POST /auth/register {"email":"test@example.com","password":"12345678"}

POST /auth/login → Copy token

http://localhost:8000 (login HTML)

📱 Como Usar
Registre via /docs

Login → token auto dashboard

Palavra dia: GET /word/random (Bearer token)

Review SRS: Próximo /daily/review

🤖 Roadmap (Faltam)
 SRS Completo: Algoritmo next_review (fácil=7d, difícil=1d)

 /quiz/start protegido + submit score

 PWA Mobile (service worker + Tailwind)

 Deploy Railway/Heroku (env vars SECRET_KEY)

 Alembic migrations

 Tests pytest

 Redis Cache words

 Rate limit /word/random

🐳 Docker Production
text
# docker-compose.prod.yml
services:
  app:
    build: .
    ports: ["8000:8000"]
    env_file: .env
  db: ...
🤝 Contribua
Fork → Pull Request

pre-commit install

Issues bem-vindas!

📄 Licença
MIT – Livre uso!
​

Autor: Raphael Barbosa (DevOps @ Consultoria SP)