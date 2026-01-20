# ============================================
# Helmet Detection – JSON Q&A Engine (FINAL)
# ============================================

import pandas as pd
import json

# --------------------------------------------
# 1. Load detection results
# --------------------------------------------
df = pd.read_csv("detections.csv")

# --------------------------------------------
# 2. Question → Answer Logic
# --------------------------------------------
def answer_question(question):
    q = question.lower()

    if "total" in q:
        answer = len(df)

    elif (
        "without helmet" in q
        or "helmet violation" in q
        or "violations" in q
        or "no helmet" in q
    ):
        answer = int((df["class"] == "Without Helmet").sum())

    elif "with helmet" in q:
        answer = int((df["class"] == "With Helmet").sum())

    elif "average confidence" in q:
        answer = round(float(df["confidence"].mean()), 3)

    else:
        answer = "Question not supported"

    return {
        "question": question,
        "answer": answer
    }

# --------------------------------------------
# 3. Run (Example)
# --------------------------------------------
if __name__ == "__main__":
    question = "How many helmet violations are there?"
    result = answer_question(question)
    print(json.dumps(result, indent=2))
