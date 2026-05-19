import pandas as pd
import psycopg2

# Load dataset
df = pd.read_csv("data/processed/task2_final_output.csv")

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="bank_reviews",
    user="postgres",
    password="postgre",  
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# -----------------------
# 1. Insert banks
# -----------------------
unique_banks = df["bank"].unique()

for bank in unique_banks:
    cur.execute("""
        INSERT INTO banks (bank_name)
        VALUES (%s)
        ON CONFLICT (bank_name) DO NOTHING;
    """, (bank,))

conn.commit()

# -----------------------
# 2. Insert reviews
# -----------------------
for _, row in df.iterrows():

    cur.execute("""
        SELECT bank_id FROM banks WHERE bank_name = %s;
    """, (row["bank"],))

    bank_id = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO reviews (
            bank_id,
            review_text,
            rating,
            review_date,
            data_source,
            sentiment_label,
            sentiment_score,
            identified_theme
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        bank_id,
        row["review"],
        row["rating"],
        row["date"],
        row["source"],
        row["sentiment_label"],
        row["sentiment_score"],
        row["identified_theme"]
    ))

conn.commit()

cur.close()
conn.close()

print("✅ Data inserted successfully!")