# HealthMate AI: End-to-end Medical Chatbot using Generative AI

HealthMate AI is a professional-grade medical chatbot that leverages Generative AI (RAG - Retrieval Augmented Generation) to provide accurate answers based on medical documentation. It features a modern, responsive dashboard interface with advanced features like chat history and resource management.

![HealthMate AI Dashboard](https://raw.githubusercontent.com/your-username/End-to-end-Medical-chatbot-Generative-AI/main/static/screenshot.png) <!-- Replace with actual screenshot URL when available -->

## 🌟 Key Features

- **Advanced RAG Engine**: Combines Google Gemini Pro with Pinecone Vector Database for highly relevant medical answers.
- **Professional UI/UX**: Modern dark-themed dashboard with glassmorphism effects and smooth animations.
- **Chat History**: Persistent conversation storage using SQLite, allowing you to resume previous chats.
- **Resource Management**: Browse the specific medical documents being used as the knowledge base.
- **Responsive Design**: Fully functional on mobile, tablet, and desktop devices.
- **Fast Responses**: Optimized with Gemini 2.0 Flash for near-instant answers.

## 🛠️ Tech Stack

- **Framework**: Flask (Python)
- **AI Orchestration**: LangChain
- **LLM**: Google Gemini 2.0 Flash
- **Vector Database**: Pinecone
- **Embeddings**: Hugging Face (`all-MiniLM-L6-v2`)
- **Database**: SQLite (for chat history)
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript, Bootstrap 5, Font Awesome

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/End-to-end-Medical-chatbot-Generative-AI.git
cd End-to-end-Medical-chatbot-Generative-AI
```

### 2. Create and Activate Environment

```bash
# Using Conda
conda create -n medibot python=3.10 -y
conda activate medibot

# OR using venv
python -m venv venv
source venv/bin/activate  # Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configuration (.env)

Create a `.env` file in the root directory:

```ini
PINECONE_API_KEY="your_pinecone_api_key"
GOOGLE_API_KEY="your_google_api_key"
PINECONE_HOST="your_pinecone_index_host" # Optional
```

### 5. Setup Pinecone Index

Create an index in [Pinecone Console](https://app.pinecone.io/):
- **Name**: `medical-chatbot`
- **Dimensions**: `384`
- **Metric**: `cosine`

### 6. Ingest Data

Place your medical PDFs in the `data/` folder and run:

```bash
python store_index.py
```

### 7. Run the App

```bash
python app.py
```
Access the app at `http://localhost:8080`.

---

## ☁️ Deployment (AWS CICD)

This project is configured for automated deployment to AWS using GitHub Actions.

### Deployment Flow:
1. **GitHub Actions**: Triggers on push to `main`.
2. **Docker**: Builds a container image.
3. **ECR**: Original image is pushed to AWS Elastic Container Registry.
4. **EC2**: A self-hosted runner pulls the latest image and deploys it.

### Required GitHub Secrets:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`
- `ECR_REPO`
- `PINECONE_API_KEY`
- `GOOGLE_API_KEY`

---
*Disclaimer: This chatbot is for informational purposes only. Always consult a qualified healthcare provider for medical advice.*