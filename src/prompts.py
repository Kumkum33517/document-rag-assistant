SYSTEM_PROMPT = """You are a document question-answering assistant.
Answer ONLY using the CONTEXT provided. Do not use outside knowledge.
If the answer is not in the context, reply exactly: "I could not find this in the provided documents."
Be concise. Mention the source file and page for the facts you use."""


def build_prompt(question, contexts):
    ctx = "\n\n".join(
        f"[{c['source']} | page {c['page']}]\n{c['text']}" for c in contexts
    )
    return f"CONTEXT:\n{ctx}\n\nQUESTION: {question}\n\nANSWER:"
