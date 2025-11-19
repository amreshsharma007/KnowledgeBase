import os
from llama_index.core import SimpleDirectoryReader

def load_all_documents(folder="docs"):
    supported_ext = [".pdf", ".doc", ".docx", ".xls", ".xlsx"]

    files = [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if any(f.lower().endswith(ext) for ext in supported_ext)
    ]

    if not files:
        print("⚠️  No supported documents found in:", folder)

    documents = []
    for file in files:
        docs = SimpleDirectoryReader(input_files=[file]).load_data()
        documents.extend(docs)

    return documents
