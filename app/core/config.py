"""
Application configuration using Pydantic Settings
"""
from typing import List, Optional
from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""
    
    # Project Information
    PROJECT_NAME: str = "CashMeOutside API"
    PROJECT_DESCRIPTION: str = "FastAPI application with PostgreSQL, JWT authentication, and Docker support"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    # Database Configuration
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/cashmeoutside_db"
    SYNC_DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/cashmeoutside_db"
    
    # JWT Configuration
    JWT_SECRET_KEY: str = "changeme_secret_key_for_jwt_tokens"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS Configuration
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v):
        if isinstance(v, str):
            return [i.strip() for i in v.split(",")]
        return v
    
    # Environment
    ENVIRONMENT: str = "development"
    
    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
