# SFA_Chatbot/backend/training_script.py

import os
import datetime

def review_unanswered_questions():
    log_file_path = "unanswered_questions.log" # This is where ai_enhanced_app.py will ideally log
    if not os.path.exists(log_file_path):
        print("No unanswered questions log file found yet.")
        print("The chatbot needs to be run and receive questions it can't answer to generate this log.")
        return

    print("--- Reviewing Unanswered Questions Log ---")
    print("These are questions the chatbot couldn't find a direct answer for.")
    print("Consider adding these topics or more training examples to your 'enhanced_knowledge_base.py'.")
    print("-" * 40)

    try:
        with open(log_file_path, 'r') as f:
            questions = [line.strip() for line in f if line.strip()]

        if not questions:
            print("The log file is empty. No unanswered questions recorded yet.")
            return

        # Count frequencies
        question_counts = {}
        for q in questions:
            question_counts[q] = question_counts.get(q, 0) + 1

        # Sort by most frequent
        sorted_questions = sorted(question_counts.items(), key=lambda item: item[1], reverse=True)

        for q, count in sorted_questions:
            print(f"Question: '{q}' (Asked {count} time(s))")

        print("-" * 40)
        print("Tip: If you see a common theme, add a new entry to enhanced_knowledge_base.py")
        print("     with appropriate keywords and training examples for that topic.")

    except Exception as e:
        print(f"Error reading log file: {e}")

if __name__ == "__main__":
    # Note: In ai_enhanced_app.py, for simplicity, I used `unanswered_questions_log.append()`.
    # For a real log file persistence, you'd modify `ai_enhanced_app.py` to write to this file:
    # Example change in ai_enhanced_app.py (inside the else block for no match):
    # with open("unanswered_questions.log", "a") as log_file:
    #     log_file.write(f"{datetime.datetime.now()}: {user_message}\n")
    #
    # For now, this script will just tell you if the log file exists and how to generate it.
    review_unanswered_questions()