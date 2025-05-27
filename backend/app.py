from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS # Needed for cross-origin requests from frontend
from knowledge_base import knowledge_base # Import your knowledge base
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app) # Enable CORS for all routes, allowing your frontend to talk to it

# --- Knowledge Base Processing (for smarter matching) ---
# Extract just the questions for TF-IDF Vectorizer
questions = [item["question"] for item in knowledge_base]

# Initialize TF-IDF Vectorizer
# TF-IDF stands for Term Frequency-Inverse Document Frequency.
# It's a numerical statistic that reflects how important a word is to a document in a collection or corpus.
# We're using it here to convert our questions into numerical vectors.
vectorizer = TfidfVectorizer().fit(questions)
question_vectors = vectorizer.transform(questions)

# Function to find the best matching answer
def find_best_answer(user_question):
    # Convert the user's question into a TF-IDF vector
    user_question_vector = vectorizer.transform([user_question])

    # Calculate cosine similarity between user's question and all questions in knowledge base
    # Cosine similarity measures the cosine of the angle between two non-zero vectors.
    # It determines whether two vectors are pointing in roughly the same direction.
    # Higher similarity score means closer meaning.
    similarities = cosine_similarity(user_question_vector, question_vectors).flatten()

    # Get the index of the most similar question
    best_match_index = np.argmax(similarities)
    best_match_score = similarities[best_match_index]

    # You can set a threshold for similarity. If the match is not good enough, return a default answer.
    # This threshold might need tuning.
    if best_match_score > 0.4: # A threshold of 0.4 means it has to be at least somewhat similar
        return knowledge_base[best_match_index]["answer"]
    else:
        return "I'm sorry, I don't have information on that specific topic. Could you please rephrase your question or ask something else related to SFA operations?"

# --- Flask Routes ---
@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').lower() # Convert to lowercase for easier matching

    # Get the answer from our knowledge base
    answer = find_best_answer(user_message)

    return jsonify({"answer": answer})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)