# Starbucks Capstone Project

## Table of Contents
 * [Project Motivation](#project-motivation)
 * [Software & Libraries](#software-and-libraries)
 * [Files & Datasets](#files-and-datasets)
 * [Python files](#python-files)

Check out the blog post!

### Project Motivation

The motivation for this project is to analyze records of Starbucks' transactional, demographic, and promotional data to develop a machine learning classifier aimed at identifying the key features that predict the success of promotional offers. By analyzing customer demographics, promotional engagement, and various promotional metrics, I aim to determine which factors most impact customer purchasing decisions in a promotional offer.

After uploading and cleaning the data, exploratory data analysis was performed to characterize the data, look for missing data and outliers, and to determine data suitability for a machine learning model. After the data was combined and cleaned, candidate classification models and data transformers were chosen from resources in the scikit-learn documentation. The models were trained and fitted, tuned, and analyzed. Due to the binary nature of the problem (whether or not a customer completed an offer), a logistic regression model turned out to be the most effective. Finally, the model features were analyzed and ranked by importance with the aim of providing insight into the development of new promotional offers.

### Software and Libraries

This project was completed using Jupyter Lab v3.5.3 running Python v3.11.9 and the following Python packages:
| Package     |   Version   |
| ----------- | ----------- |
| Numpy       |   v1.26.4   |
| Pandas      |   v2.2.2    |
| Plotly      |   v5.21.0   |
| Matplotlib  |   v3.8.4    |
| Scikit-learn|   v1.4.2    |
| json
| math 


### Files and Datasets
Starbucks.ipynb
  * The jupyter notebook contining the development and analysis
README.md
  * This file

Datasets
Data were provided from Starbucks through the Udacity platform as three JSON files. These files contain simulated data from the Starbucks Rewards mobile app.
  * portfolio.json
    * Offer IDs and metadata on each offer (i.e. duration, barrier-of-entry, etc.)
  * profile.json
    * Demographic data for each user having made transactions in this series of datasets
  * transcript.json
    * Records of transactions and customer interactions with offers

The schema of the data files were provided by Udacity:

#### profile.json
Rewards program users (17000 users x 5 fields)

 - gender: (categorical) M, F, O, or null
 - age: (numeric) missing value encoded as 118
 - id: (string/hash)
 - became_member_on: (date) format YYYYMMDD
 - income: (numeric)

#### portfolio.json
Offers sent during 30-day test period (10 offers x 6 fields)

 - reward: (numeric) money awarded for the amount spent
 - channels: (list) web, email, mobile, social
 - difficulty: (numeric) money required to be spent to receive reward
 - duration: (numeric) time for offer to be open, in days
 - offer_type: (string) bogo, discount, informational
 - id: (string/hash)

#### transcript.json
Event log (306648 events x 4 fields)

 - person: (string/hash)
 - event: (string) offer received, offer viewed, transaction, offer completed
 - value: (dictionary) different values depending on event type
 - offer id: (string/hash) not associated with any "transaction"
 - amount: (numeric) money spent in "transaction"
 - reward: (numeric) money gained from "offer completed"
 - time: (numeric) hours after start of test

![Page1](/Project-2/images/Page_1.png)


![Page2](/Project-2/images/Page_2.png)
