from dataclasses import dataclass
from pathlib import Path

from knowledgebase_pipeline.config import KNOWLEDGE_DIR


@dataclass
class Document:
    """
    Represents a single Markdown document from the knowledge base.
    """

    path: Path
    category: str
    topic: str
    content: str


def find_markdown_files() -> list[Path]:
    """
    Find all Markdown files inside the knowledge directory.

    Searches recursively through all subdirectories.
    """

    return sorted(KNOWLEDGE_DIR.rglob("*.md"))


def get_category(file_path: Path) -> str:
    """
    Extract category from the file path.

    Example:
        knowledge/basics/loops.md
        -> basics
    """

    relative_path = file_path.relative_to(KNOWLEDGE_DIR)

    if len(relative_path.parts) < 2:
        raise ValueError(
            f"Markdown file must be inside a category directory: "
            f"{file_path}"
        )

    return relative_path.parts[0]


def get_topic(file_path: Path) -> str:
    """
    Extract topic from the Markdown filename.

    Example:
        loops.md
        -> loops

        magic_methods.md
        -> magic_methods
    """

    return file_path.stem


def load_document(file_path: Path) -> Document:
    """
    Read a single Markdown file and create a Document object.
    """

    content = file_path.read_text(
        encoding="utf-8"
    )

    if not content.strip():
        raise ValueError(
            f"Markdown file is empty: {file_path}"
        )

    category = get_category(file_path)
    topic = get_topic(file_path)

    return Document(
        path=file_path,
        category=category,
        topic=topic,
        content=content,
    )


def load_documents() -> list[Document]:
    """
    Find and load all Markdown documents.
    """

    files = find_markdown_files()

    if not files:
        raise FileNotFoundError(
            f"No Markdown files found in: {KNOWLEDGE_DIR}"
        )

    documents = []

    for file_path in files:
        document = load_document(file_path)
        documents.append(document)

    return documents


def print_documents(documents: list[Document]) -> None:
    """
    Print loaded documents for verification.
    """

    print("=" * 70)
    print("LOADER CHECK")
    print("=" * 70)

    print(f"Knowledge directory: {KNOWLEDGE_DIR}")
    print(f"Documents found:    {len(documents)}")
    print()

    for index, document in enumerate(documents, start=1):
        print(f"{index}. {document.topic}")
        print(f"   Category: {document.category}")
        print(f"   File:     {document.path}")
        print(f"   Size:     {len(document.content)} characters")
        print()

    print("=" * 70)
    print("Loader completed successfully.")
    print("=" * 70)


def validate_documents(documents: list[Document]) -> None:
    """
    Validate loaded documents.

    Raises an exception if something is wrong.
    """

    if not documents:
        raise ValueError("Document list is empty.")

    for document in documents:
        if not document.content.strip():
            raise ValueError(
                f"Document has empty content: {document.path}"
            )

        if not document.category:
            raise ValueError(
                f"Document has no category: {document.path}"
            )

        if not document.topic:
            raise ValueError(
                f"Document has no topic: {document.path}"
            )


if __name__ == "__main__":
    documents = load_documents()

    validate_documents(documents)

    print_documents(documents)
