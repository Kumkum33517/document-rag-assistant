# Document RAG Assistant

A fully local, document-based RAG app. Upload PDF/TXT/MD files, ask questions, and get answers grounded only in those documents, with sources shown. No API keys required.

## Stack
- Chunking: fixed-size with overlap (800 chars, 150 overlap)
- Embeddings: sentence-transformers all-MiniLM-L6-v2
- Vector store: FAISS (local, saved to data/index/)
- LLM: llama3.2:3b via Ollama (runs locally)
- UI: Streamlit
- Strict RAG prompt: answers only from retrieved context, otherwise replies "I could not find this in the provided documents."

## Setup (macOS)

1. Install Ollama and pull the model:

        brew install ollama
        brew services start ollama
        ollama pull llama3.2:3b

2. Create the environment and install dependencies:

        python3 -m venv venv
        source venv/bin/activate
        python -m pip install -r requirements.txt

3. Run the app:

        python -m streamlit run app.py

4. In the sidebar, upload documents (or use the ones in data/docs/), click "Build / Rebuild index", then ask questions.

## Run the tests

    python tests/test_questions.py

Runs the test questions, including one out-of-scope question that must be refused.

## Project structure

    app.py                 Streamlit UI
    src/config.py          Settings (chunk size, model names, top-k)
    src/loader.py          Reads PDF/TXT/MD files
    src/chunker.py         Splits text into overlapping chunks
    src/embedder.py        Text to vectors
    src/vector_store.py    Builds, saves and loads the FAISS index
    src/retriever.py       Semantic top-k retrieval
    src/prompts.py         Strict RAG prompt
    src/generator.py       Ollama LLM call
    src/pipeline.py        ingest() and ask()
    tests/                 Test questions
    data/docs/             Source documents

## Limitations
- Text-based PDFs only (no OCR for scanned files)
- A 3B model can occasionally answer loosely
- Each question is independent (no chat memory)