# ai/gpt.py
from openai import OpenAI

from knowledgebase_pipeline.config import OPENAI_API_KEY


if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not configured")


client = OpenAI(api_key=OPENAI_API_KEY)


def ask_gpt(
    system_prompt: str,
    user_prompt: str,
    model: str = "gpt-5-mini",
) -> str:
    """
    Send a request to an OpenAI model and return its text response.
    """

    response = client.responses.create(
        model=model,
        instructions=system_prompt,
        input=user_prompt,
    )

    return response.output_text
