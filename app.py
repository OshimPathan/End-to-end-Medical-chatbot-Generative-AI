from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
import sqlite3
import datetime

# --- Database Setup ---
def init_db():
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_msg TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

embeddings = download_hugging_face_embeddings()


docsearch=PineconeVectorStore.from_existing_index(
    index_name="medical-chatbot",
    embedding=embeddings
)

retriever=docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)


prompt_template="""
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {input}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", prompt_template),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": input})
    answer = response["answer"]
    
    # Save to database
    try:
        conn = sqlite3.connect('chat_history.db')
        c = conn.cursor()
        c.execute("INSERT INTO chats (user_msg, bot_response) VALUES (?, ?)", (msg, answer))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error saving to DB: {e}")
        
    print("Response : ", answer)
    return str(answer)

@app.route("/history", methods=["GET"])
def history():
    conn = sqlite3.connect('chat_history.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM chats ORDER BY timestamp ASC")
    rows = c.fetchall()
    conn.close()
    
    history_data = []
    for row in rows:
        history_data.append({
            "user_msg": row["user_msg"],
            "bot_response": row["bot_response"],
            "timestamp": row["timestamp"]
        })
    return jsonify(history_data)

@app.route("/resources", methods=["GET"])
def resources():
    data_dir = os.path.join(os.getcwd(), "data")
    files = []
    if os.path.exists(data_dir):
        files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
    return jsonify(files)

@app.route("/clear_history", methods=["POST"])
def clear_history():
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute("DELETE FROM chats")
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8080)), debug=False)
