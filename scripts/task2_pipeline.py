import pandas as pd
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

# =========================
# 1. LOAD DATA
# =========================
df = pd.read_csv("data/raw/clean_reviews.csv")

df = df.dropna(subset=["review", "rating"])
df = df.drop_duplicates(subset=["review"])

df["review"] = df["review"].astype(str)

# =========================
# 2. SENTIMENT MODEL
# =========================
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def get_sentiment(text):
    result = sentiment_model(str(text))[0]
    return result["label"], result["score"]

df["sentiment_label"], df["sentiment_score"] = zip(
    *df["review"].apply(get_sentiment)
)

# =========================
# 3. SENTIMENT AGGREGATION
# =========================
print("\nSentiment by bank:")
print(df.groupby("bank")["sentiment_score"].mean())

print("\nSentiment by rating:")
print(df.groupby("rating")["sentiment_score"].mean())

# =========================
# 4. TF-IDF KEYWORDS
# =========================
vectorizer = TfidfVectorizer(stop_words="english", max_features=30)
vectorizer.fit(df["review"])
keywords = vectorizer.get_feature_names_out()

print("\nTop keywords:", keywords)

# =========================
# 5. THEME ASSIGNMENT
# =========================
def assign_theme(text):
    text = str(text).lower()

    if any(x in text for x in ["login", "password", "otp"]):
        return "Account Access Issues"
    elif any(x in text for x in ["slow", "error", "not working", "crash"]):
        return "Performance Issues"
    elif any(x in text for x in ["ui", "design", "interface"]):
        return "UI & Design"
    elif any(x in text for x in ["support", "help", "service"]):
        return "Customer Support"
    elif any(x in text for x in ["payment", "upi", "transfer"]):
        return "Transaction Issues"
    else:
        return "General Feedback"

df["identified_theme"] = df["review"].apply(assign_theme)

# =========================
# 6. FINAL OUTPUT
# =========================
output_cols = [
    "review",
    "rating",
    "date",
    "bank",
    "source",
    "sentiment_label",
    "sentiment_score",
    "identified_theme"
]

import os

os.makedirs("data/processed", exist_ok=True)

df[output_cols].to_csv("data/processed/task2_final_output.csv", index=False)

print("Saved to data/processed/task2_final_output.csv")

print("\nTask 2 completed successfully!")