import os
from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer

def create_vectorstore(docs):
    print("🔍 Generating embeddings...")
    embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    texts = [d.page_content for d in docs]
    metadatas = [d.metadata for d in docs]

    # generate embeddings
    vectors = embedder.encode(texts)

    # FAISS requires this specific format:
    text_embeddings = list(zip(texts, vectors))

    # build store
    vectorstore = FAISS.from_embeddings(
        text_embeddings=text_embeddings,
        embedding=embedder
    )

    # save path
    save_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "vectorstore"))
    os.makedirs(save_path, exist_ok=True)

    print(f"💾 Saving vectorstore to: {save_path}")
    vectorstore.save_local(save_path)

    print("✅ Vectorstore saved successfully!")
