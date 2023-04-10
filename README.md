# FAANG Stock Data Analysis Project

## Overview

This goal project of this project was to apply everything I learned and build an end-to-end datapipline from the [Data Engineering Zoomcamp 2023](https://github.com/DataTalksClub/data-engineering-zoomcamp). 

The following steps to achieve the overall goal for the project are:

1. Select a dataset.
2. Create a pipeline to process the dataset into a datalake. 
3. Create a pipeline to move the dataset from the datalake into a data warehouse.
4. Transform the data in the data warehouse and prepare it for dashboard use.
5. Create a dashboard. 

## What are FAANG Stocks?

FAANG is an acronym that refers to a group of five major technology companies: Facebook (now Meta), Amazon, Apple, Netflix, and Google (now Alphabet). These companies are known for being some of the largest and most successful technology companies in the world. They have a significant impact on the stock market and the global economy as a whole, and their stocks are often in high demand among investors.


## About the Dataset.

The [dataset](https://www.kaggle.com/datasets/aayushmishra1512/faang-complete-stock-data) was taken from the Kaggle site. Kaggle is an online community and platform for data scientists and machine learning practitioners to participate in data science competitions, collaborate on projects, and access datasets and machine learning resources.

I have also created a small dataset which refers the companies to there stock_symbols.

The FAANG stock data contains the following information:
1. Date: refers to the date on which a particular transaction related to that stock took place.
2. Open: Opening Price of the stock.
3. High: Max Price of the stock of the day.
4. Low: Min Price of the stock of the day.
5. Close: Closing price of stock of the day. 
6. Adj Close: Data is adjusted using appropriate split and dividend multipliers for the closing price for the day.
7. Volume: Volume are the physical number of shares traded of that stock on a particular day.
8. Company: Name of the FAANG company
9. Stock_Symbol: The name of the ticker symbol of the company. 

## Problem/Questions

The goals for this project to answer the following questions.

* What was the overall trend of FAANG stocks during this period?
* What was the average daily trading volume of FAANG stocks during this period?
* Which FAANG company had the highest percentage increase in stock price during this period?

Some of the problems that I was faced with the project was that, the dataset was separated between the 5 companies.
While trying to achieve the goals of the project. (mentioned in the overview section)
I needed to find a way to combine the dataset together to order to run an analysis on the data and answer the questions. 

## Technologies 

The technologies that were used in order to achieve the goal for this project are:

* Cloud: [Google Cloud](https://cloud.google.com)
* Data lake: [Google Cloud Storage](https://cloud.google.com/storage)
* Data warehouse: [BigQuery](https://cloud.google.com/bigquery)
* Data transformation: [DBT](https://www.getdbt.com/)
* Infrastructure: [Terraform](https://www.terraform.io/)
* Orchestration: [Prefect](https://www.prefect.io/)
* Data visualization: [Google Looker Studio](https://cloud.google.com/looker)
* Github: [Github](https://github.com/)

## Project Architecture

<p align="center">
  <img width="700" height="400" src="https://github.com/enochiankim/data-engineering-zoomcamp-2023_Final_Project/blob/main/images/Project_Architecture.PNG">
</p>

This project architecture is setup to do the following:

* This process will repeat six times for the six tables.
* A script called `etl_process.py` will first take retrieve raw stock data from the github page and be placed into a csv file and converted in a parquet file. 
* Once the files are converted into a parquet file, a new column will be added to be specify the name of the company and the files will be placed into a Google Cloud Storage bucket (data lake).
* Once the files are loaded into the bucket, they will be taken from the bucket and moved into Bigquery (data warehouse) where the files will be inserted into tables for dbt use. 
* I ran two SQL commands to merge the tables together and to partition accordingly (commands are in the flows section).
* For the dbt process, since we have 6 different tables, the dbt model will combine the tables according the correct columns in order to form a brand new table which will be used for visualizations.
* Once the dbt process is completed, the visualizations can now be created on Google Looker Studio. 
* Terraform is used configure and deploy the remaining GCP resources we need for our project.
* Prefect is used to orchestrate the ETL process.

## Results

Below are the results of the dashboard.

The dashboard link can be found [here.](https://lookerstudio.google.com/u/0/reporting/c53de9ae-0f9d-49a1-8810-2251b7d209cf/page/qVmLD)

FAANG stock data overall
<p align="left">
  <img width="800" height="700" src="https://github.com/enochiankim/data-engineering-zoomcamp-2023_Final_Project/blob/main/images/FAANG%20Overall.PNG">
</p>

FAANG Average Volume
<p align="left">
  <img width="800" height="700" src="https://github.com/enochiankim/data-engineering-zoomcamp-2023_Final_Project/blob/main/images/FAANG_Bar.PNG">
</p>


FAANG Highest Percentage Increase
<p align="left">
  <img width="800" height="700" src="https://github.com/enochiankim/data-engineering-zoomcamp-2023_Final_Project/blob/main/images/FAANG_Line.PNG">
</p>

Findings from the results:

* Apple has the highest average volume overall.
* Amazon and Google have similar highest percentage increase.
* Nexflix and Apple have the lowest recorded price however Netflix has much less volume than Apple.
* Amazon has the highest recorded price and has second least amount of volume.
* Facebook has the third most volume and the low and high are also the third most.

## Reproducing this Project

1. Clone this repo then install the packages that is needed for this project.
```bash
pip install -r requirements.txt
```
2. Setup Google Cloud Environment: 
- Create a [Google Cloud Platform project](https://console.cloud.google.com/cloud-resource-manager)
- Configure Identity and Access Management (IAM) for the service account, giving it the following privileges: BigQuery Admin, Storage Admin and Storage Object Admin
- Make sure to download the JSON credentials and save it
- Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install-sdk)
- Let the [environment variable point to your GCP key](https://cloud.google.com/docs/authentication/application-default-credentials#GAC), authenticate it and refresh the session token.
3. Setup Terraform Infrastructure:
-If you do not have Terraform, first install it [link](https://developer.hashicorp.com/terraform/downloads) and add it to your PATH.
-After you have downloaded and installed it, run the following commands:
```bash
cd terraform/
terraform init
terraform plan -var="project=<your-gcp-project-id>"
terraform apply -var="project=<your-gcp-project-id>"
```
4. Setup Prefect Orchestration:
- Once the required python packages have been installed, install prefect.
- In order to setup prefect, run the following command and access this UI http://127.0.0.1:4200/:
```bash
prefect orion start
```
- Make sure to register your Google Cloud Storage Bucket and BigQuery credentials on top of that, the Docker Box too.
- Also make sure that the names of the block match within these files `etl_process.py` and the block section of the repo.
- Next step, you will store the data in both the both Google Cloud Storage Bucket and BigQuery running the following in the command line:
```bash
cd flows/
python etl_process.py
```
- If you want to run this in docker, run the following commands:
```bash
cd Prefect/
docker image build -t <docker-username>/stock:zoom .
docker image push <docker-username>/stock:zoom
```
- Then deploy the docker by running this command:
```bash
cd flows/
python docker_deploy.py
```
- Run this command afterwards:
```bash
prefect agent start
```
- Then this contained flow from the command line:
```bash
prefect deployment run etl-parent-flow/docker_stock_flow --param "companies=[Amazon,Apple,Facebook,Google,Neflix]"
```
5. After running all of these commands, you should have the data uploaded in both Google Cloud Storage and BigQuery, check and verify that the data is there. 

6. Setup dbt:
- In order to run the dbt flow, you need to create a dbt account, you can create one [here](https://cloud.getdbt.com/)
- Once dbt is setup, login setup the project, clone the repo again and go to develop. 
- Once you are in develop, check the bottom right and you should see a Ready sign.
- If you see that sign run the following command:
```bash
dbt run
```
- This dbt process will create the final dataset called final_faang_stock_data. This dataset will be used to create the data visualization on Google Looker Studio
7. Next go to [Google Looker Studio](https://cloud.google.com/looker) and you can create the visualization needed for this project. 

