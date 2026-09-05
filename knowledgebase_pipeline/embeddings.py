# knowledgebase_pipeline/embeddings.py

import json

from openai import OpenAI

from knowledgebase_pipeline.config import (
    CHUNKS_FILE,
    EMBEDDING_MODEL,
    OPENAI_API_KEY,
)


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_api_key() -> None:
    """
    Check that the OpenAI API key is configured.
    """

    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY is not configured."
        )


# ---------------------------------------------------------------------------
# Load chunks
# ---------------------------------------------------------------------------

def load_chunks(
    input_path=CHUNKS_FILE,
) -> list[dict]:
    """
    Load chunks from a JSONL file.

    Each line must contain:
        id
        text
        metadata
    """

    if not input_path.exists():
        raise FileNotFoundError(
            f"Chunks file not found: {input_path}"
        )

    chunks = []

    with input_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        for line_number, line in enumerate(
            file,
            start=1,
        ):
            line = line.strip()

            if not line:
                continue

            try:
                chunk = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"Invalid JSON on line "
                    f"{line_number}: {error}"
                ) from error

            if not chunk.get("id"):
                raise ValueError(
                    f"Chunk on line {line_number} "
                    f"has no ID."
                )

            if not chunk.get("text"):
                raise ValueError(
                    f"Chunk {chunk.get('id')} "
                    f"has no text."
                )

            if "metadata" not in chunk:
                raise ValueError(
                    f"Chunk {chunk.get('id')} "
                    f"has no metadata."
                )

            chunks.append(chunk)

    if not chunks:
        raise ValueError(
            f"No chunks found in: {input_path}"
        )

    return chunks


# ---------------------------------------------------------------------------
# OpenAI client
# ---------------------------------------------------------------------------

def create_openai_client() -> OpenAI:
    """
    Create an OpenAI API client.
    """

    validate_api_key()

    return OpenAI(
        api_key=OPENAI_API_KEY,
    )


# ---------------------------------------------------------------------------
# Embeddings
# ---------------------------------------------------------------------------

def create_embeddings(
    chunks: list[dict],
    client: OpenAI,
    model: str = EMBEDDING_MODEL,
) -> list[dict]:
    """
    Create embeddings for all chunks.

    The API accepts multiple texts in one request,
    so all chunk texts are sent as a batch.
    """

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    response = client.embeddings.create(
        model=model,
        input=texts,
    )

    if len(response.data) != len(chunks):
        raise ValueError(
            "Number of embeddings does not match "
            "number of chunks."
        )

    results = []

    # The API returns embeddings with indexes.
    # Sort explicitly to preserve the same order
    # as the input chunks.
    embeddings_by_index = {
        item.index: item.embedding
        for item in response.data
    }

    for index, chunk in enumerate(chunks):
        embedding = embeddings_by_index.get(index)

        if not embedding:
            raise ValueError(
                f"Embedding not found for "
                f"chunk: {chunk['id']}"
            )

        results.append(
            {
                "id": chunk["id"],
                "text": chunk["text"],
                "metadata": chunk["metadata"],
                "embedding": embedding,
            }
        )

    return results


# ---------------------------------------------------------------------------
# Save embeddings
# ---------------------------------------------------------------------------

def save_embeddings(
    items: list[dict],
    output_path=CHUNKS_FILE.parent / "embeddings.jsonl",
) -> None:
    """
    Save chunks with embeddings to a JSONL file.

    One item = one JSON object = one line.
    """

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output_path.open(
        "w",
        encoding="utf-8",
    ) as file:
        for item in items:
            file.write(
                json.dumps(
                    item,
                    ensure_ascii=False,
                )
                + "\n"
            )


# ---------------------------------------------------------------------------
# Validation of embeddings
# ---------------------------------------------------------------------------

def validate_embeddings(
    items: list[dict],
) -> None:
    """
    Validate generated embeddings before saving.
    """

    if not items:
        raise ValueError(
            "No embeddings were generated."
        )

    ids = set()

    embedding_dimension = None

    for item in items:
        item_id = item.get("id")

        if not item_id:
            raise ValueError(
                "Embedding item has no ID."
            )

        if item_id in ids:
            raise ValueError(
                f"Duplicate embedding ID: {item_id}"
            )

        ids.add(item_id)

        embedding = item.get("embedding")

        if not embedding:
            raise ValueError(
                f"Empty embedding: {item_id}"
            )

        if embedding_dimension is None:
            embedding_dimension = len(
                embedding
            )

        if len(embedding) != embedding_dimension:
            raise ValueError(
                f"Embedding dimension mismatch "
                f"for chunk: {item_id}"
            )

        if not all(
            isinstance(value, (int, float))
            for value in embedding
        ):
            raise ValueError(
                f"Embedding contains "
                f"non-numeric values: {item_id}"
            )


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def print_embedding_statistics(
    chunks: list[dict],
    embeddings: list[dict],
    output_path,
) -> None:
    """
    Print information that allows us to verify
    the embedding stage.
    """

    dimension = len(
        embeddings[0]["embedding"]
    )

    print("=" * 70)
    print("EMBEDDINGS CHECK")
    print("=" * 70)

    print(f"Input chunks:       {len(chunks)}")
    print(f"Embeddings created: {len(embeddings)}")
    print(f"Embedding model:    {EMBEDDING_MODEL}")
    print(f"Vector dimension:   {dimension}")
    print()
    print("First embedding:")
    print("-" * 70)

    first = embeddings[0]

    print(f"ID: {first['id']}")
    print(f"Text length: {len(first['text'])} characters")
    print(f"Vector length: {len(first['embedding'])}")
    print(
        f"First 5 values: "
        f"{first['embedding'][:5]}"
    )

    print("-" * 70)
    print()
    print(f"Output file: {output_path}")
    print("=" * 70)
    print("Embeddings completed successfully.")
    print("=" * 70)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    output_path = (
        CHUNKS_FILE.parent
        / "embeddings.jsonl"
    )

    chunks = load_chunks()

    client = create_openai_client()

    embeddings = create_embeddings(
        chunks=chunks,
        client=client,
    )

    validate_embeddings(
        embeddings
    )

    save_embeddings(
        items=embeddings,
        output_path=output_path,
    )

    print_embedding_statistics(
        chunks=chunks,
        embeddings=embeddings,
        output_path=output_path,
    )
