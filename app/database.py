import os
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL não foi encontrada. Crie um arquivo .env na raiz do projeto.")


def _ensure_sslmode(url: str) -> str:
    """Supabase/pooler costuma exigir SSL. Mantém a URL intacta e adiciona sslmode=require se faltar."""
    parsed = urlparse(url)
    if "supabase.com" not in parsed.netloc or "sslmode=" in parsed.query:
        return url

    query = dict(parse_qsl(parsed.query))
    query["sslmode"] = "require"
    return urlunparse(parsed._replace(query=urlencode(query)))


engine = create_engine(
    _ensure_sslmode(DATABASE_URL),
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_database_connection() -> bool:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return True
