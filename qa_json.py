import pandas as pd
import json

# Load detection data
df = pd.read_csv("detections.csv")

def answer_question(question):
    question = question.lower()

    if "total detections" in question:
        return {
            "question": question,
            "answer": int(len(df))
        }

    elif "without helmet" in question:
        count = int((df["class"] == "Without Helmet").sum())
        return {
            "question": question,
            "answer": count
        }

    elif "with helmet" in question:
        count = int((df["class"] == "With Helmet").sum())
        return {
            "question": question,
            "answer": count
        }

    elif "average confidence" in question:
        return {
            "question": question,
            "answer": round(float(df["confidence"].mean()), 3)
        }

    else:
        return {
            "question": question,
            "answer": "Question not supported"
        }

# Example question
question = "How many people are without helmet?"
result = answer_question(question)

print(json.dumps(result, indent=2))
