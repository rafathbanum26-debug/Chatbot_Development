# Week 9 – Chatbot Development Using Ollama

## 1. Project Overview

This project focuses on building an interactive AI chatbot using Python and Ollama. The chatbot uses a locally running Large Language Model (LLM) to answer user questions and maintain conversation context.

## 2. Objectives

- To understand the architecture of an AI chatbot powered by an LLM.
- To build a command-line chatbot using Python and Ollama.
- To implement conversation history for context-aware responses.
- To save conversations for future integration with LangChain.

## 3. Technologies Used

- Python
- Ollama
- Gemma 3 (1B) Large Language Model
- Jupyter Notebook
- Pandas
- CSV files

## 4. Project Structure

```text
Chatbot_Development/
├── dataset/
│   ├── chat_history.csv
│   ├── sample_questions.csv
│   ├── chatbot_logs.txt
│   └── responses.csv
├── notebook/
│   └── Week9_Chatbot_Development.ipynb
├── chatbot.py
├── README.md
└── requirements.txt
```

## 5. Installation

1. Install Python and Ollama.
2. Download the language model:

```bash
ollama pull gemma3:1b
```

3. Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

## 6. How to Run the Project

Run the following command in the VS Code terminal:

```bash
python chatbot.py
```

Enter questions in the terminal to interact with the chatbot. Type `exit` to stop the conversation.

## 7. Features

- Interactive command-line conversation.
- Local LLM-based response generation.
- Conversation history maintained during the current session.
- Automatic saving of questions and responses in CSV files.
- Timestamps for conversation records.
- Text logging for application activity and errors.

## 8. Dataset Files

- `chat_history.csv` – Stores user questions, chatbot responses, and timestamps.
- `sample_questions.csv` – Contains sample questions for testing.
- `responses.csv` – Stores chatbot responses for analysis.
- `chatbot_logs.txt` – Records application logs.

## 9. Testing and Observations

The chatbot can be tested with general knowledge, reasoning, programming, and educational questions. Its responses should be checked for correctness and completeness. Response quality depends on the model and the question asked.

## 10. Limitations

- The chatbot requires Ollama and a downloaded model.
- Response speed depends on the computer's resources.
- Some responses may be incorrect or incomplete.
- Conversation context is maintained during the running session; previous conversations are saved in CSV files.

## 11. Conclusion

This project demonstrates how to develop an interactive AI chatbot using Python and Ollama. It generates responses using a local language model, maintains conversation context, and saves conversation records for analysis. The project provides a foundation for future integration with LangChain.
