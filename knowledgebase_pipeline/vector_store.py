# knowledgebase_pipeline/vector_store.py

import json
import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)

from knowledgebase_pipeline.config import (
    CHUNKS_FILE,
    QDRANT_COLLECTION,
    QDRANT_URL,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DISTANCE = Distance.COSINE


# ---------------------------------------------------------------------------
# Loading embeddings
# ---------------------------------------------------------------------------

def load_embeddings() -> list[dict]:
    """
    Load embeddings from embeddings.jsonl.
    """

    if not CHUNKS_FILE.parent.exists():
        raise FileNotFoundError(
            f"Chunks directory does not exist: {CHUNKS_FILE.parent}"
        )

    embeddings_file = CHUNKS_FILE.parent / "embeddings.jsonl"

    if not embeddings_file.exists():
        raise FileNotFoundError(
            f"Embeddings file not found: {embeddings_file}"
        )

    embeddings = []

    with embeddings_file.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"Invalid JSON on line {line_number}: "
                    f"{embeddings_file}"
                ) from exc

            embeddings.append(item)

    if not embeddings:
        raise ValueError(
            f"No embeddings found in: {embeddings_file}"
        )

    return embeddings


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_embeddings(embeddings: list[dict]) -> None:
    """
    Validate embeddings before uploading them to Qdrant.
    """

    if not embeddings:
        raise ValueError("Embedding list is empty.")

    required_fields = {
        "id",
        "text",
        "metadata",
        "embedding",
    }

    ids = set()
    vector_dimension = None

    for index, item in enumerate(embeddings, start=1):

        missing_fields = required_fields - item.keys()

        if missing_fields:
            raise ValueError(
                f"Embedding #{index} is missing fields: "
                f"{sorted(missing_fields)}"
            )

        chunk_id = item["id"]

        if not isinstance(chunk_id, str) or not chunk_id.strip():
            raise ValueError(
                f"Embedding #{index} has invalid ID."
            )

        if chunk_id in ids:
            raise ValueError(
                f"Duplicate embedding ID: {chunk_id}"
            )

        ids.add(chunk_id)

        if not isinstance(item["text"], str) or not item["text"].strip():
            raise ValueError(
                f"Embedding '{chunk_id}' has empty text."
            )

        if not isinstance(item["metadata"], dict):
            raise ValueError(
                f"Embedding '{chunk_id}' has invalid metadata."
            )

        vector = item["embedding"]

        if not isinstance(vector, list) or not vector:
            raise ValueError(
                f"Embedding '{chunk_id}' has an invalid vector."
            )

        if not all(
                isinstance(value, (int, float))
                for value in vector
        ):
            raise ValueError(
                f"Embedding '{chunk_id}' contains "
                f"non-numeric vector values."
            )

        if vector_dimension is None:
            vector_dimension = len(vector)
        elif len(vector) != vector_dimension:
            raise ValueError(
                f"Embedding '{chunk_id}' has dimension "
                f"{len(vector)}, expected {vector_dimension}."
            )

    print("Embedding validation: OK")
    print(f"Embedding count:      {len(embeddings)}")
    print(f"Vector dimension:     {vector_dimension}")


# ---------------------------------------------------------------------------
# Qdrant helpers
# ---------------------------------------------------------------------------

def get_vector_dimension(embeddings: list[dict]) -> int:
    """
    Return embedding vector dimension.
    """

    return len(embeddings[0]["embedding"])


def make_point_id(chunk_id: str) -> str:
    """
    Create a deterministic UUID for a Qdrant point.

    The same chunk ID will always produce the same UUID.
    """

    return str(
        uuid.uuid5(
            uuid.NAMESPACE_URL,
            f"python_teacher_ai:{chunk_id}",
        )
    )


def create_collection_if_needed(
        client: QdrantClient,
        vector_dimension: int,
) -> None:
    """
    Create the target collection if it does not exist.

    Existing collection is preserved.
    """

    if client.collection_exists(QDRANT_COLLECTION):
        print(
            f"Collection '{QDRANT_COLLECTION}' already exists."
        )
        return

    print(
        f"Creating collection '{QDRANT_COLLECTION}'..."
    )

    client.create_collection(
        collection_name=QDRANT_COLLECTION,
        vectors_config=VectorParams(
            size=vector_dimension,
            distance=DISTANCE,
        ),
    )

    print("Collection created: OK")


def get_collection_info(
        client: QdrantClient,
):
    """
    Return information about the target collection.
    """

    return client.get_collection(QDRANT_COLLECTION)


# ---------------------------------------------------------------------------
# Upload
# ---------------------------------------------------------------------------

def build_points(
        embeddings: list[dict],
) -> list[PointStruct]:
    """
    Convert embeddings into Qdrant points.
    """

    points = []

    for item in embeddings:
        chunk_id = item["id"]

        payload = {
            "chunk_id": chunk_id,
            "text": item["text"],
            "metadata": item["metadata"],
        }

        points.append(
            PointStruct(
                id=make_point_id(chunk_id),
                vector=item["embedding"],
                payload=payload,
            )
        )

    return points


def upload_embeddings(
        client: QdrantClient,
        embeddings: list[dict],
) -> None:
    """
    Upload all embeddings to Qdrant.
    """

    points = build_points(embeddings)

    print(f"Uploading {len(points)} points...")

    client.upsert(
        collection_name=QDRANT_COLLECTION,
        points=points,
    )

    print("Upload: OK")


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_collection(
        client: QdrantClient,
        expected_count: int,
        expected_dimension: int,
) -> None:
    """
    Verify that the Qdrant collection contains the expected data.
    """

    print()
    print("Verifying Qdrant collection...")

    info = get_collection_info(client)

    actual_count = client.count(
        collection_name=QDRANT_COLLECTION,
        exact=True,
    ).count

    print(f"Collection:           {QDRANT_COLLECTION}")
    print(f"Distance:             {DISTANCE.name}")
    print(f"Vector dimension:     {expected_dimension}")
    print(f"Expected points:      {expected_count}")
    print(f"Actual points:        {actual_count}")

    if actual_count != expected_count:
        raise RuntimeError(
            "Point count does not match the number of embeddings. "
            f"Expected {expected_count}, got {actual_count}."
        )

    collection_size = info.config.params.vectors

    if collection_size is None:
        raise RuntimeError(
            "Could not read Qdrant vector configuration."
        )

    if collection_size.size != expected_dimension:
        raise RuntimeError(
            "Qdrant vector dimension does not match embeddings. "
            f"Qdrant: {collection_size.size}, "
            f"Embeddings: {expected_dimension}."
        )

    if collection_size.distance != DISTANCE:
        raise RuntimeError(
            "Qdrant distance metric does not match expected value. "
            f"Expected: {DISTANCE}, "
            f"Actual: {collection_size.distance}."
        )

    print("Collection configuration: OK")

    # Read one point to verify payload and vector.
    sample = client.scroll(
        collection_name=QDRANT_COLLECTION,
        limit=1,
        with_vectors=True,
        with_payload=True,
    )

    points, _ = sample

    if not points:
        raise RuntimeError(
            "Collection exists but contains no readable points."
        )

    point = points[0]

    if point.vector is None:
        raise RuntimeError(
            "Sample point contains no vector."
        )

    if not isinstance(point.vector, list):
        raise RuntimeError(
            "Sample point has an unexpected vector format."
        )

    if len(point.vector) != expected_dimension:
        raise RuntimeError(
            "Sample point vector dimension is incorrect."
        )

    if point.payload is None:
        raise RuntimeError(
            "Sample point contains no payload."
        )

    if "chunk_id" not in point.payload:
        raise RuntimeError(
            "Sample payload does not contain 'chunk_id'."
        )

    if "text" not in point.payload:
        raise RuntimeError(
            "Sample payload does not contain 'text'."
        )

    if "metadata" not in point.payload:
        raise RuntimeError(
            "Sample payload does not contain 'metadata'."
        )

    print("Sample vector:       OK")
    print("Sample payload:      OK")
    print(f"Sample chunk ID:     {point.payload['chunk_id']}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 70)
    print("QDRANT VECTOR STORE")
    print("=" * 70)

    print()
    print(f"Qdrant URL:       {QDRANT_URL}")
    print(f"Collection:       {QDRANT_COLLECTION}")
    print()

    print("[1/6] Loading embeddings...")

    embeddings = load_embeddings()

    print(f"      Loaded: {len(embeddings)} embeddings")

    print()
    print("[2/6] Validating embeddings...")

    validate_embeddings(embeddings)

    vector_dimension = get_vector_dimension(embeddings)

    print()
    print("[3/6] Connecting to Qdrant...")

    client = QdrantClient(url=QDRANT_URL)

    try:
        client.get_collections()

        print("      Connection: OK")

        print()
        print("[4/6] Checking collection...")

        create_collection_if_needed(
            client=client,
            vector_dimension=vector_dimension,
        )

        print()
        print("[5/6] Uploading embeddings...")

        upload_embeddings(
            client=client,
            embeddings=embeddings,
        )

        print()
        print("[6/6] Verifying database...")

        verify_collection(
            client=client,
            expected_count=len(embeddings),
            expected_dimension=vector_dimension,
        )

        print()
        print("=" * 70)
        print("VECTOR STORE BUILD PASSED")
        print("=" * 70)
        print()
        print("Knowledge base is now stored in Qdrant.")
        print()
        print(f"Collection:       {QDRANT_COLLECTION}")
        print(f"Points:           {len(embeddings)}")
        print(f"Vector dimension: {vector_dimension}")
        print(f"Distance:         {DISTANCE.name}")
        print(f"Qdrant URL:       {QDRANT_URL}")
        print()
        print("=" * 70)

    finally:
        client.close()


if __name__ == "__main__":
    main()
