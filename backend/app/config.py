from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    DB_URL: str = "sqlite:///./km.db"
    STORAGE_DIR: str = "./storage"
    EMBED_MODEL: str = "paraphrase-multilingual-MiniLM-L12-v2"
    OLLAMA_HOST: str = "http://localhost:11434"
    LLM_MODEL: str = "gemma3:4b"
    OCR_CONF_THRESHOLD: float = 0.7  # TUNE
    CHUNK_TOKENS: int = 480           # TUNE
    FUSION_ALPHA: float = 0.5         # TUNE
    TOP_K: int = 10
    class Config:
        env_file = ".env"
settings = Settings()
