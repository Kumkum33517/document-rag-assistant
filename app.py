import os
import streamlit as st
from src.config import DOCS_DIR
from src.pipeline import ingest, ask

st.set_page_config(page_title="Document RAG Assistant", page_icon="📄")
st.title("📄 Document RAG Assistant")
st.caption("Answers come only from your uploaded documents.")

os.makedirs(DOCS_DIR, exist_ok=True)

with st.sidebar:
    st.header("Documents")
    uploads = st.file_uploader(
        "Upload PDF / TXT", type=["pdf", "txt", "md"], accept_multiple_files=True
    )
    if uploads:
        for f in uploads:
            with open(os.path.join(DOCS_DIR, f.name), "wb") as out:
                out.write(f.getbuffer())
        st.success(f"Saved {len(uploads)} file(s). Now rebuild the index.")

    if st.button("Build / Rebuild index"):
        with st.spinner("Indexing documents..."):
            try:
                n_pages, n_chunks = ingest()
                st.success(f"Indexed {n_pages} pages into {n_chunks} chunks")
            except Exception as e:
                st.error(str(e))

    st.write("**Files:**")
    for name in os.listdir(DOCS_DIR):
        st.write(f"- {name}")

question = st.text_input("Ask a question about your documents")

if question:
    with st.spinner("Thinking..."):
        try:
            answer, contexts = ask(question)
            st.subheader("Answer")
            st.write(answer)
            with st.expander("Sources retrieved"):
                for c in contexts:
                    st.markdown(f"**{c['source']}**, page {c['page']}, score {c['score']:.2f}")
                    st.write(c["text"])
                    st.divider()
        except Exception as e:
            st.error(str(e))
