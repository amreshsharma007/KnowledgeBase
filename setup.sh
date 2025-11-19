#!/bin/bash

echo "🔥 KnowledgeBase Offline Chatbot — Initial Setup Starting..."

# -------------------------------
# 1. Create folder structure
# -------------------------------
echo "📁 Creating folders..."
mkdir -p models
mkdir -p docs

touch models/.gitkeep
touch docs/.gitkeep

# -------------------------------
# 2. Create virtual environment
# -------------------------------
echo "🐍 Creating virtual environment..."
python3 -m venv venv

echo "📦 Activating virtual environment..."
source venv/bin/activate

# -------------------------------
# 3. Install requirements
# -------------------------------
echo "📦 Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

# -------------------------------
# 4. Download embedding model
# -------------------------------
echo "⬇️ Downloading BGE-small embedding model from HuggingFace..."

cd models
git clone https://huggingface.co/BAAI/bge-small-en-v1.5 bge-small-en-v1.5

cd ..

# -------------------------------
# 5. Final instructions
# -------------------------------
echo ""
echo "🎉 Setup Complete!"
echo ""
echo "📌 Next steps:"
echo "1. Put your PDF, Word, Excel files inside: docs/"
echo "2. Pull the LLM model manually (only once):"
echo "     ollama pull phi3:mini"
echo "3. Run your bot:"
echo "     source venv/bin/activate"
echo "     python bot.py"
echo ""
echo "🚀 You're ready to go!"
