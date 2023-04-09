# FAANG Stock Data Analysis Project

## Overview

This goal project of this project was to apply everything I learned and build an end-to-end datapipline from the [Data Engineering Zoomcamp 2023](https://github.com/DataTalksClub/data-engineering-zoomcamp). 

In order to achieve the overall goal: 
1. Select a dataset.
2. Create a pipeline to process the dataset into a datalake. 
3. Create a pipeline to move the dataset from the datalake into a data warehouse.
4. Transform the data in the data warehouse and prepare it for dashboard use.
5. Create a dashboard. 

## What are FAANG Stocks?

FAANG is an acronym that refers to a group of five major technology companies: Facebook (now Meta), Amazon, Apple, Netflix, and Google (now Alphabet). These companies are known for being some of the largest and most successful technology companies in the world. They have a significant impact on the stock market and the global economy as a whole, and their stocks are often in high demand among investors.


## About the Dataset.

The [dataset](https://www.kaggle.com/datasets/aayushmishra1512/faang-complete-stock-data) was taken from the Kaggle. Kaggle is an online community and platform for data scientists and machine learning practitioners to participate in data science competitions, collaborate on projects, and access datasets and machine learning resources.

The FAANG stock data contains the following information:
1. Date: refers to the date on which a particular transaction related to that stock took place.
2. Open: Opening Price of the stock.
3. High: Max Price of the stock of the day.
4. Low: Min Price of the stock of the day.
5. Close: Closing price of stock of the day. 
6. Adj Close: Data is adjusted using appropriate split and dividend multipliers for the closing price for the day.
7. Volume: Volume are the physical number of shares traded of that stock on a particular day.

## Problem/Questions

The goal for this project to answer the following questions.

* What was the overall trend of FAANG stocks during this period?
* What was the average daily trading volume of FAANG stocks during this period?
* Which FAANG company had the highest percentage increase in stock price during this period?

The problem that I had was that, the dataset were separated between the 5 companies. 
I needed to find a way to combine the dataset together to order to run an analysis on the data and answer the questions. 

