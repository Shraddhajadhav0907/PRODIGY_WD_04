import pandas as pd
import os

print("STEP 1: Script started")

# Show where Python is running from
print("Current working directory:")
print(os.getcwd())

# Load dataset
df = pd.read_csv(r"C:\Users\LENOVO\OneDrive\文档\GitHub\PRODIGY_WD_04\PRODIGY_DS_04\twitter_training.csv")

print("STEP 2: Dataset loaded successfully")

# Show column names
print("STEP 3: Columns in dataset:")
print(df.columns.tolist())

# Show first 5 rows
print("STEP 4: Dataset preview:")
print(df.head())

# IMPORTANT: find correct sentiment column
# Use the THIRD column as sentiment (Twitter dataset standard)
sentiment_col = df.columns[2]
print("STEP 5: Using sentiment column:", sentiment_col)

print("STEP 5: Sentiment column found:", sentiment_col)

# Count sentiments
sentiment_counts = df[sentiment_col].value_counts()

print("STEP 6: Sentiment Counts:")
print(sentiment_counts)

# Save result
output_file = "sentiment_summary.csv"
sentiment_counts.to_csv(output_file)

print("STEP 7: Sentiment summary saved as", output_file)
print("✅ TASK COMPLETED SUCCESSFULLY")

import matplotlib
matplotlib.use("Agg")  # prevents GUI issues
import matplotlib.pyplot as plt

# Create bar graph
plt.figure(figsize=(6,4))
sentiment_counts.plot(kind="bar")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.title("Sentiment Distribution on Twitter Data")

# Save graph as image
plt.savefig("sentiment_graph.png")
plt.close()

print("📊 Graph saved as sentiment_graph.png")