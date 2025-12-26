# Task-04 | Sentiment Analysis on Twitter Data

## Project Overview
This project is part of *Task-04* of my Data Science Internship at *Prodigy InfoTech*.  
The objective was to perform *sentiment analysis* on Twitter posts related to various games and visualize the distribution of sentiments.

## Dataset
The dataset used is twitter_training.csv, which contains the following columns:
- *ID*: Unique identifier for each tweet
- *Game*: Name of the game
- *Sentiment*: Sentiment label (Positive, Negative, Neutral, Irrelevant)
- *Tweet*: Text content of the tweet

Note: The dataset does not contain headers, so they were manually assigned during preprocessing.

## Tools & Technologies
- *Python*
- *Pandas* – for data manipulation
- *Matplotlib* – for visualization

## Steps Performed
1. Loaded the dataset using Pandas and manually assigned column names.  
2. Counted the number of tweets in each sentiment category.  
3. Saved the sentiment counts to sentiment_summary.csv.  
4. Created a *bar graph* sentiment_graph.png to visualize the distribution of sentiments.

## Output
- sentiment_summary.csv → Table containing the count of each sentiment category.  
- sentiment_graph.png → Bar chart visualizing the sentiment distribution.

## Skills Gained
- Data Cleaning and Preprocessing  
- Sentiment Analysis  
- Data Visualization with Python  
- Working with real-world social media datasets

## Summary
This task helped me understand how to handle social media data, analyze sentiment patterns, and visually represent insights for effective data interpretation.