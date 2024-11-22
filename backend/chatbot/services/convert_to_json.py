from transformers import pipeline
import json
from datetime import datetime
# Initialize the QA pipeline
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", device=0)

def process_user_file(file_path):
    """Reads the content of a text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def answer_question(context, question, model_pipeline):
    """Get an answer from the pipeline using the provided context."""
    answer = model_pipeline(question=question, context=context)
    return {
        "question": question,
        "answer": answer["answer"],
        "score": answer["score"]
    }

def chunk_text(text, chunk_size=1000):
    """Splits the text into smaller chunks to fit model input limits."""
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks


def save_interaction_to_json(question, answer, score, file_path="interactions.json"):
    interaction = {
        "question": question,
        "answer": answer,
        "score": score,
        "timestamp": datetime.now().isoformat()
    }

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(interaction)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)