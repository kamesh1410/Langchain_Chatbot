from flask import Flask, request, jsonify
import faiss
import numpy as np
from langchain_huggingface import HuggingFaceEmbeddings
import os

app = Flask(__name__)

# Load FAISS index and embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Ensure FAISS index exists before loading
if not os.path.exists("faiss_index.bin"):
    raise FileNotFoundError("FAISS index file not found. Please run the index creation script.")

index = faiss.read_index("faiss_index.bin")

# Load course data
if not os.path.exists("data.txt"):
    raise FileNotFoundError("Data file not found. Please extract data first.")

with open("data.txt", "r", encoding="utf-8") as file:
    data = [line.strip() for line in file.readlines() if line.strip()]

# Function to retrieve answers from FAISS index
def get_answer(query):
    query_embedding = np.array([embeddings.embed_query(query)], dtype="float32")
    _, result_indices = index.search(query_embedding, k=3)
    
    # Collect multiple responses for better results
    answers = [data[i] for i in result_indices[0] if i < len(data)]
    
    if not answers:
        return "No relevant data found."
    
    return "\n".join(answers)

# API Route to handle GET requests
@app.route('/chat', methods=['GET'])
def chat():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query parameter is missing"}), 400
    
    answer = get_answer(query)
    
    # Enhanced response structure
    return jsonify({
        "query": query,
        "answer": answer
    })

if __name__ == '__main__':
    app.run(debug=True)
