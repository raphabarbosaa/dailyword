Aprenda inglês diariamente com Spaced Repetition System (SRS)! FastAPI backend + Postgres + Docker + Frontend HTML5/JS. Desenvolvido em 17/03/2026 (2h MVP funcional).
​

[

🚀 Features Atuais (17/03/2026)
Feature	Descrição	Endpoint	Status
FastAPI v1.0	API REST completa com Swagger docs auto-gerados	GET /docs ou /redoc	✅ http://localhost:8000/docs
Autenticação JWT	Register/Login com bcrypt + token 30min + protected routes	POST /auth/register, /login, GET /protected	✅ Teste via Swagger
Postgres DB	Users (email, hashed_password) + Reviews (SRS spaced repetition)	SQLAlchemy ORM + get_db dependency	✅ Base.metadata.create_all()
Docker Compose	Postgres 16-alpine + Redis 7-alpine (volumes persistentes)	docker-compose up -d	✅ Porta 5432/6379
Redis Sessions	Cache futuro (não usado ainda)	Configurado docker-compose.yml	✅
Word Random	Palavra inglês aleatória + definição via Free Dictionary API	GET /word/random	✅ https://api.dictionaryapi.dev/api/v2/entries/en/{word} 
​
Frontend Login	HTML/CSS/JS moderno + localStorage token + fetch API	GET / → /dashboard	✅ Responsivo mobile
SRS Base	Model Review (word, difficulty 1-5, next_review DateTime)	Tabela Postgres	✅ Algoritmo pendente
Git Ready	requirements.txt + .gitignore + README completo	SSH/HTTPS push	✅ 13 arquivos commitados
Demo Local: [http://localhost:8000](http://localhost:8000/) → Login → Dashboard → /docs API completa.

🛠 Tech Stack Detalhado
text
Backend: FastAPI 0.115+ | Uvicorn ASGI | SQLAlchemy 2.0 ORM
Database: PostgreSQL 16-alpine | psycopg2-binary | Alembic (pendente)
Cache: Redis 7-alpine
Auth: JWT (python-jose[cryptography]) | bcrypt<5.0 | passlib
Frontend: Jinja2 Templates | Vanilla JS (fetch + localStorage)
DevOps: Docker Compose | venv Python 3.13 | VSCode Windows
APIs: Free Dictionary API (definições reais) [web:94]
Dependências (requirements.txt):

text
fastapi==0.115.0
uvicorn==0.30.6
sqlalchemy==2.0.35
psycopg2-binary==2.9.9
redis==5.0.8
python-jose[cryptography]==3.3.0
passlib[bcrypt]<5.0
jinja2==3.1.6
pydantic-settings==2.5.2
python-multipart==0.0.9
httpx==0.27.0
📦 Instalação & Setup Local (5min)
powershell
# Clone + venv
git clone https://github.com/raphabarbosaa/dailyword.git
cd dailyword
python -m venv venv
venv\Scripts\activate  # Windows

# Dependências
pip install -r requirements.txt

# Docker DB (Terminal 1)
docker-compose up -d
docker ps  # db:5432 redis:6379

# API (Terminal 2)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
Verifique:

text
http://localhost:8000/docs  # Swagger UI
http://localhost:8000      # Frontend login
docker-compose logs db     # Postgres OK
🧪 Testes Manuais (Swagger /docs)
Register Novo User:

text
POST /auth/register
{"email": "user@example.com", "password": "12345678"}
Resposta: {"msg": "User criado"}

Login:

text
POST /auth/login
username: user@example.com
password: 12345678
Resposta: {"access_token": "eyJ...", "token_type": "bearer"}

Protected:

text
GET /protected
Header: Authorization: Bearer [TOKEN]
Resposta: {"msg": "Token válido!", "user": "user@example.com"}

Word Random (protegido):

text
GET /word/random
Header: Authorization: Bearer [TOKEN]
Exemplo: {"word": "serene", "definition": "calm, peaceful", "example": "..."}
​

📱 Fluxo Usuário Completo
text
1. Acessa http://localhost:8000 (HTML login bonito)
2. Register/Login → Token localStorage auto
3. Dashboard → Botão "Palavra Dia" (fetch /word/random)
4. Marca difficulty 1-5 → Salva Review (SRS next_review)
5. Amanhã: /daily/review → 5 palavras pra revisar
🤖 Roadmap Detalhado (Pendências Priorizadas)
Prioridade	Feature	Descrição	Esforço
🔴 Alta	SRS Algoritmo	next_review = hoje + (dias * 2^difficulty)	15min
🔴 Alta	/daily/review	GET 5 reviews user.today	10min
🟡 Média	/quiz/start	10 palavras MCQ protegido	20min
🟡 Média	PWA Mobile	Service worker + Tailwind + manifest.json	30min
🟢 Baixa	Deploy Railway	GitHub → Railway (env SECRET_KEY)	5min
🟢 Baixa	Alembic Migrations	alembic init + upgrade	15min
🟢 Baixa	Pytest 80%	Testes auth + word endpoints	1h
🟢 Baixa	Redis Cache	LRU words + sessions	10min
🟢 Baixa	Rate Limit	slowapi /word/random (10/min)	5min
🐳 Docker Production Ready
docker-compose.yml (já incluso):

text
version: '3.8'
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: dailyword
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
    ports: ["5432:5432"]
    volumes: [postgres_data:/var/lib/postgresql/data]
  redis:
    image: redis:7-alpine
    ports: ["6379:6379"]
volumes:
  postgres_data:
Production (Railway/Docker Hub):

text
# Dockerfile
FROM python:3.13-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "$PORT"]
🔧 Troubleshooting Comum
Erro	Causa	Fix
500 bcrypt	bcrypt>=5.0 bug	pip install "bcrypt<5.0"
NoSuchTableError	Tabelas não criadas	Base.metadata.create_all(bind=engine)
TemplateNotFound	login.html missing	Crie templates/ na raiz
Permission denied SSH	Key não cadastrada	GitHub Settings → SSH keys
Docker connection refused	Containers down	docker-compose up -d
🤝 Contribuições
Fork repo

git checkout -b feature/srs

git push origin feature/srs

Pull Request → Discussão

Issues bem-vindas: Bugs, features, deploy.

📄 Licença
MIT License – Use livremente! © 2026 Raphael Barbosa (DevOps SP)