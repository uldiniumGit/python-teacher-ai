# knowledgebase_pipeline/config.py

from pathlib import Path
import os

from dotenv import load_dotenv


# ---------------------------------------------------------------------------
# Project paths
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

KNOWLEDGE_DIR = BASE_DIR / "knowledge"

DATA_DIR = BASE_DIR / "data"

CHUNKS_DIR = DATA_DIR / "chunks"

CHUNKS_FILE = CHUNKS_DIR / "chunks.jsonl"

# ---------------------------------------------------------------------------
# Environment variables
# ---------------------------------------------------------------------------

load_dotenv(BASE_DIR / ".env")


# ---------------------------------------------------------------------------
# OpenAI
# ---------------------------------------------------------------------------

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "text-embedding-3-small",
)


# ---------------------------------------------------------------------------
# Chunking
# ---------------------------------------------------------------------------
CHUNK_SIZE = int(
    os.getenv("CHUNK_SIZE", "800")
)

CHUNK_OVERLAP = int(
    os.getenv("CHUNK_OVERLAP", "100")
)


# ---------------------------------------------------------------------------
# Qdrant
# ---------------------------------------------------------------------------

QDRANT_URL = os.getenv(
    "QDRANT_URL",
    "http://localhost:6333",
)

QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

QDRANT_COLLECTION = os.getenv(
    "QDRANT_COLLECTION",
    "python_knowledge",
)


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_config() -> None:
    """Validate required configuration values."""

    if not KNOWLEDGE_DIR.exists():
        raise FileNotFoundError(
            f"Knowledge directory does not exist: {KNOWLEDGE_DIR}"
        )

    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY is not set. "
            "Add it to the .env file."
        )

    if CHUNK_SIZE <= 0:
        raise ValueError(
            "CHUNK_SIZE must be greater than 0."
        )

    if CHUNK_OVERLAP < 0:
        raise ValueError(
            "CHUNK_OVERLAP cannot be negative."
        )

    if CHUNK_OVERLAP >= CHUNK_SIZE:
        raise ValueError(
            "CHUNK_OVERLAP must be smaller than CHUNK_SIZE."
        )


# ---------------------------------------------------------------------------
# Debug output
# ---------------------------------------------------------------------------

def print_config() -> None:
    """Print the current pipeline configuration."""

    print("=" * 60)
    print("Neuro-Task Pipeline Configuration")
    print("=" * 60)

    print(f"BASE_DIR:          {BASE_DIR}")
    print(f"KNOWLEDGE_DIR:     {KNOWLEDGE_DIR}")
    print(f"DATA_DIR:          {DATA_DIR}")
    print(f"CHUNKS_DIR:        {CHUNKS_DIR}")
    print(f"CHUNKS_FILE:       {CHUNKS_FILE}")

    print()

    print(f"EMBEDDING_MODEL:   {EMBEDDING_MODEL}")
    print(f"CHUNK_SIZE:        {CHUNK_SIZE}")
    print(f"CHUNK_OVERLAP:     {CHUNK_OVERLAP}")

    print()

    print(f"QDRANT_URL:        {QDRANT_URL}")
    print(f"QDRANT_COLLECTION: {QDRANT_COLLECTION}")

    print()

    # Never print the actual API key.
    print(
        "OPENAI_API_KEY:    "
        + ("configured" if OPENAI_API_KEY else "not configured")
    )

    print("=" * 60)


if __name__ == "__main__":
    validate_config()
    print_config()
