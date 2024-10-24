# Disaster Response Pipeline Project

## Table of Contents
 * [Instructions on how to interact with the project](#instructions-on-how-to-interact-with-the-project)
 * [Software & Libraries](#software-and-libraries-used)
 * [Project Motivation](#project-motivation)
 * [File Descriptions](#file-descriptions)
 * [Components](#components)
 * [Licensing, Authors, Acknowledgements, etc.](#licensing-authors-acknowledgements-etc)
 
### Instructions on how to interact with the project:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

### Software and libraries used

This project was completed using Jupyter Lab v3.5.3 running Python v3.11.9 and the following Python packages:
| Package     |   Version   |
| ----------- | ----------- |
| Numpy       |   v1.26.4   |
| Pandas      |   v2.2.2    |
| Plotly      |   v5.21.0   |
| Matplotlib  |   v3.8.4    |
| Scikit-learn|   v1.4.2    |
| Statsmodels |    v0.14.1  |
| sqlite3     | v1.2.19 |
| sqlaclchemy | v1.2.19 |
| nltk        | v3.2.5 |
| pickle      | v0.7.4 |

### Project Motivation
The ultimate motivation for this project is to categorize messages on-the-fly during a natural disater. This has the potential to allow responders to operate more efficiently in these situations. Here we worked off of a data set provided by [Figure Eight](https://appen.com/) to build a NLP categorization model and to deploy the results to an API dashboard.

### File Structure and Descriptions
\app    

| - template    
| |- master.html # main web app    
| |- go.html # classification result page after query    
|- run.py # Flask backend file that runs the web app    


data    

|- disaster_categories.csv # categorical data file    
|- disaster_messages.csv # messages data file    
|- process_data.py # ETL pipeline file  
|- {database_file}.db # Database saved from ETL pipeline   


models   

|- train_classifier.py # ML pipeline file 
|- {model_name}.pkl # saved model from ML pipeline  


README.md    

### Python files
There are three Python files I completed for this project. 

#### 1. ETL Pipeline (`process_data.py`)
A Python script which loads two data sets and writes a database file:

 - Loads the messages and categories data files
 - Merges the two datasets
 - Cleans the data by converting the categories into logical categorical columns
 - Stores it in a SQLite database
  
#### 2. ML Pipeline (`train_classifier.py`)
A Python script which loads a database and generates a parallel-serial, cross-validated NLP machine learning model:

 - Loads data from the SQLite database
 - Splits the dataset into training and test sets
 - Constructs an NLP machine learning pipeline
 - Trains and tunes the ML model using GridSearchCV
 - Outputs accuracy metrics of the model
 - Exports the final model to a pickle file
 
#### 3. Flask Web App
The project includes a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data. The outputs are shown below:

![app3](https://user-images.githubusercontent.com/54407746/98725077-9826b800-238c-11eb-828f-864dce8cbd9b.JPG)


![app1](https://user-images.githubusercontent.com/54407746/98724735-159df880-238c-11eb-8338-bc4b4e0b1c39.JPG)


![app2](https://user-images.githubusercontent.com/54407746/98724932-5bf35780-238c-11eb-8a93-ebb09ab2d510.JPG)

