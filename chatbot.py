import csv
import logging
from datetime import datetime
from pathlib import Path

import ollama

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "dataset"

DATASET_DIR.mkdir(exist_ok=True)

HISTORY_FILE = DATASET_DIR / "chat_history.csv"
RESPONSES_FILE = DATASET_DIR / "responses.csv"
LOG_FILE = DATASET_DIR / "chatbot_logs.txt"

MODEL = "gemma3:1b"

# Configure logging
logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    force=True
)


def create_csv_file(file_path, headers):
    if not file_path.exists() or file_path.stat().st_size == 0:
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)


create_csv_file(
    HISTORY_FILE,
    ["timestamp", "user_message", "bot_response"]
)

create_csv_file(
    RESPONSES_FILE,
    ["timestamp", "user_message", "bot_response"]
)

# Conversation history for contextual responses
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful educational AI chatbot. "
            "Give clear, simple and accurate answers. "
            "If you are unsure, say so."
        )
    }
]


def save_conversation(timestamp, question, answer):
    with open(
        HISTORY_FILE, "a", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, question, answer])

    with open(
        RESPONSES_FILE, "a", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, question, answer])

    logging.info("Conversation saved successfully")


def main():
    print("=" * 45)
    print("  WEEK 9 - AI CHATBOT USING OLLAMA")
    print("=" * 45)
    print("Model:", MODEL)
    print("Type 'exit' to stop the chatbot.\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() == "exit":
                print("Chatbot: Goodbye! Have a nice day.")
                break

            if not user_input:
                print("Chatbot: Please enter a question.")
                continue

            messages.append({
                "role": "user",
                "content": user_input
            })

            response = ollama.chat(
                model=MODEL,
                messages=messages
            )

            answer = response["message"]["content"]
            timestamp = datetime.now().isoformat(
                timespec="seconds"
            )

            print("\nChatbot:", answer, "\n")

            messages.append({
                "role": "assistant",
                "content": answer
            })

            save_conversation(timestamp, user_input, answer)

        except KeyboardInterrupt:
            print("\nChatbot stopped.")
            break

        except Exception as error:
            print("Error:", error)
            logging.exception("Chatbot error")


if __name__ == "__main__":
    main()