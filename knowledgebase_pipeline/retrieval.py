# retrieval.py
from openai import OpenAI
from qdrant_client import QdrantClient

from knowledgebase_pipeline.config import (
    OPENAI_API_KEY,
    EMBEDDING_MODEL,
    QDRANT_URL,
    QDRANT_COLLECTION,
)

TOP_K = 5


def create_openai_client() -> OpenAI:
    """
    Create OpenAI client.
    """

    if not OPENAI_API_KEY:
        raise RuntimeError(
            "OPENAI_API_KEY is not configured."
        )

    return OpenAI(api_key=OPENAI_API_KEY)


def create_qdrant_client() -> QdrantClient:
    """
    Create Qdrant client.
    """

    return QdrantClient(
        url=QDRANT_URL,
    )


def create_query_embedding(
        client: OpenAI,
        query: str,
) -> list[float]:
    """
    Create an embedding for the user's query.
    """

    if not query.strip():
        raise ValueError(
            "Query cannot be empty."
        )

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=query,
    )

    if not response.data:
        raise RuntimeError(
            "OpenAI returned no embedding."
        )

    embedding = response.data[0].embedding

    if not embedding:
        raise RuntimeError(
            "OpenAI returned an empty embedding."
        )

    return embedding


def search_qdrant(
        client: QdrantClient,
        query_vector: list[float],
        limit: int = TOP_K,
):
    """
    Search for the most relevant chunks in Qdrant.
    """

    response = client.query_points(
        collection_name=QDRANT_COLLECTION,
        query=query_vector,
        limit=limit,
        with_payload=True,
    )

    return response.points


def retrieve_context(
        query: str,
        limit: int = TOP_K,
) -> str:
    """
    Create query embedding, search Qdrant
    and return relevant chunks as a single context.
    """

    openai_client = create_openai_client()
    qdrant_client = create_qdrant_client()

    try:
        query_vector = create_query_embedding(
            client=openai_client,
            query=query,
        )

        results = search_qdrant(
            client=qdrant_client,
            query_vector=query_vector,
            limit=limit,
        )

        context_parts = []

        for result in results:
            payload = result.payload or {}

            text = payload.get("text")

            if text:
                context_parts.append(text)

        return "\n\n---\n\n".join(context_parts)

    finally:
        qdrant_client.close()


def retrieve_context_with_metadata(
        query: str,
        limit: int = TOP_K,
) -> tuple[str, list[dict]]:
    openai_client = create_openai_client()
    qdrant_client = create_qdrant_client()

    try:
        query_vector = create_query_embedding(
            client=openai_client,
            query=query,
        )

        results = search_qdrant(
            client=qdrant_client,
            query_vector=query_vector,
            limit=limit,
        )

        context_parts = []
        metadata = []

        for rank, result in enumerate(results, start=1):
            payload = result.payload or {}
            text = payload.get("text", "")

            if text:
                context_parts.append(text)

            metadata.append(
                {
                    "rank": rank,
                    "id": result.id,
                    "score": result.score,
                    "source": payload.get("source"),
                    "section": payload.get("section"),
                    "text_length": len(text),
                }
            )

        context = "\n\n---\n\n".join(context_parts)

        return context, metadata

    finally:
        qdrant_client.close()
