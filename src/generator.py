import ollama
from src.config import LLM_MODEL
from src.prompts import SYSTEM_PROMPT, build_prompt


def generate_answer(question, contexts):
    resp = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_prompt(question, contexts)},
        ],
        options={"temperature": 0},
    )
    return resp["message"]["content"]
