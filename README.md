# <img src="static/images/logo.png" width="40" height="40"> HealthMate AI: End-to-end Medical Chatbot using Generative AI

HealthMate AI is a professional-grade medical chatbot that leverages Generative AI (RAG - Retrieval Augmented Generation) to provide accurate answers based on medical documentation. It features a modern, responsive dashboard interface with advanced features like voice interaction, chat history, and resource management.

<p align="center">
  <img src="static/images/logo.png" width="200" alt="HealthMate AI Logo">
</p>

## 🌟 Key Features

- **Advanced RAG Engine**: Combines Google Gemini Pro with Pinecone Vector Database for highly relevant medical answers.
- **Voice Interaction**: Integrated Speech-to-Text and Text-to-Speech capabilities for hands-free operation.
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
- **Embeddings**: Hugging Face (`sentence-transformers/all-MiniLM-L6-v2`)
- **Database**: SQLite (for chat history)
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript, Bootstrap 5, Font Awesome

## 📂 Project Structure

```
├── app.py                 # Main Flask application
├── store_index.py         # Script to ingest data into Pinecone
├── src/
│   ├── helper.py          # Helper functions for data processing
│   └── prompt.py          # System prompts for the LLM
├── templates/
│   └── chat.html          # Main chat interface
├── static/
│   ├── style.css          # Custom styling
│   └── images/            # Assets
├── data/                  # Directory for medical PDF documents
└── requirements.txt       # Python dependencies
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10 - 3.12 (Tested on 3.12)
- Pinecone API Key
- Google Gemini API Key

### 1. Clone the Repository

```bash
git clone https://github.com/OshimPathan/End-to-end-Medical-chatbot-Generative-AI.git
cd End-to-end-Medical-chatbot-Generative-AI
```

### 2. Create and Activate Environment

```bash
# Using Conda
conda create -n medibot python=3.12 -y
conda activate medibot

# OR using venv
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

> [!IMPORTANT]
> Use the provided `requirements.txt` to avoid dependency conflicts with `torch` and `transformers`.

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

## 🐳 Run with Docker

You can also run the application using Docker to ensure a consistent environment.

1. **Build the Image**
   ```bash
   docker build -t medical-chatbot .
   ```

2. **Run the Container**
   ```bash
   docker run -d -p 8080:8080 \
     -e PINECONE_API_KEY="your_key" \
     -e GOOGLE_API_KEY="your_key" \
     medical-chatbot
   ```

---

## ⚠️ Troubleshooting

**`RuntimeError: operator torchvision::nms does not exist`**
This error occurs due to a version mismatch between `torch` and `torchvision`. Ensure you have installed the exact versions specified in `requirements.txt`:
```bash
pip uninstall torch torchvision transformers -y
pip install -r requirements.txt
```

**`ModuleNotFoundError: No module named 'langchain_huggingface'`**
This indicates an outdated environment. Run `pip install -r requirements.txt` to update your packages.

---

## ☁️ Deployment (AWS CICD)

This project is configured for automated deployment to AWS using GitHub Actions.

### Required GitHub Secrets:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`
- `ECR_REPO`
- `PINECONE_API_KEY`
- `GOOGLE_API_KEY`

---
*Disclaimer: This chatbot is for informational purposes only. Always consult a qualified healthcare provider for medical advice.*