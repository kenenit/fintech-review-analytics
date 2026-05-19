import pandas as pd
import matplotlib.pyplot as plt

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("data/processed/task2_final_output.csv")

print("Dataset loaded:", df.shape)

# =========================
# 1. SENTIMENT DISTRIBUTION BY BANK
# =========================
sentiment_counts = df.groupby(["bank", "sentiment_label"]).size().unstack()

sentiment_counts.plot(kind="bar", stacked=True, figsize=(8,5))
plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")
plt.legend(title="Sentiment")
plt.tight_layout()
plt.show()


# =========================
# 2. RATING DISTRIBUTION BY BANK
# =========================
df.boxplot(column="rating", by="bank", figsize=(8,5))

plt.title("Rating Distribution by Bank")
plt.suptitle("")  # remove automatic title
plt.xlabel("Bank")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()


# =========================
# 3. THEME DISTRIBUTION BY BANK
# =========================
theme_counts = df.groupby(["bank", "identified_theme"]).size().unstack()

theme_counts.plot(kind="bar", stacked=True, figsize=(10,6))
plt.title("Theme Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")
plt.legend(title="Theme", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# =========================
# 4. NEGATIVE REVIEWS (COMPLAINTS)
# =========================
negative_df = df[df["sentiment_label"] == "NEGATIVE"]

complaints = negative_df.groupby(["bank", "identified_theme"]).size().unstack()

complaints.plot(kind="bar", figsize=(10,5))
plt.title("Negative Themes (Complaints) by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Complaints")
plt.legend(title="Theme", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# =========================
# 5. FEATURE REQUEST DETECTION
# =========================
keywords = ["feature", "add", "want", "need", "please"]

feature_df = df[df["review"].str.contains("|".join(keywords), case=False, na=False)]

feature_counts = feature_df.groupby(["bank", "identified_theme"]).size().unstack()

feature_counts.plot(kind="bar", figsize=(10,5))
plt.title("Feature Requests by Bank")
plt.xlabel("Bank")
plt.ylabel("Count")
plt.legend(title="Theme", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# =========================
# 6. QUICK INSIGHT PRINT (OPTIONAL)
# =========================
print("\n--- BASIC INSIGHTS ---")

for bank in df["bank"].unique():
    bank_df = df[df["bank"] == bank]
    print(f"\n{bank}")
    print("Total reviews:", len(bank_df))
    print("Avg rating:", bank_df["rating"].mean())
    print("Most common theme:", bank_df["identified_theme"].value_counts().idxmax())