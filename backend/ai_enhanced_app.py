# SFA_Chatbot/backend/ai_enhanced_app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from enhanced_knowledge_base import knowledge_base # Import the ENHANCED knowledge base
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os
import openai # We'll need this for the AI helper
from dotenv import load_dotenv # For securely loading API key

# Load environment variables from .env file (if it exists)
load_dotenv()

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# --- OpenAI API Setup (for the AI helper) ---
# It tries to get the key from environment variable or .env file
openai.api_key = os.getenv("OPENAI_API_KEY")
USE_OPENAI = bool(openai.api_key) # Only use OpenAI if an API key is provided

if USE_OPENAI:
    print("OpenAI API key found. AI enhancement is ENABLED.")
else:
    print("OpenAI API key NOT found. AI enhancement is DISABLED (will only use knowledge base).")

# --- Knowledge Base Processing ---
# Combine original question, keywords, and training examples for vectorization
all_training_phrases = []
qa_map = {} # Map phrase to its corresponding knowledge base item

for item in knowledge_base:
    # Add the main question
    all_training_phrases.append(item["question"].lower())
    qa_map[item["question"].lower()] = item

    # Add keywords
    for kw in item.get("keywords", []):
        all_training_phrases.append(kw.lower())
        qa_map[kw.lower()] = item

    # Add training examples
    for te in item.get("training_examples", []):
        all_training_phrases.append(te.lower())
        qa_map[te.lower()] = item

# Initialize TF-IDF Vectorizer with a larger vocabulary
vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english').fit(all_training_phrases)
question_vectors = vectorizer.transform(all_training_phrases)

# --- Conversation History (for suggestions) ---
# This will store the IDs of the last few answered questions to avoid suggesting the same thing
conversation_history = []
MAX_HISTORY_LENGTH = 3

# --- Logging for Unanswered Questions (for learning) ---
unanswered_questions_log = []

# Function to get the best matching answer from our knowledge base
def find_best_answer_from_kb(user_question):
    user_question_vector = vectorizer.transform([user_question.lower()])
    similarities = cosine_similarity(user_question_vector, question_vectors).flatten()

    best_match_index = np.argmax(similarities)
    best_match_score = similarities[best_match_index]

    # You can adjust this threshold. A higher threshold means it needs to be a very close match.
    # 0.4-0.6 is often a good starting range.
    if best_match_score > 0.4:
        # Get the original knowledge base item from the qa_map
        matched_phrase = all_training_phrases[best_match_index]
        return qa_map[matched_phrase], "📚 Found in knowledge base"
    else:
        return None, None # No good match found in KB

# Function to get an answer from OpenAI's GPT
def get_openai_answer(user_question):
    if not USE_OPENAI:
        return None

    try:
        # We can give it some context about SFA chatbots
        system_message = "You are a helpful AI assistant for an SFA (Sales Force Automation) app. Provide concise and relevant answers. If the question is outside SFA operations, answer generally but professionally."

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo", # You can try "gpt-4" if you have access and want more advanced responses
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_question}
            ],
            max_tokens=150, # Limit the length of the response
            temperature=0.7 # Creativity level (0.0-1.0), 0.7 is balanced
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None

@app.route('/')
def home():
    return "SFA Chatbot AI-Enhanced Backend is running!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip()

    if not user_message:
        return jsonify({"answer": "Please type a question."})

    # 1. Try to find an answer in the enhanced knowledge base
    matched_item, source_tag = find_best_answer_from_kb(user_message)
    answer = ""
    suggestions_to_send = []

    if matched_item:
        answer = matched_item["answer"]
        source_tag = source_tag
        # Add the answered question's ID to history
        conversation_history.append(matched_item["id"])
        if len(conversation_history) > MAX_HISTORY_LENGTH:
            conversation_history.pop(0) # Keep history limited

        # Generate suggestions, avoiding recently discussed topics
        all_possible_suggestions = []
        for item in knowledge_base:
            if item["id"] != matched_item["id"]: # Don't suggest the current topic
                all_possible_suggestions.extend(item.get("suggestions", []))

        # Filter out suggestions already in recent history
        unique_suggestions = list(set(all_possible_suggestions)) # Remove duplicates
        for s in unique_suggestions:
            # Check if the suggestion is for an item recently covered
            # This requires careful matching of suggestion text to question text in KB
            suggestion_is_in_history = False
            for history_id in conversation_history:
                history_item = next((kb_item for kb_item in knowledge_base if kb_item["id"] == history_id), None)
                if history_item and s.lower() in history_item["question"].lower():
                    suggestion_is_in_history = True
                    break
            if not suggestion_is_in_history:
                suggestions_to_send.append(s)
            if len(suggestions_to_send) >= 3: # Limit suggestions to 3
                break

    else:
        # 2. If not found in KB, try OpenAI
        ai_answer = get_openai_answer(user_message)
        if ai_answer:
            answer = ai_answer
            source_tag = "🧠 AI Enhanced answer"
        else:
            # 3. If no answer found, log and provide generic response
            answer = "I'm sorry, I don't have information on that specific topic in my knowledge base. Please rephrase your question or ask something else related to SFA operations."
            source_tag = "🤷 No direct match"
            unanswered_questions_log.append(user_message)
            print(f"Logged unanswered question: {user_message}") # For monitoring

    # Combine answer with source tag and suggestions
    final_response = f"{answer}\n\n<small><i>{source_tag}</i></small>"
    if suggestions_to_send:
        final_response += "\n\nYou might also want to know about:\n" + "\n".join([f"- {s}" for s in suggestions_to_send])

    return jsonify({"answer": final_response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)