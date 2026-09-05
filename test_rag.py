from datetime import datetime
from pathlib import Path

from openai import OpenAI
from qdrant_client import QdrantClient

from knowledgebase_pipeline.config import (
    OPENAI_API_KEY,
    EMBEDDING_MODEL,
    QDRANT_URL,
    QDRANT_COLLECTION,
)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

TOP_K = 5

BASE_DIR = Path(__file__).resolve().parent
REPORT_FILE = BASE_DIR / "data" / "rag_test_report.txt"


# ---------------------------------------------------------------------------
# Clients
# ---------------------------------------------------------------------------

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

    return QdrantClient(url=QDRANT_URL)


# ---------------------------------------------------------------------------
# Embedding
# ---------------------------------------------------------------------------

def create_query_embedding(
        client: OpenAI,
        query: str,
) -> list[float]:
    """
    Create an embedding for the user's query.
    """

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


# ---------------------------------------------------------------------------
# Semantic search
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Report helpers
# ---------------------------------------------------------------------------

def create_report_header(
        test_queries: list[str],
) -> str:
    """
    Create the beginning of the text report.
    """

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    lines = [
        "=" * 70,
        "PYTHON KNOWLEDGE BASE — RAG TEST REPORT",
        "=" * 70,
        "",
        "TEST INFORMATION",
        "-" * 70,
        f"Date:             {timestamp}",
        f"Embedding model:  {EMBEDDING_MODEL}",
        f"Qdrant URL:       {QDRANT_URL}",
        f"Collection:       {QDRANT_COLLECTION}",
        f"Top K:            {TOP_K}",
        f"Test queries:     {len(test_queries)}",
        "",
        "",
        "TEST QUERIES",
        "-" * 70,
    ]

    for index, query in enumerate(test_queries, start=1):
        lines.extend([
            "",
            f"Query {index}:",
            query,
        ])

    lines.extend([
        "",
        "",
    ])

    return "\n".join(lines)


def create_query_report(
        query_number: int,
        query: str,
        results,
) -> str:
    """
    Create text report section for one query.
    """

    lines = [
        "=" * 70,
        f"QUERY {query_number}",
        "=" * 70,
        "",
        "Question:",
        query,
        "",
        f"Results found: {len(results)}",
        "",
    ]

    for index, result in enumerate(results, start=1):
        payload = result.payload or {}

        chunk_id = payload.get(
            "chunk_id",
            "N/A",
        )

        text = payload.get(
            "text",
            "",
        )

        metadata = payload.get(
            "metadata",
            {},
        )

        category = metadata.get(
            "category",
            "N/A",
        )

        topic = metadata.get(
            "topic",
            "N/A",
        )

        section = metadata.get(
            "section",
            "N/A",
        )

        content_type = metadata.get(
            "content_type",
            "N/A",
        )

        lines.extend([
            "-" * 70,
            f"RESULT {index}",
            "-" * 70,
            "",
            f"Score:        {result.score:.4f}",
            f"Chunk ID:     {chunk_id}",
            f"Category:     {category}",
            f"Topic:        {topic}",
            f"Section:      {section}",
            f"Content type: {content_type}",
            "",
            "Text:",
            "-" * 70,
            text,
            "-" * 70,
            "",
        ])

    lines.extend([
        "",
    ])

    return "\n".join(lines)


def create_final_result_report() -> str:
    """
    Create final result section.
    """

    return "\n".join([
        "=" * 70,
        "FINAL RESULT",
        "=" * 70,
        "",
        "Status: ALL RAG TESTS PASSED",
        "",
        "The semantic retrieval tests completed successfully.",
        "",
    ])


def save_report(
        report: str,
) -> None:
    """
    Save the RAG test report to a text file.
    """

    REPORT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    REPORT_FILE.write_text(
        report,
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# Console output
# ---------------------------------------------------------------------------

def print_results(
        query: str,
        results,
) -> None:
    """
    Print semantic search results.
    """

    print()
    print("=" * 70)
    print("RAG RETRIEVAL TEST")
    print("=" * 70)

    print()
    print(f"Question: {query}")
    print(f"Results:  {len(results)}")

    print()
    print("-" * 70)

    for index, result in enumerate(results, start=1):
        payload = result.payload or {}

        chunk_id = payload.get(
            "chunk_id",
            "N/A",
        )

        text = payload.get(
            "text",
            "",
        )

        metadata = payload.get(
            "metadata",
            {},
        )

        print()
        print(f"[{index}] Score: {result.score:.4f}")
        print(f"Chunk ID: {chunk_id}")

        if metadata:
            print(
                f"Category: {metadata.get('category', 'N/A')}"
            )

            print(
                f"Topic:    {metadata.get('topic', 'N/A')}"
            )

            print(
                f"Section:  {metadata.get('section', 'N/A')}"
            )

            print(
                f"Type:     {metadata.get('content_type', 'N/A')}"
            )

        print()
        print("Text:")

        # Do not print an excessively large chunk.
        preview = text[:1000]

        print(preview)

        if len(text) > 1000:
            print("...")

        print()
        print("-" * 70)


# ---------------------------------------------------------------------------
# Single query test
# ---------------------------------------------------------------------------

def run_test(
        query: str,
        query_number: int,
) -> str:
    """
    Run one complete RAG retrieval test.

    Returns:
        Text report section for the query.
    """

    openai_client = create_openai_client()
    qdrant_client = create_qdrant_client()

    try:
        print()
        print("=" * 70)
        print("RAG QUERY")
        print("=" * 70)

        print()
        print(f"Question:        {query}")
        print(f"Embedding model: {EMBEDDING_MODEL}")
        print(f"Qdrant URL:      {QDRANT_URL}")
        print(f"Collection:      {QDRANT_COLLECTION}")
        print(f"Top K:           {TOP_K}")

        print()
        print("[1/3] Creating query embedding...")

        query_embedding = create_query_embedding(
            client=openai_client,
            query=query,
        )

        print("      OK")

        print(
            f"      Vector dimension: "
            f"{len(query_embedding)}"
        )

        print()
        print("[2/3] Searching Qdrant...")

        results = search_qdrant(
            client=qdrant_client,
            query_vector=query_embedding,
            limit=TOP_K,
        )

        if not results:
            raise RuntimeError(
                "Qdrant returned no search results."
            )

        print("      OK")
        print(
            f"      Results found: {len(results)}"
        )

        print()
        print("[3/3] Checking results...")

        for result in results:
            if result.score is None:
                raise RuntimeError(
                    "Search result has no similarity score."
                )

            if result.payload is None:
                raise RuntimeError(
                    "Search result has no payload."
                )

            if "text" not in result.payload:
                raise RuntimeError(
                    "Search result payload has no text."
                )

            if "chunk_id" not in result.payload:
                raise RuntimeError(
                    "Search result payload has no chunk_id."
                )

        print("      OK")

        print_results(
            query=query,
            results=results,
        )

        print()
        print("=" * 70)
        print("RAG RETRIEVAL TEST PASSED")
        print("=" * 70)

        return create_query_report(
            query_number=query_number,
            query=query,
            results=results,
        )

    finally:
        qdrant_client.close()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    test_queries = [
        "Что такое list в Python?",
        "Что такое наследование в Python?",
        "Что такое магические методы в Python?",
    ]

    print("=" * 70)
    print("PYTHON KNOWLEDGE BASE — RAG TEST")
    print("=" * 70)

    print()
    print(f"Collection: {QDRANT_COLLECTION}")
    print(
        f"Test queries: {len(test_queries)}"
    )

    report_parts = [
        create_report_header(
            test_queries=test_queries,
        )
    ]

    for query_number, query in enumerate(
            test_queries,
            start=1,
    ):
        report_section = run_test(
            query=query,
            query_number=query_number,
        )

        report_parts.append(
            report_section
        )

    report_parts.append(
        create_final_result_report()
    )

    report = "\n".join(report_parts)

    save_report(
        report=report,
    )

    print()
    print("=" * 70)
    print("ALL RAG TESTS PASSED")
    print("=" * 70)

    print()
    print(f"Report saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()
