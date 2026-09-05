# knowledgebase_pipeline/chunker.py

import json
import re
from dataclasses import dataclass

from knowledgebase_pipeline.config import CHUNKS_FILE
from knowledgebase_pipeline.loader import (
    Document,
    load_documents,
    validate_documents,
)


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class MarkdownSection:
    """
    Represents a logical section of a Markdown document.
    """

    level: int
    title: str
    content: str


@dataclass
class Chunk:
    """
    Represents a semantic chunk that will later be embedded
    and stored in the vector database.
    """

    id: str
    text: str
    metadata: dict


# ---------------------------------------------------------------------------
# Markdown parsing
# ---------------------------------------------------------------------------

HEADING_PATTERN = re.compile(
    r"^(#{1,6})\s+(.+?)\s*$",
    re.MULTILINE,
)


def parse_markdown_sections(
        content: str,
) -> list[MarkdownSection]:
    """
    Split Markdown document into logical sections based on headings.

    Markdown code blocks are protected so that '#' inside code
    is not treated as a heading.
    """

    lines = content.splitlines()

    sections: list[MarkdownSection] = []

    current_level = 0
    current_title = ""
    current_content: list[str] = []

    in_code_block = False

    def save_current_section() -> None:
        if current_title or current_content:
            sections.append(
                MarkdownSection(
                    level=current_level,
                    title=current_title,
                    content="\n".join(current_content).strip(),
                )
            )

    for line in lines:
        stripped = line.strip()

        # Track fenced code blocks.
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            current_content.append(line)
            continue

        # Do not interpret headings inside code blocks.
        if not in_code_block:
            match = HEADING_PATTERN.match(line)

            if match:
                save_current_section()

                current_level = len(match.group(1))
                current_title = match.group(2).strip()
                current_content = []

                continue

        current_content.append(line)

    save_current_section()

    return [
        section
        for section in sections
        if section.title or section.content
    ]


# ---------------------------------------------------------------------------
# Text utilities
# ---------------------------------------------------------------------------

def normalize_text(text: str) -> str:
    """
    Normalize excessive whitespace while preserving Markdown structure.
    """

    lines = text.splitlines()

    normalized_lines = []

    previous_blank = False

    for line in lines:
        line = line.rstrip()

        if not line.strip():
            if not previous_blank:
                normalized_lines.append("")
            previous_blank = True
            continue

        normalized_lines.append(line)
        previous_blank = False

    return "\n".join(normalized_lines).strip()


def estimate_tokens(text: str) -> int:
    """
    Rough token estimation.

    This is intentionally simple and is used only for chunk sizing.
    The real token count may differ depending on the tokenizer.
    """

    return max(1, len(text) // 4)


# ---------------------------------------------------------------------------
# Content type detection
# ---------------------------------------------------------------------------

CONTENT_TYPE_MAP = {
    "definition": "definition",
    "purpose": "concept",
    "core concepts": "concept",
    "syntax": "reference",
    "rules": "rule",
    "examples": "example",
    "edge cases": "warning",
    "common mistakes": "common_mistake",
    "related concepts": "reference",
    "key takeaways": "reference",
    "source": "reference",
}


def get_content_type(section_title: str) -> str:
    """
    Determine chunk content type from Markdown section title.
    """

    normalized_title = section_title.strip().lower()

    return CONTENT_TYPE_MAP.get(
        normalized_title,
        "concept",
    )


# ---------------------------------------------------------------------------
# Section splitting
# ---------------------------------------------------------------------------

def split_by_paragraphs(
        text: str,
        max_tokens: int,
) -> list[str]:
    """
    Split large text by paragraphs.

    Paragraphs are kept together whenever possible.
    """

    paragraphs = re.split(
        r"\n\s*\n",
        text.strip(),
    )

    chunks: list[str] = []
    current_parts: list[str] = []
    current_tokens = 0

    for paragraph in paragraphs:
        paragraph = paragraph.strip()

        if not paragraph:
            continue

        paragraph_tokens = estimate_tokens(paragraph)

        if (
                current_parts
                and current_tokens + paragraph_tokens > max_tokens
        ):
            chunks.append(
                "\n\n".join(current_parts)
            )

            current_parts = []
            current_tokens = 0

        # A single paragraph may itself be too large.
        if paragraph_tokens > max_tokens:
            if current_parts:
                chunks.append(
                    "\n\n".join(current_parts)
                )
                current_parts = []
                current_tokens = 0

            chunks.extend(
                split_large_paragraph(
                    paragraph,
                    max_tokens,
                )
            )

            continue

        current_parts.append(paragraph)
        current_tokens += paragraph_tokens

    if current_parts:
        chunks.append(
            "\n\n".join(current_parts)
        )

    return chunks


def split_large_paragraph(
        text: str,
        max_tokens: int,
) -> list[str]:
    """
    Split a very large paragraph by lines.

    This is a fallback for content that cannot be kept as
    a single semantic paragraph.
    """

    lines = text.splitlines()

    chunks: list[str] = []
    current_lines: list[str] = []
    current_tokens = 0

    for line in lines:
        line_tokens = estimate_tokens(line)

        if (
                current_lines
                and current_tokens + line_tokens > max_tokens
        ):
            chunks.append(
                "\n".join(current_lines)
            )

            current_lines = []
            current_tokens = 0

        current_lines.append(line)
        current_tokens += line_tokens

    if current_lines:
        chunks.append(
            "\n".join(current_lines)
        )

    return chunks


# ---------------------------------------------------------------------------
# Chunk creation
# ---------------------------------------------------------------------------

def build_chunk_text(
        document: Document,
        section: MarkdownSection,
        content: str,
) -> str:
    """
    Add document context to the actual chunk content.

    This makes every chunk more self-contained for later retrieval.
    """

    parts = [
        f"Topic: {document.topic}",
        f"Section: {section.title}",
    ]

    if section.level >= 3:
        parts.append(
            f"Subtopic: {section.title}"
        )

    parts.append("")
    parts.append(content.strip())

    return "\n".join(parts).strip()


def create_chunk_metadata(
        document: Document,
        section: MarkdownSection,
) -> dict:
    """
    Create metadata required for vector search and filtering.
    """

    return {
        "language": "python",
        "version": "3.14",
        "category": document.category,
        "topic": document.topic,
        "subtopic": (
            section.title
            if section.level >= 3
            else None
        ),
        "content_type": get_content_type(
            section.title
        ),
        "difficulty": "beginner",
        "document": document.path.name,
        "section": section.title,
    }


def create_chunks(
        documents: list[Document],
        max_tokens: int,
) -> list[Chunk]:
    """
    Convert documents into semantic chunks.

    The primary splitting unit is a Markdown section.
    Large sections are additionally split by paragraphs.
    """

    chunks: list[Chunk] = []

    for document in documents:
        sections = parse_markdown_sections(
            document.content
        )

        document_chunk_number = 0

        for section in sections:
            content = normalize_text(
                section.content
            )

            if not content:
                continue

            section_parts = split_by_paragraphs(
                content,
                max_tokens,
            )

            for part_number, section_part in enumerate(
                    section_parts,
                    start=1,
            ):
                document_chunk_number += 1

                chunk_text = build_chunk_text(
                    document=document,
                    section=section,
                    content=section_part,
                )

                metadata = create_chunk_metadata(
                    document=document,
                    section=section,
                )

                chunk_id = (
                    f"python_"
                    f"{document.category}_"
                    f"{document.topic}_"
                    f"{document_chunk_number:03d}"
                )

                if len(section_parts) > 1:
                    chunk_id += f"_part_{part_number}"

                chunks.append(
                    Chunk(
                        id=chunk_id,
                        text=chunk_text,
                        metadata=metadata,
                    )
                )

    return chunks


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_chunks(
        chunks: list[Chunk],
) -> None:
    """
    Validate generated chunks before saving them.
    """

    if not chunks:
        raise ValueError(
            "No chunks were generated."
        )

    required_metadata = {
        "language",
        "version",
        "category",
        "topic",
    }

    ids = set()

    for chunk in chunks:
        if not chunk.id:
            raise ValueError(
                "Chunk has no ID."
            )

        if chunk.id in ids:
            raise ValueError(
                f"Duplicate chunk ID: {chunk.id}"
            )

        ids.add(chunk.id)

        if not chunk.text.strip():
            raise ValueError(
                f"Chunk has empty text: {chunk.id}"
            )

        missing_metadata = (
                required_metadata
                - chunk.metadata.keys()
        )

        if missing_metadata:
            raise ValueError(
                f"Chunk {chunk.id} is missing metadata: "
                f"{missing_metadata}"
            )


# ---------------------------------------------------------------------------
# JSONL storage
# ---------------------------------------------------------------------------

def save_chunks(
        chunks: list[Chunk],
        output_path=CHUNKS_FILE,
) -> None:
    """
    Save chunks to a JSONL file.

    One chunk = one JSON object = one line.
    """

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output_path.open(
            "w",
            encoding="utf-8",
    ) as file:
        for chunk in chunks:
            data = {
                "id": chunk.id,
                "text": chunk.text,
                "metadata": chunk.metadata,
            }

            file.write(
                json.dumps(
                    data,
                    ensure_ascii=False,
                )
                + "\n"
            )


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def print_chunk_statistics(
        documents: list[Document],
        chunks: list[Chunk],
) -> None:
    """
    Print information that allows us to manually verify
    the chunking stage.
    """

    token_counts = [
        estimate_tokens(chunk.text)
        for chunk in chunks
    ]

    average_tokens = (
        sum(token_counts) / len(token_counts)
        if token_counts
        else 0
    )

    print("=" * 70)
    print("CHUNKER CHECK")
    print("=" * 70)

    print(f"Documents:       {len(documents)}")
    print(f"Chunks:          {len(chunks)}")
    print(
        f"Average tokens:  {average_tokens:.1f}"
    )

    if token_counts:
        print(
            f"Min tokens:      {min(token_counts)}"
        )
        print(
            f"Max tokens:      {max(token_counts)}"
        )

    print()
    print("First 5 chunks:")
    print("-" * 70)

    for chunk in chunks[:5]:
        print(f"ID: {chunk.id}")
        print(
            f"Tokens: {estimate_tokens(chunk.text)}"
        )
        print(
            f"Metadata: {chunk.metadata}"
        )
        print("Text:")
        print(chunk.text)
        print("-" * 70)

    print()
    print(f"Output file: {CHUNKS_FILE}")
    print("=" * 70)
    print("Chunker completed successfully.")
    print("=" * 70)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    documents = load_documents()

    validate_documents(
        documents
    )

    chunks = create_chunks(
        documents=documents,
        max_tokens=800,
    )

    validate_chunks(
        chunks
    )

    save_chunks(
        chunks
    )

    print_chunk_statistics(
        documents=documents,
        chunks=chunks,
    )
