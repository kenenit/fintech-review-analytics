# fintech-review-analytics
Customer Experience Analytics for Ethiopian Banking Apps

This project analyzes Google Play Store reviews for Ethiopian fintech applications to extract insights on customer sentiment, common complaints, and feature requests. It is part of the 10 Academy AI Mastery Week 2 Challenge.

📌 Project Overview

The goal of this project is to build an end-to-end data pipeline that:

Scrapes user reviews from Google Play Store
Cleans and preprocesses raw text data
Performs sentiment analysis and thematic extraction
Stores processed data in a relational PostgreSQL database
Generates insights for business decision-making
🏦 Banks Analyzed
PayPal
Google Pay
Revolut
📁 Project Structure
fintech-review-analytics/
│
├── data/
│   └── processed/
│       ├── clean_reviews.csv
│       └── task2_final_output.csv
│
├── scripts/
│   ├── schema.sql
│   └── load_to_postgres.py
│
├── src/
├── notebooks/
├── tests/
├── .github/workflows/
├── requirements.txt
└── README.md
🧪 Task 1 – Data Collection & Preprocessing
Objective

Scrape Google Play Store reviews and prepare a clean dataset for analysis.

Methodology
Used google-play-scraper to collect reviews
Extracted:
Review text
Rating (1–5)
Date
Bank/App name
Source (Google Play)
Cleaned dataset:
Removed duplicates
Handled missing values
Standardized date format (YYYY-MM-DD)
Output
Clean dataset saved as: clean_reviews.csv
Total records collected: 1200+
🧠 Task 2 – Sentiment & Thematic Analysis
Objective

Analyze user sentiment and extract key themes from reviews.

Approach
Sentiment Analysis
Model used: DistilBERT / VADER (based on implementation)
Output:
sentiment_label (POSITIVE / NEGATIVE / NEUTRAL)
sentiment_score (confidence score)
Thematic Analysis
Extracted keywords using NLP techniques
Grouped into themes such as:
Login Issues
Transaction Performance
UI/UX Feedback
Feature Requests
General Feedback
Output
Final processed dataset: task2_final_output.csv
🗄️ Task 3 – PostgreSQL Database Engineering
Objective

Store processed review data in a structured relational database.

Database Setup
Database name: bank_reviews
Schema Design
banks table
bank_id (PRIMARY KEY)
bank_name (UNIQUE)
reviews table
review_id (PRIMARY KEY)
bank_id (FOREIGN KEY → banks.bank_id)
review_text
rating (1–5)
review_date
data_source
sentiment_label
sentiment_score
identified_theme
ETL Pipeline

A Python script (load_to_postgres.py) was developed to:

Load processed CSV data
Insert unique banks into banks table
Map and insert review data into reviews table
Maintain referential integrity using foreign keys
Data Summary
Total reviews inserted: 1203
Bank distribution:
PayPal: 446
Google Pay: 336
Revolut: 421
Data Validation

Performed SQL checks:

Total row count verification
Bank-wise grouping
Null value checks

Example query:

SELECT b.bank_name, COUNT(*)
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;
Key Design Notes
The column source was renamed to data_source to avoid SQL reserved keyword conflicts.
Data types were selected for scalability and analysis compatibility.
⚙️ Technologies Used
Python
Pandas
PostgreSQL
psycopg2
Google Play Scraper
NLP (Transformers / VADER)
🚀 Next Steps (Task 4)
Sentiment visualization
Theme frequency analysis
Bank comparison dashboards
Business recommendations
📌 Author

Data Engineering Project – 10 Academy AI Mastery Program