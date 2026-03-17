from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://user:pass@localhost:5432/dailyword"
    redis_url: str = "redis://localhost:6379"
    secret_key: str = "dailyword-super-secret-key-change-in-prod"
    
    class Config:
        env_file = ".env"

settings = Settings()
