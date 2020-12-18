# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Web APIs and Classification

### N Kumeresh, DSI-18-Singapore

## Problem Statement

To assist one of our colleagues, who is a moderator of the entrepreneur subreddit, with filtering out the investing posts in the entrepreneur subreddit.
The entrepreneur subreddit is mostly filled with irrelevant posts from the investing subreddit, which causes annoyance to the business owners who share their business ideas. By constructing a classifier model, we can use it to seperate business ideas and business investment strategies for new business owners who desire to start their side hustle. The two classifier models that will be constructed will be the **Logistics Regression Classifier and the Multi-nominal Bayes Model**. The performance metric to be used for measuring against the models will be **Accuracy** as the model needs to classify the post according to their respective subreddit.

## Executive Summary

The project aims to create a classification model to distinguish posts from the entrepreneur subreddit and the investing subreddit. The posts and title were scrapped from their respective subreddits using reddit's API and the requests library. The posts were "cleaned" to remove unwanted characters and a brief exploratory data analysis was done on the dataset. 

From the analysis, Term Frequency Inverse Document Frequency (TFIDF) Vectorizer was found to perform slightly better than the Count Vectorizer. Also, Multi-nominal Naive Bayes Model performed slightly better than the Logistics Regression model even though their performance was comparable. Both models also have a higher accuracy score compared to Baseline accuracy.


## Conclusions and Recommendations

To conclude, posts and their titles that were transformed with TFIDF Vectorizer were shown to perform slightly better than the posts transformed with the Count Vectorizer. A similar finding was seen for datasets trained on Multi-nominal Naive Bayes (MNNB) model performed slightly better than Logistic Regression. 
Even though both models have shown close performance, the Multi-nominal Naive Bayes model with TFIDF Vectorizer has shown to be the best model with a accuracy test score of 0.9428 while the logistic regression model with TFIDF Vectorizer coming close with an accuracy test score of 0.9336. Both models also beats the baseline accuracy score of 0.5387.

I would recommend MNNB model to be deployed in the entrepreneur subreddit as it's show to have a very high accuracy in filtering out investing subreddit posts from the entrepreneur subreddit and this would help to save time and energy instead of manually looking through the posts.

---

### Datasets

#### Provided Data

The datasets were scrapped from the entreprenuer and investing subreddit as part of the project:

- [Cleaned Entrepreneur set](./datasets/cleaned_entre_df.csv)
- [Cleaned Investing set](./data/cleaned_invest_df.csv)