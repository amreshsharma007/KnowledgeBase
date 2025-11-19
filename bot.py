from llama_index.core import VectorStoreIndex, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from load_docs import load_all_documents

# ----------------------------
# 🔥 1. Load your local embedding model (BGE-small)
# ----------------------------
Settings.embed_model = HuggingFaceEmbedding(
    model_name="models/bge-small-en-v1.5",   # path in your project
    local_files_only=True                    # never use internet
)

# ----------------------------
# 🔥 2. Load documents
# ----------------------------
documents = load_all_documents("docs")

if not documents:
    print("⚠️ No supported documents found in docs/ folder.")
    exit(1)

print(f"Loaded {len(documents)} document chunks.")

# ----------------------------
# 🔥 3. Use local phi3 from Ollama
# ----------------------------
llm = Ollama(
    model="phi3:mini",
    request_timeout=120.0
)

# ----------------------------
# 🔥 4. Build vector index in-memory
# ----------------------------
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=Settings.embed_model
)

# ----------------------------
# 🔥 5. Create a chat engine
# ----------------------------
chat_engine = index.as_chat_engine(
    llm=llm,
    similarity_top_k=5,
    chat_mode="condense_question"
)

print("\n📚 Offline KnowledgeBase Chatbot Ready!")
print("Ask anything about your PDFs, Word, and Excel files.")
print("Type 'exit' to quit.\n")

# ----------------------------
# 🔥 6. Chat loop
# ----------------------------
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Bye!")
        break

    try:
        response = chat_engine.chat(user_input)
        print("Bot:", response, "\n")
    except Exception as e:
        print("⚠️ Error:", e)
