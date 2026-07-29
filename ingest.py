import os
import chromadb


def ingest_runbooks():
    """Reads markdown runbooks and indexes them into local ChromaDB."""
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name="linux_runbooks")

    kb_dir = "./knowledge_base"
    if not os.path.exists(kb_dir):
        print(f"Error: '{kb_dir}' directory not found.")
        return

    documents = []
    ids = []
    metadatas = []

    for idx, filename in enumerate(os.listdir(kb_dir)):
        if filename.endswith(".md"):
            filepath = os.path.join(kb_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                documents.append(content)
                ids.append(f"runbook_{idx}")
                metadatas.append({"filename": filename})

    if documents:
        collection.add(
            documents=documents,
            ids=ids,
            metadatas=metadatas
        )
        print(f"Successfully indexed {len(documents)} runbooks into ChromaDB!")
    else:
        print("No .md files found in knowledge_base/")


if __name__ == "__main__":
    ingest_runbooks()