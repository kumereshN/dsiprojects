# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 2: Ames Housing Data and Kaggle Challenge

### N Kumeresh, DSI-18-Singapore

## Problem Statement

As part of the Ames real estate consulting agency, my team is tasked with creating a **regression based model to predict the housing price using the Ames Housing Dataset** to assist real estate agents with their day to day tasks. Currently, the real estate agents make use of their domain knowledge, search through the web to help them or rely on outdated spreadsheets containing the sale prices to provide estimated prices for their clients. This is time-consuming and cumbersome. With a model, the agents can make quick and effective decisions in creating sale prices for the houses in Ames.

## Executive Summary

The project reviews the data covering the extensive features of the Ames Housing dataset to construct a regression model to predict the sale prices of the house. The data is has many features, such the year built, renovated, the square feet of the basements and rooms. Analysis of the dataset involves find strong positive and negative correlations between the features and the saleprice to be used in constructing the model. Of the 4 models that were created, Linear, Ridge, Lasso and ElasticNet Regression, Lasso Regression model had the best score. 

## Conclusions and Recommendations

Based on the Exploratory Data Analysis, I found a strong positive correlation for variables that have square feet in them, such as `1st_flr_sf `. Size of the house seems to have a significant impact on the price of the house. `Fireplace` and `Kitchen Quality`, neighborhood, zonning dummies are also some of the features that have significant impact on the price. I also took a log transformation of the highly skewed house sale price.

I've used 4 different types of models, Linear Regression, Ridge Regresion, Lasso Regression and ElasticNet Regression to predict the housing price. All of the models except, ElasticNet, achieved stable results and scores, the coefficients being almost the same. The model achieved a R-squared score of approximately 84% ~ 85% on the train-validation sets and this show consistency across all the models, except Elastic Net which favored `l1-ratio` of 1 with 1 being Lasso Regression.

`gr_liv_area`, `total_bsmt_sf`, `year_remod/add`, `garage_area`,`bsmtfin_sf_1` have strong positive correlations while `Masonry veneer type brick face`, `house_age` and the `bldg_type` have strong negative correlations with the saleprice. I believe that this model can prove to be useful to the real estate agents for their day to day work as it's found to predict fairly accurately. Further feature engineering to create better features to improve the model's performance can useful in the future.

---

### Datasets

#### Provided Data

Train and Test datasets were provided as part of the project:

- [Train set](./datasets/train.csv.csv)
- [Test set](./data/test.csv)


---
## Data Dictionary

[Link](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)